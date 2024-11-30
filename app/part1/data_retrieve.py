import os
import pandas as pd
import subprocess
import glob
from sqlalchemy import create_engine
from datetime import datetime

os.environ["KAGGLE_CONFIG_DIR"] = os.path.expanduser("~/.kaggle/")

#Download the dataset
dataset = "yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018"

# Execute the Kaggle download command
subprocess.run(
    ["kaggle", "datasets", "download", "-d", dataset, "--unzip"], 
    check=True
)

csv_files = glob.glob("*.csv")
for file in csv_files:
    print(f"Processing {file}")
    df = pd.read_csv(file)
    current_time = datetime.now()
    df["created_at"] = current_time.strftime("%Y-%m-%d %H:%M:%S")

    db_name = "airline_delays.db"  # SQLite database file
    engine = create_engine(f"sqlite:///{db_name}")

    table_name = "airline_delays"
    df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data has been saved to the SQLite database '{db_name}' in table '{table_name}'.")
