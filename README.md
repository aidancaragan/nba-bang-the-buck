# NBA "Bang for the Buck" Roster Valuation Model

## Project Overview
This project evaluates the financial efficiency of NBA player production by analyzing the relationship between on-court impact and contract size. While basic box scores show volume, modern front offices hunt for cost-controlled, high-impact assets to maximize roster building under the restrictive NBA salary cap. 

This model blends traditional per-game volume statistics with advanced impact metrics to calculate a **Win Shares per Million Dollars** efficiency rating.

## The Toolset & Architecture
* **Development Environment:** Visual Studio Code
* **Language:** Python 3.14
* **Data Toolkit:** Pandas (for data wrangling, cleaning, and relational database merging)
* **Version Control:** Git & GitHub

## Data Pipeline & Cleaning Methodology
Real-world sports data is notoriously fragmented and messy. This project builds a localized data pipeline that automates the following steps:
1. **Multi-Source Ingestion:** Loads three separate datasets containing standard box score statistics (`per_game_stats.csv`), contract structures (`salaries.csv`), and advanced impact metrics (`advanced percentages.csv`).
2. **Text Sanitation:** Strips non-numeric characters (dollar signs, commas, hidden whitespace) from financial data and handles player name encoding exceptions caused by international diacritics (e.g., accents).
3. **Relational Merging:** Chained merges combine the datasets seamlessly on unique player identifiers.
4. **Context Filters:** Establishes data thresholds (minimum 40 games played and 15+ minutes per game) to eliminate statistical noise from small sample sizes.

## Analytical Methodology
Instead of relying on arbitrary fan formulas, this model leverages **Win Shares ($WS$)**—a metric estimating the total number of wins a player contributes to his team based on offensive and defensive efficiency.

$$\text{WS per Million} = \left( \frac{\text{Total Win Shares}}{\text{Seasonal Salary}} \right) \times 1,000,000$$

## Key Insights & Roster Construction Takeaways
* **The "Rookie-Scale" Dominance:** Second-round picks and converted two-way players out-perform the entire league on absolute efficiency scales. Because the Collective Bargaining Agreement (CBA) limits their salaries to minimum tiers, any rotation-level output (e.g., Kobe Sanders) drastically inflates their financial efficiency rating.
* **Front Office Application:** Identifying these specific high-value, low-cost assets is critical for front offices looking to maximize flexibility around maximum-contract stars.

## How To Run
1. Clone the repository to your local machine.
2. Install dependencies: `pip install pandas`
3. Run the primary script: `python bankforbuck.py`
