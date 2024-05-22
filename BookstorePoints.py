books = int(input('How many books have you purchased this month?\n')) # User input for number of books

points = 0 # initializes points awarded

if books < 2: # Assigns points based on number of books purchsed
    points = 0
elif books < 4:
    points = 5
elif books < 6:
    points = 15
elif books < 8:
    points = 30
else:
    points = 60

print('Number of CSU Global Bookstore Book Club Points:', points) # prints out number of points
