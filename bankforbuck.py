import pandas as pd

# 1. Load all THREE CSV files into DataFrames
stats_df = pd.read_csv('per_game_stats.csv', encoding='latin-1')
salaries_df = pd.read_csv('salaries.csv', encoding='latin-1', skiprows=1)
advanced_df = pd.read_csv('advanced percentages.csv', encoding='latin-1')

# 2. CLEAN messy text out of the salary column so Python can do math
salaries_df['2025-26'] = salaries_df['2025-26'].astype(str).str.strip()
salaries_df['2025-26'] = salaries_df['2025-26'].str.replace(
    '$', '', regex=False)
salaries_df['2025-26'] = salaries_df['2025-26'].str.replace(
    ',', '', regex=False)
salaries_df['2025-26'] = pd.to_numeric(salaries_df['2025-26'], errors='coerce')

# 3. Select only the Player name and Advanced Metrics to keep the data clean
# This avoids column name clutter when we merge them
advanced_sub = advanced_df[['Player', 'WS', 'BPM']]

# 4. Merge all three datasets together on the Player's name
merged_df = pd.merge(stats_df, salaries_df, on='Player')
merged_df = pd.merge(merged_df, advanced_sub, on='Player')

# 5. Filter out low-minute/low-game players to avoid statistical anomalies
filtered_df = merged_df[(merged_df['G'] > 40) & (merged_df['MP'] > 15)].copy()

# 6. Drop any rows where salary data is missing or zero
filtered_df = filtered_df[filtered_df['2025-26'] > 0]

# 7. NEW ADVANCED METRIC: Win Shares per Million Dollars
# Win Shares (WS) estimates the total number of wins a player contributed to his team.
filtered_df['WS_per_Million'] = (
    filtered_df['WS'] / filtered_df['2025-26']) * 1000000

# 8. Sort from highest advanced value index to lowest
value_leaders = filtered_df.sort_values(by='WS_per_Million', ascending=False)

# CLEAN FORMATTING FOR DISPLAY
value_leaders['2025-26'] = value_leaders['2025-26'].fillna(
    0).astype(int).map('${:,.0f}'.format)
value_leaders['WS_per_Million'] = value_leaders['WS_per_Million'].round(2)

# 9. Print the top 10 advanced value players to your terminal
print("\n--- TOP 10 \"BANG FOR THE BUCK\" PLAYERS IN THE NBA (WIN SHARES PER MILLION) ---")
print(value_leaders[['Player', 'Tm', '2025-26',
      'WS', 'WS_per_Million']].head(10))
