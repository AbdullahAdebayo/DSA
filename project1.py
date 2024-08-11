import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Filter schools by average_math in descending order
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]]
best_math_schools = best_math_schools.sort_values("average_math", ascending=False)

print(best_math_schools)

# Calculate total SAT score
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Get top 10 schools by total SAT score
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False)
top_10_schools = top_10_schools.head(10)

print(top_10_schools)

# Calculate standard deviation, number of schools, and mean of total SAT by borough
borough_stats = schools.groupby("borough")["total_SAT"].agg(
    num_schools='size',
    average_SAT='mean',
    std_SAT='std'
).reset_index()

# Find the borough with the largest standard deviation
largest_std_dev = borough_stats.loc[borough_stats["std_SAT"].idxmax()].to_frame().T
largest_std_dev.round()

print(largest_std_dev)