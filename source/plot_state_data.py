import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Read GeoJSON
us_states = gpd.read_file("https://raw.githubusercontent.com/PublicaMundi/MappingAPI/refs/heads/master/data/geojson/us-states.json")

# Read Excel file (with 'State' and 'Sample Value' columns)
sample_data = pd.read_excel("data/sample_state_data.xlsx")

# Merge: align 'State' from sample_data with 'name' from us_states
merged = us_states.merge(sample_data, left_on='name', right_on='State')

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
divider = make_axes_locatable(ax)

# Create a new axis on the right for the colorbar
cax = divider.append_axes("right", size="3%", pad=0.1)

# Plot the data and get the matplotlib collection
plot = merged.plot(column='Sample Value', cmap='plasma', ax=ax, legend=False)

# Add a colorbar that spans the height of the map
sm = plt.cm.ScalarMappable(cmap='plasma', norm=plt.Normalize(vmin=merged['Sample Value'].min(), vmax=merged['Sample Value'].max()))
cbar = fig.colorbar(sm, cax=cax)

# Remove axis ticks
ax.set_axis_off()

# Save figures
plt.savefig("plots/sample_state_data_map.pdf", bbox_inches='tight')
plt.savefig("plots/sample_state_data_map.png", dpi=300, bbox_inches='tight')
plt.show()

