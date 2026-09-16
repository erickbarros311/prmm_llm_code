import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the file (replace with the actual name of your Excel file)
file_name = 'r_diff_copilot.xlsx'

# Read the Excel spreadsheet
df = pd.read_excel(file_name)

# Select the first 3 columns and rename them to simplify the code
df = df.iloc[:, :3]
df.columns = ['Time', 'Reference', 'Generated']

# 2. Configure the figure with an appropriate size
plt.figure(figsize=(10, 6))

# Plot the Reference Model (Black, solid, thick)
plt.plot(df['Time'], df['Reference'],
         label='Reference Model $R_r(t)$',
         color='black', linestyle='-', linewidth=5)

# Plot the Generated Model (Red, dashed, overlaid)
plt.plot(df['Time'], df['Generated'],
         label='Copilot Model $R_g(t)$',
         color='red', linestyle='--', linewidth=3)

# 3. Academic Formatting (Titles, legends, and axes)
plt.xlabel('Time ($t$)', fontsize=18)
plt.ylabel('Reliability $R(t)$', fontsize=18)
plt.title('Comparison of Reliability Models', fontsize=20)

# Axis tick marks/numbers fontsize
plt.tick_params(axis='both', which='major', labelsize=16)


# Configure the legend for the top right corner
plt.legend(fontsize=18, loc='upper right', framealpha=1.0, edgecolor='black')

# Add a grid to facilitate visual reading
plt.grid(True, linestyle='-', alpha=0.5)
plt.tight_layout()

# 4. Save the image in very high resolution for the paper
plt.savefig('final_plot_copilot.png', dpi=300)

# Display the plot on the screen
plt.show()