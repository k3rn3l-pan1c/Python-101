# Write your function below!

def fizz_count(x):
        count = 0
        for item in x:
            count = count + (item == "fizz") # could use an if

        return count
