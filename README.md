# How does it works?

It reads content of the page from given URL, removes all unreadable content and print 10 most frequent words (if more than two words have the same occurances - alphabetical sort is used).

# Running instructions

To run application you need only **requests** dependency.

Either install **requests** on your machine globally or build virtualenv for this application:

## Install required libraries if needed
1. create virtualen:
```
virtualenv venv/
```
2. install dependents:
```
pip install < requirements.txt
```

## Run application

```
python main.py
```
Give URL in standard input and get results

or
```
python main.py https://www.exeample.com/
```
if you wish to put URL give URL as command

Take to account, that using -u option and giving URL ignores standard input.

## Results

Results are printed to output and saved in **results.txt**.

Every successful execution of this program changes **results.txt**.

# Unit tests

If you want to execute unittests, you need to **unittest** dependency installed.

You can run unit tests by executing command:
```
python -u unittest tests.py
```


