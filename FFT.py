import csv

with open('momentum_exchange.txt') as input_file:
   lines = input_file.readlines()
   newLines = []
   for line in lines:
      newLine = line.strip().split()
      newLines.append( newLine )

with open('output.csv', 'w') as test_file:
   file_writer = csv.writer(test_file)
   file_writer.writerows( newLines )


Open the input and output files
with open('output.csv', 'r') as infile, open('output1.csv', 'w') as outfile:
    # Read the lines from the input file
    lines = infile.readlines()
    
    # Iterate through the lines, skipping every alternate line
    for i, line in enumerate(lines):
        if i % 2 == 0 or line.strip():  # If it's an even line or not empty
            outfile.write(line)



import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('output1.csv', header=None)

# Split the DataFrame into two columns
column1 = df[0][-9999:]
column2 = df[1][-9999:]
column3 = df[2][-9999:]


# Create a figure and axis objects for the main plot and subplots
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

# Plot the second column against the first column as a line plot in the first subplot
ax1.plot(column1, column2, label='Drag Coefficient', linestyle='-')
ax1.set_xlabel('Time')
ax1.set_ylabel('Drag Coefficient')
ax1.set_title('Drag Coefficient vs Time')
ax1.grid(True)
ax1.legend()

# Plot the third column against the first column as a line plot in the second subplot
ax2.plot(column1, column3, label='Lift Coefficient', linestyle='-',color='red')
ax2.set_xlabel('Time')
ax2.set_ylabel('Lift Coefficient')
ax2.set_title('Lift Coefficient vs Time')
ax2.grid(True)
ax2.legend()

# Adjust layout
plt.tight_layout()

# Save the plot as an image file (e.g., PNG)
plt.savefig('plot_line_subplots.png')