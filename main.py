import pandas as pd
import requests
import dotenv
import os
import time

dotenv.load_dotenv()
api_key = os.environ["API_KEY"]

def call_api(search_query, type="koop", page_number=1, page_size=25, max_retries=5):
    """
    Args:
        search_query (String): URL substring that describes the search specifics (example for formatting: /amsterdam/tuin)
        type (String): type of search query (koop/huur)
        page_number (Int/String): Page number
        page_size (Int/String): Number of items on fetched page -> cannot exceed 25 based on rudimentary tests

    Returns:
        JSON data representation of requested page results
    """
    api_url = f'http://partnerapi.funda.nl/feeds/Aanbod.svc/json/{api_key}/?type={type}&zo={search_query}&page={page_number}&pagesize={page_size}'


    # loop request in case of timeouts and rate limits
    retries = 0
    backoff_base = 3 # base for exponential backoff timer in seconds

    while True:
        try:
            response = requests.get(api_url, timeout=10)

        # only timeout is an error we can fix on the fly in this script, other errors are likely an issue with user input/network/the api itself
        except requests.exceptions.Timeout:
            retries += 1

            # back off after network exception before retry
            if retries > max_retries:
                raise RuntimeError("ERROR: Max retries reached (due to repeated timeouts)")
            
            sleep_time = backoff_base ** retries
            print(f'Request timeout, trying again after backoff of {sleep_time}s') 
            time.sleep(backoff_base ** retries)
            continue

        except requests.exceptions.TooManyRedirects:
            raise RuntimeError("ERROR: Too many redirects")

        except requests.exceptions.HTTPError:
            raise RuntimeError(f"ERROR: Invalid HTTP response")

        except requests.exceptions.RequestException:
            raise RuntimeError(f"ERROR: network issue")

        # return on succesful request
        if response.status_code == 200:
            return response.json()

        # experienced status 401 seemingly for rate limitation in testing, so counting both 401 and 429 as rate limitation status codes for this case
        if response.status_code == 401 or response.status_code == 429:
            retries += 1

            if retries > max_retries:
                raise RuntimeError(f'Max retries reached, status code: {response.status_code}')

            sleep_time = backoff_base ** retries
            print(f'Rate limited, trying again after backoff of {sleep_time}s')
            time.sleep(sleep_time)
            continue

        # edge case for other status codes 
        raise RuntimeError(f"Non-200 status code (not rate limiter): {response.status_code}\nResponse: {response.text}")


def get_total_page_count(search_query):
    """
    Args:
        search_query (String): URL substring that describes the search specifics (example for formatting: /amsterdam/tuin)

    Returns:
        JSON data representation of requested page results
    """
    res = call_api(search_query)
    return res["Paging"]["AantalPaginas"]


def get_all_items(search_query):
    """
    Args:
        search_query (String): URL substring that describes the search specifics (example for formatting: /amsterdam/tuin)

    Returns:
        Dataframe of MakelaarIDs for all items that match the search query
    """
    df = pd.DataFrame()
    # loop over pages to get all items adding each page to the to-be-returned dataframe
    for i in range(1, get_total_page_count(search_query) + 1):
        page_info = call_api(search_query, page_number=i)
        ids = pd.DataFrame(page_info["Objects"])[["MakelaarNaam"]]
        df = pd.concat([df, ids], ignore_index=True)

    return df


def get_makelaars_with_most_listings(search_query):
    """
    Args:
        search_query (String): URL substring that describes the search specifics (example for formatting: /amsterdam/tuin)

    Returns:
        Name and amount of objects listed for sale for the 10 makelaars that have the most listings
    """
    all_items = get_all_items(search_query)
    return all_items.value_counts().head(10)


if __name__ == "__main__":
    print(get_makelaars_with_most_listings("/amsterdam"))
    print(get_makelaars_with_most_listings("/amsterdam/tuin"))