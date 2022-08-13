# defining types_of_people variable
types_of_people = 10
# defining x
x = f"There are {types_of_people} types of people."

# difining binary variable
binary = "binary"

# defining do_not variable
do_not = "don't"
# using f something to insert virables into text
y = f"Those who do know {binary} and those who {do_not}."

# printing the x variable
print(x)
# printin the y variable
print(y)

# printing and inserting f style the x variable
print(f"I said: {x}")
# printing and inserting f style the y variable 
print(f"I also said: '{y}'")

# defining helarious variable to False
hilarious = False
# defining the joke_evaluation variable and preparing for format method
joke_evaluation = "Isn't that joke so funny?! {}"

# printing and formation ... really cool ...
print(joke_evaluation.format(hilarious))

# defining w character variable
w = "This is the left side of ..."
# defining e character variable
e = "a sting with a right side."

# printing w and e
print(w + e)