import pandas as pd

race_result_df = pd.read_csv('../f1_data_csv/f1db-races-race-results.csv')
print(race_result_df.count())