# myQiita

このリポジトリはQiita CLIを使って記事を管理するためのリポジトリです。

Qiita CLIについては以下のページを参照してください。

- [自分のエディタで記事投稿ができる、Qiita CLIの使い方 - Qiita](https://qiita.com/Qiita/items/666e190490d0af90a92b#qiita-cli%E3%81%A8%E3%81%AF)

## 記事の新規作成

```bash
npx qiita new [article file name]
```

記事を新しく作る際にはユニークとなるファイル名が必要になります。
その辺は機械的にやりたいのでPythonで日時からMD5ハッシュを作ることにしました。

```python
import hashlib
import datetime
import subprocess


def newid():
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    md5 = hashlib.md5(timestamp.encode('utf-8')).hexdigest()
    return md5


def main():
    id = newid()
    cmd = "npx qiita new %s" % id

    result = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.returncode)
    print(result.stdout)


if __name__ == "__main__":
    main()
```

実行すると次のようなFROMTMATTERが含まれるマークダウンが生成されます。
この場合は生成されたIDが`f60698f78b6b0468c60eddc1a5cfa1b4`なので、`f60698f78b6b0468c60eddc1a5cfa1b4.md`が生成されて`title`にもその値が埋められています。

```markdown
---
title: f60698f78b6b0468c60eddc1a5cfa1b4
tags:
  - ''
private: false
updated_at: ''
id: null
organization_url_name: null
slide: false
ignorePublish: false
---
# new article body
```

なお、実行環境は`Python 3.11.0`です。

```markdown
---
title: newArticle001 # 記事のタイトル
tags:
  - "" # タグ（ブロックスタイルで複数タグを追加できます）
private: false # true: 限定共有記事 / false: 公開記事
updated_at: "" # 記事を投稿した際に自動的に記事の更新日時に変わります
id: null # 記事を投稿した際に自動的に記事のUUIDに変わります
organization_url_name: null # 関連付けるOrganizationのURL名
slide: false # true: スライドモードON / false: スライドモードOFF
---
# new article body
```
