import matplotlib.pyplot as plt

# Data
routes = ['Inverness to Edinburgh', 'Edinburgh to Glasgow', 'London to Birmingham', 'London to Carfiff', 'London to Manchester']
values = [3, 20, 10, 9, 20]

# Sorting 
sorted_data = sorted(zip(routes, values), key=lambda x: x[1], reverse=True)
sorted_routes, sorted_values = zip(*sorted_data)

# Color
blue_color = '#C3AF97'

# Font sans-serif
plt.rcParams['font.family'] = 'sans-serif'

# Creating vizualisation
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_routes, sorted_values, color=blue_color)

# Title and lables
plt.title('Transportation Density during 24 hours', fontsize=16, weight='bold')
plt.xlabel('Routes', fontsize=12, weight='bold')
plt.ylabel('Density', fontsize=12, weight='bold')

# Values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')

# Offsets
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.ylim(0, max(sorted_values) + 5)



# Show visualization
plt.show()

