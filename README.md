## Functional programming and built-in Python modules

### Task 1

A closure in programming is a function that preserves references to variables from its lexical context, that is, from the scope where it was declared.

Implement the `caching_fibonacci` function, which creates and uses a cache to store and reuse already calculated Fibonacci numbers.

**The Fibonacci series** is a sequence of numbers of the form: `0, 1, 1, 2, 3, 5, 8, ...`, where each subsequent number of the sequence is obtained by adding two previous members of the series.

In general, to calculate the nth term of the Fibonacci series, you need to calculate the expression: `F(n) = F^(n-1) + F^(n-2)`

This problem can be solved recursively by calling a function that calculates the numbers of the sequence until the call reaches terms less than `n = 1`, where the sequence is given.

#### Task requirements:

1. The `caching_fibonacci()` function should return the internal function `fibonacci(n)`.
2. `fibonacci(n)` calculates the nth Fibonacci number. If the number is already in the cache, the function must return the value from the cache.
3. If the number is not in the cache, the function must calculate it, store it in the cache, and return the result.
4. Using recursion to calculate Fibonacci numbers.

#### Recommendations for implementation:

As a recommendation, we will provide a pseudo code of the task.

> [!IMPORTANT] ☝ Pseudocode is a way of writing an algorithm or program code that is used to describe an idea or process in a human-readable form. It is not intended to be directly executed on a computer, but it helps developers clearly understand and plan how a program or algorithm will work. Its main purpose is to convey the idea of ​​the algorithm clearly and simply.

Here is the pseudocode for the caching_fibonacci function, which calculates the Fibonacci numbers using caching:

```python
FUNCTION caching_fibonacci
    Create an empty `cache` dictionary

    FUNCTION fibonacci(n)
        if n <= 0, return 0
        if n == 1, return 1
        if n у cache, return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci function
THE END OF FUNCTION caching_fibonacci
```

The `caching_fibonacci` function creates an internal `fibonacci` function and a `cache` dictionary to store the results of calculating Fibonacci numbers. Each time `fibonacci(n)` is called, it first checks whether a value for `n` is already stored in the `cache`. If the value is in the cache, it is returned immediately, which greatly reduces the number of recursive calls. If the value is not in the `cache`, it is calculated recursively and stored in the cache. The `caching_fibonacci` function returns an internal `fibonacci` function that can now be used to compute Fibonacci numbers using caching.

#### Example of using the function:

```python
# Getting a function fibonacci
fib = caching_fibonacci()

# Using the fibonacci function to calculate Fibonacci numbers
print(fib(10))  # prints 55
print(fib(15))  # prints 610
```

In this example, when you call `fib(10)` or `fib(15)`, the `fibonacci` function inside `caching_fibonacci` calculates the corresponding Fibonacci numbers, storing the previous results in the cache. This makes repeated calls for the same values ​​of `n` significantly faster, since they simply return the value from the cache. The closure allows `fibonacci(n)` to "remember" the `cache` state between different calls, which is key to caching the results of computations

---

### Task 2

We need to create a `generator_numbers` function that will parse the text, identify all valid numbers considered to be part of the income, and return them as a generator. Real numbers in the text are written without errors, clearly separated by spaces on both sides. You also need to implement the `sum_profit` function, which will use `generator_numbers` to sum these numbers and calculate the total profit.

#### Task requirements:

1. The function `generator_numbers(text: str)` should take a string as an argument and return a generator that iterates over all valid numbers in the text. Real numbers in the text are considered to be written without errors and are clearly separated by spaces on both sides.
2. The function `sum_profit(text: str, func: Callable)` should use the `generator_numbers` generator to calculate the total sum of the numbers in the input string and accept it as an argument when called.

#### Recommendations for implementation:

1. Use regular expressions to identify real numbers in text, making sure the numbers are clearly separated by spaces.
2. Apply the `yield` construct in the `generator_numbers` function to create the generator.
3. Make sure that `sum_profit` correctly processes the data from `generator_numbers` and sums all the numbers.

#### Example of using the function:

```python
text = "The total income of the employee consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
```

#### Expected result:

```python
Total income: 1351.46
```

---

### Task 3 (optional)

Develop a Python script to analyze log files. The script must be able to read a log file passed as a command line argument and output statistics by logging levels, for example, `INFO`, `ERROR`, `DEBUG`. Alternatively, the user can specify the logging level as the second command line argument to retrieve all entries for that level.

Log files are files that contain records of events that have occurred in the operating system, software, or other systems. They help monitor and analyze system behavior, detect and diagnose problems.

To perform the task, take the following example of a log file:

```python
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
```

#### Task requirements:

1. The script must accept the path to the log file as a command line argument.
2. The script must take an optional command line argument after the log file path argument. It is responsible for outputting all records of a certain logging level. And takes the value according to the logging level of the file. For example, the `error` argument will output all `ERROR` level entries from the log file.
3. The script should read and analyze the log file, counting the number of entries for each logging level (`INFO`, `ERROR`, `DEBUG`, `WARNING`).
4. Implement the function `parse_log_line(line: str) -> dict` to parse log lines.
5. Implement the `load_logs(file_path: str) -> list` function to load logs from a file.
6. Implement the `filter_logs_by_level(logs: list, level: str) -> list` function to filter logs by level.
7. Implement `count_logs_by_level(logs: list) -> dict` to count records by logging level.
8. The results should be presented in the form of a table with the number of records for each level. To do this, implement the `display_log_counts(counts: dict)` function, which formats and outputs the results. It accepts the results of the `count_logs_by_level` function.

#### Recommendations for implementation:

1. Before you begin, familiarize yourself with the structure of your log file. Note the date and time format, logging levels `INFO`, `ERROR`, `DEBUG`, `WARNING` and message structure.
2. Understand how the various components of the log are separated, usually by spaces or special characters.
3. Divide your task into logical blocks and functions for better readability and further extensibility.
4. Parsing a log line is performed by the \*\*\*\*function `parse_log_line(line: str) -> dict`, which takes a line from the log as an input parameter and returns a dictionary with parsed components: date, time, level, message. Use string methods such as `split()` to split a string into parts.
5. Log files are loaded by the `load_logs(file_path: str) -> list` function, which opens the file, reads each line and applies the `parse_log_line` function to it, saving the results to a list.
6. Filtering by logging level is performed by the function `filter_logs_by_level(logs: list, level: str) -> list`. It will allow you to retrieve all log entries for a specific logging level.
7. Counting records by logging level should be done by the function `count_logs_by_level(logs: list) -> dict`, which goes through all records and counts the number of records for each logging level.
8. Display the results using the `display_log_counts(counts: dict)` function, which formats and displays the counting results in a readable form.
9. Your script must be able to handle different types of errors, such as missing a file or errors when reading it. Use `try`/`except` blocks to handle exceptional situations.

#### Example of using:

When running the script

```python
python [main.py](<http://main.py/>) /path/to/logfile.log
```

We should expect the following output

```python
Logging level    | Quantity
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1
```

If a student wants to look through all the records of the singing level of the logan, you can run the script with an additional argument, for example:

```python
python main.py path/to/logfile.log error
```

You will see detailed statistics for the levels, as well as detailed information for all records with the `ERROR` level.

```python
Logging level    | Quantity
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Details of lairs for the ranks 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

---

### Task 4

Pay for the console bot of the assistant from the front office and give payment for the help of the decorators.

#### Task requirements:

1. All requests made by the correspondent must be processed through the help of the `input_error` decorator. This decorator is responsible for turning the system into a notification like `“Enter user name”`, `“Give me name and phone please”`, etc.
2. The `input_error` decorator is guilty of eliminating errors that occur in functions - `handler` and these errors: `KeyError`, `ValueError`, `IndexError`. If there is a fault, the decorator is responsible for turning the correct line of the decorator. Vikonannya does not bother with the program.

#### Recommendations for implementation:

In addition, I will add the `input_error` decorator to handle the `ValueError` processing

```python
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner
```

Then we burned the decorator with the `add_contact` function of our bot, so that we began to fix the `ValueError`.

```python
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
```

You need to add processors to other commands (functions), and add to the decorator the processing of other types of errors with related information.

#### Task requirements:

1. The presence of the `input_error` decorator, which generates error messages for all commands.
2. Processing errors for types `KeyError`, `ValueError`, `IndexError` in functions with the help of the `input_error` decorator.
3. The skin function for processing commands uses the `input_error` decorator, which handles regular notifications and rotates notifications about notifications.
4. The correct reaction of the bot to the destruction of commands is the processing of amends entered without completing the program.

#### Example of using:

When you run the script, the dialogue with the bot is similar to the same.

```python
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356
Enter a command:
```
