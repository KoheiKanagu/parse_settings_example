# 概要
pm2を使ってparse-serverとparse-dashboardをモニタリングする時のconfig例

詳細: [Parse Serverの死活管理と設定変更したらすぐ自動で反映されるようにする](http://qiita.com/KoheiKanagu/items/b02fed82ddad4ed51928)


# example

    /usr/local/bin/python3 -c "$(curl -fsSL https://raw.githubusercontent.com/KoheiKanagu/parse_settings_example/master/generator.py)" --mountPath "/your_mountPath" --port 1340 --publicServerURL "https://example.com/your_parse" --serverURL "https://example.com/your_parse" --databaseURI "mongodb://localhost:27017/your_db"