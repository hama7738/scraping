import pandas as pd
import requests
import json
import argparse
from datetime import datetime as dt

def create_url(id):
    # url =  'https://itunes.apple.com/lookup?id='
    url =  "http://itunes.apple.com/jp/rss/customerreviews/id=" + str(id) +"/json"
    return url

def extract_data(url):
    r = requests.get(url=url)
    req_text = r._content.decode("utf-8")
    json_obj = json.loads(req_text)
    ## print(json_obj['resultCount'])
    return json_obj['feed']
    ## return json_obj['results']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--output_path")

    args = parser.parse_args()
    id = args.id
    output_path = args.output_path

    url =  create_url(id=id)
    data = extract_data(url)
    entry = data['entry']
    df = pd.DataFrame([x['content']['label'] for x in entry], columns=["feedback"])
    if output_path:
        df.to_csv(output_path +  "app-feedback" + dt.now().strftime("%Y-%d") + ".csv")
    else:
        print(df.head())
