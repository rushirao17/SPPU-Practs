"""
Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem.
"""
# Map Coloring Problem

regions = ['delhi', 'chennai', 'mumbai', 'kolkata']
colors = ['red', 'green', 'blue', 'yellow']

neighbour = {
    'delhi': ['mumbai', 'chennai'],
    'chennai': ['mumbai', 'kolkata', 'delhi'],
    'mumbai': ['delhi', 'chennai', 'kolkata'],
    'kolkata': ['mumbai', 'chennai']
}

region_color = {}

def color_selection(region):
    available_colors = colors[:]
    for neighbor in neighbour[region]:
        if neighbor in region_color:
            neighbor_color = region_color[neighbor]
            if neighbor_color in available_colors:
                available_colors.remove(neighbor_color)
    if available_colors:
        return available_colors[0]
    else:
        return None

for region in regions:
    region_color[region] = color_selection(region)

print(region_color)

if None in region_color.values():
    print("Insufficient colors, please add more colors")
