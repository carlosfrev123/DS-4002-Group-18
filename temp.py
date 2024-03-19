
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('./DATA/3P_CLEAN.csv')

# Extract the required columns
season = data['Season'][::-1]
three_point_percentage = data['3P%'][::-1]
field_goal_percentage = data['FG%'][::-1]

# Plot the data
plt.plot(season, three_point_percentage, label='3P%')
plt.plot(season, field_goal_percentage, label='FG%')

# Add labels and title
plt.xlabel('Season')
plt.ylabel('Percentage')
plt.title("3P% and FG% over Time")

# Rotate the x-axis labels
plt.xticks(rotation=90)

# Add legend
plt.legend()

# Show the plot
plt.show()
