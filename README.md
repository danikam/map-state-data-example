# Map State Data Example

This repository provides an example of how to visualize **state-level data** on a map of the United States using **GeoPandas** and **Matplotlib**. It demonstrates how to:
- Load **geospatial data** for US states (in GeoJSON format).
- Merge this with **custom data** from an Excel file.
- Plot the merged data with a **color-coded map** and an adjustable **colorbar**.
- Save the resulting map in both **PDF** and **PNG** formats.

## Sample Data

The `data/sample_state_data.xlsx` file contains:
- **State**: Name of each US state (matches GeoJSON).
- **Sample Value**: Example numeric data for visualization.

Feel free to modify or replace `Sample Value` with your own dataset!

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/danikam/map-state-data-example.git
cd map-state-data-example

## Install dependencies

```bash
pip install geopandas matplotlib pandas openpyxl
```

## Execution

From the top level of the repo:

```bash
python source/plot_state_data.py
```
