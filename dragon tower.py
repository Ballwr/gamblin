import random

# Initialize the grid with all zeros
grid = [[0 for _ in range(3)] for _ in range(9)]

# Run the simulation 100,000 times
for _ in range(100000):
    floor = 0
    while floor < 9:
        option = random.randint(0, 2)
        if random.random() < 2/3:  # 2/3 chance of egg
            grid[floor][option] += 1  # increment egg count
        else:  # 1/3 chance of death
            break
        floor += 1



# Calculate the percentage of eggs on each floor
for i, floor in enumerate(grid):
    total = sum(floor)
    egg_percentage = [f"{(x/total)*100:.2f}%" for x in floor]
    print(f"Floor {i+1}: {', '.join(egg_percentage)}")