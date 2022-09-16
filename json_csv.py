import pandas as pd

# enter the json filename to be converted to json
JSON_FILE = 'json_filename.json'

# enter the csv filename you wish to save it as
CSV_FILE = 'csv_filename.csv'

def json_csv(JSON_FILE, CSV_FILE):
    with open(JSON_FILE, encoding = 'utf-8') as f :
        df = pd.read_json(f)
        
    df.to_csv(CSV_FILE, encoding = 'utf-8', index = False)