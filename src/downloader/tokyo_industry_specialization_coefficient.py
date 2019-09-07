import urllib3
import json
import requests
import pandas as pd
import argparse
import datetime as dt
import ssl


def create_url(cityCode):
    url = "https://opendata.resas-portal.go.jp/"
    url += "api/v1/industry/power/forIndustry?cityCode=" + str(cityCode) + "&year=2012&prefCode=13&sicCode=-"
    return url

def extract_data(url, api_key):
    r = requests.get(url=url, headers={'X-API-KEY' :api_key,'Content-Type':'application/json'})
    req_text = r._content.decode("utf-8")
    json_obj= json.loads(req_text)
    return json_obj


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key")
    parser.add_argument("--cityCode")
    parser.add_argument("--output_path")

    args = parser.parse_args()
    api_key = args.api_key
    cityCode = args.cityCode
    output_path = args.output_path

    url = create_url(cityCode=cityCode)
    json_obj = extract_data(url=url, api_key=api_key)
    df = pd.DataFrame(json_obj['result']['data'])
    df['prefCode'] = json_obj['result']['prefCode']
    df['prefName'] = json_obj['result']['prefName']
    df['cityCode'] = str(cityCode)
    df.to_csv(output_path +"tokyo-industry-2012-data-prefCode" + str(cityCode) + ".csv")
