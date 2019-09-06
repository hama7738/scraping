import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import datetime as dt

def create_url(year, month):
    url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=" + str(year) + "&month=" + str(month) + "&day=&view=p1"
    return url

def extract_data(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, "html.parser")
    rows = soup.findAll('tr',class_='mtx')
    row_data = [row.findAll('td') for row in rows][4:]
    table_data =  []
    for i in range(len(row_data)):
        text_data = ''
        for j in range(len(row_data[i])):
            text_data =  text_data + " " + row_data[i][j].text
        table_data.append(text_data)
    return table_data

def create_table(table_data):
    table = []
    table_key =  ["日", "現地平均気圧(hpa)", "海面平均気圧(hpa)", "降水量合計(mm)",
     "降水量最大1時間(mm)", "降水量最大10分間(mm)", "平均気温","最高気温","最低気温",
     "平均湿度(%)","最低湿度(%)","平均風速(m/s)","最大風速(m/s)","最大風速風向","最大瞬間風速(m/s)",
     "最大瞬間風速風向","日照時間(h)","降雪合計(cm)","最深積雪値(cm)", "天気概況昼(06:00~18:00)","天気概況夜(18:00~翌日06:00)"]

    for i in range(len(table_data)):
        row_dict = {}
        table_value = table_data[i].split()
        table_value = [v for v in table_value if v!=')']
        for j in range(len(table_value)):
            row_dict[table_key[j]] = table_value[j]
        table.append(row_dict)
    return table



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--year")
    parser.add_argument("--month")
    parser.add_argument("--output_path")
    args = parser.parse_args()
    year = args.year
    output_path = args.output_path
    month = args.month
    url = create_url(year,month)
    table_data = extract_data(url)
    table = create_table(table_data=table_data)
    df_table = pd.DataFrame(table)
    df_table.to_csv(output_path + "tenki-" + str(year) + str(month) + ".csv")
