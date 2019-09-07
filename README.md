# scraping
スクレイピング用のコードを集めたレポジトリ

### tokyo_weather_scraping.py
東京の気象情報のデータのスクレイピング用のコード。 

実行コマンド : `python tokyo_weather_scraping.py --year 2019 --month 02 --output_path "path/to/output_file/"`


### tokyo_industry_specialization_coefficient.py
RESASの産業別特化係数(https://opendata.resas-portal.go.jp/docs/api/v1/industry/power/forIndustry.html)
を取得するためのスクレイピングコード。 

実行コマンド : `python tokyo_industry_specialization_coefficient.py --api_key your_resus_api_key --cityCode 13108 --output_path "path/to/output_file/"` 

### city_code_scraping.py 
市町村コードの取得のためのスクレイピングコード
実行コマンド : `python city_code_scraping.py --api_key your_resus_api_key --prefCode 13 --output_path "path/to/output_file/"`

### app_store_feedback.py
Apple Storeの評価のスクレイピング用のコード。 

実行コマンド : `python app_store_feedback.py --id your_app_id --output_path "path/to/output_file/"`

