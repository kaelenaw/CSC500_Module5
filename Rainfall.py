# Initialize list of months, total_rain
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
total_rain = 0.0
avg_rainfall = 0.0

# Get user input for number of years
years = int(input('Enter number of years: \n'))

# Outer loop for years
for y in range(years):
    print('Year {} Rainfall:\n'.format(y + 1))
    # Inner loop for months in each year
    for m in months:
        rainfall = float(input('Inches of rainfall in {}: '.format(m)))
        total_rain += rainfall
    print()

num_months = years * 12
avg_rainfall = total_rain / num_months

print('Number of Months:', num_months)
print('Total Inches of Rainfall: {:.1f}'.format(total_rain))
print('Average Monthly Rainfall: {:.1f}'.format(avg_rainfall))
