import pandas as pd
import sqlite3

con = sqlite3.connect(r"C:\Work\Saurabh_Kansal\Upgrad\django\project_pharma\db.sqlite3")

# Load the data into a DataFrame
# surveys_df = pd.read_sql_query("SELECT * from auth_permission", con)

# Select only data for 2002
# product_start_end_df = pd.read_csv(r"C:\Work\Saurabh_Kansal\Upgrad\django\project_pharma\pharma\static\pharma\data\product_start_end.csv")
event_start_end_df = pd.read_csv(r"C:\Work\Saurabh_Kansal\Upgrad\django\project_pharma\pharma\static\pharma\data\event_start_end.csv")
# Write the new DataFrame to a new SQLite table
event_start_end_df.to_sql("event_start_end", con, if_exists="replace")

con.close()