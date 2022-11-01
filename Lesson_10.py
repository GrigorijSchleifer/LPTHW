weekdays = [
    "monday", 
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"]

def week_formatting(weekday):
    print(f"{weekday}")

for i in weekdays:
    print(f"Today is:\n \t*{week_formatting(i)}")




tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backlash_cat = "I'm \\ a \\ cat"

fat_cat = '''
I'll do a list:
\n
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)
