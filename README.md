# Funda test assignment

## Running the solution

Create a file called ```.env``` and add line for the API key (```API_KEY={key}```)

Install the dependencies from ```requirements.txt``` (using ```pip install -r requirements.txt```)

Execute ```main.py``` (using ```python main.py```).

## Language choice

I opted to do this assignment in Python. Mainly due to Python being the best for these kinds of tasks in my opinion. It is also my most commonly used programming language, so with my experience with the language and libraries used in this task I believe it best shows my general style of programming and method of solving a task. I wanted to also add a solution using .NET/C#, but unfortunately was low on time this week.

## Files

`test_environment.ipynb` is a Jupyter notebook that I used to experiment with the API to see what kind of data and error codes it returns (among other things). This file serves no purpose in the final solution (found in `main.py`) but could give insight into my thinking process. `main.py` contains my solution to this task.

## AI

I opted not to use AI for this task. Even though I believe AI can be a useful tool (when used correctly as assisting tool rather than something that generates entire bits of code for you), I deemed it to be out of place in a task that is supposed to show my programming style and thought process. The code was fully written by me, with debugging help from stackoverflow threads (For example [this thread](https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module) for the requests library error handling).

## Results

Below you can find my results (at the time of writing the script) for both queries

### Results: Amsterdam query

| MakelaarNaam                         | Count |
|--------------------------------------|-------|
| Heeren Makelaars                     | 165   |
| KRK Makelaars Amsterdam              | 109   |
| Broersma Wonen                       | 105   |
| Ramón Mossel Makelaardij o.g. B.V.   | 98    |
| Eefje Voogd Makelaardij              | 91    |
| Hallie & Van Klooster Makelaardij    | 87    |
| Carla van den Brink B.V.             | 87    |
| De Graaf & Groot Makelaars           | 78    |
| Makelaardij Van der Linden Amsterdam | 75    |
| Linger OG Makelaars en Taxateurs     | 74    |


### Results: Amsterdam + Tuin query

| MakelaarNaam                                      | Count |
|---------------------------------------------------|-------|
| Broersma Wonen                                    | 30    |
| Heeren Makelaars                                  | 28    |
| Linger OG Makelaars en Taxateurs                  | 25    |s
| DSTRCT Amsterdam                                  | 20    |
| De Graaf & Groot Makelaars                        | 19    |
| Carla van den Brink B.V.                          | 18    |
| KIJCK. makelaars Amsterdam                        | 18    |
| KRK Makelaars Amsterdam                           | 16    |
| VON POLL REAL ESTATE                              | 15    |
| Keizerskroon Makelaars - Certified Expat Broker   | 14    |



