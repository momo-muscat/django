【uv】

## ● uvのインストール
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## ● 環境設定
```
$env:Path = "C:\Users\[ユーザー名]\.local\bin;$env:Path"
$env:Path = "C:\Users\doi\.local\bin;$env:Path"
```

## ● uvがインストールされたかどうかを確認
```
uv --version
```

## ● VSCodeを開きプロジェクトトップにディレクトリ移動

## ● 依存関係管理ファイル、仮想環境構築
```
uv init
uv venv
```


# 【Django】
## ● Djangoをインストール
```
uv add django
```

## ●Djangoプロジェクトの作成
（プロジェクトフォルダを二重構造にしたくない場合は、最後にピリオドを付ける）
```
uv run django-admin startproject [プロジェクト名] .
```

## ● 作成されたファイルの確認
```
tree /f

プロジェクト名           # プロジェクトのルートディレクトリ
├─ .venv               #
├─ .gitignore          #
├─ .python-version     #
├─ main.py             # 不要
├─ pyproject.toml      #
├─ uv.lock             #
├─ README.md           # このファイル
├─ manage.py           # 管理コマンド実行用スクリプト
├─ プロジェクト名      # プロジェクト共通設定（'config'等に名前を変える）
│   ├─ __init__.py    # Pythonパッケージとして認識させるファイル
│   ├─settings.py     # プロジェクトの設定ファイル
│   ├─urls.py         # URLディスパッチの定義
│   ├─admin.py        # 新規追加
│   ├─asgi.py         # 非同期サーバ用の設定
│   └─wsgi.py         # 本番サーバ用の設定
├─ apps                # 新規追加
├─ models              # 新規追加
├─ migrations          # 新規追加
├─ templates           # 新規追加
└─ static              # 新規追加
```

## ● 開発サーバ起動
```
uv run python manage.py runserver
http://127.0.0.1:8000/
```

## ● VSCodeでプロジェクトを開く
1.  VSCodeを起動
1. 「ファイル」→「フォルダーを開く」
1.  プロジェクトのルートディレクトリを選択
1. 「Ctrl + Shift + P」を押してコマンドパレットを開く
1. 「Python: Select Interpreter」と入力してインタプリタのパスを選択

## ● 以下の共通フォルダを生成
-apps       # アプリケーション
-models     # モデル
-migrations # マイグレーション
-templates  # テンプレート
-static     # 静的ファイル
※ apps、models、migrationsフォルダに/__init__.pyファイルを作成

## ● settings.pyで言語・タイムゾーンの設定変更
```
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
```

## ● settings.pyでtemplateフォルダの設定
```
TEMPLATES = [  
    {  
        ....,  
        'DIRS': [BASE_DIR / "templates"],  
        ....,  
    },  
]
```

## ● settings.pyでstaticフォルダの設定
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

```

## ● アプリケーションの作成
```
uv run python manage.py startapp [アプリ名] [アプリフォルダ]/[アプリ名]
```

## ● アプリケーションの登録
1. apps/[アプリ名]/apps.py の name を修正
```
name = 'apps.[アプリ名]'
```
2. setteings.pyのINSTALLED_APPSに追加
```
'apps.[アプリ名].apps.[アプリ名_PascalCase]Config'
```

## ● urls.pyでURLの登録
```
from django.urls import path, include
urlpatterns = [
    ...,
    path('app名/', include('[app名].urls')),
]
```

## ● [アプリ名]フォルダ内にurls.pyを作成
```
from django.urls import path
 
urlpatterns = [
  
]
```

## ● templateフォルダの作成
```
[templates]フォルダ > [アプリ名]フォルダ
```

## ● psycopg2インストール
```
uv add psycopg2
```

## ● setteings.pyでDB接続設定（PostgreSQL）
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name',                  # PostgreSQLデータベース名
        'USER': 'user',                  # データベースユーザ名
        'PASSWORD': 'password',          # データベースパスワード
        'HOST': 'localhost',             # データベースホスト（IPアドレスまたはホスト名）
        'PORT': '5432',                  # データベースポート（デフォルトは5432）
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
        'TIME_ZONE': 'Asia/Tokyo',       # 日本時間の場合
        'USE_TZ': True,                  # タイムゾーンを有効にする
    }
}
```

## ● データベースの設計図を作成
```
uv run python manage.py makemigrations
```

## ● データベースに反映
```
uv run python manage.py migrate
```

## ● 管理者ユーザーの作成
```
uv run python manage.py createsuperuser
user:
e-mail:
password:
```

## ● migrateをやり直す
1. 過去のmigrate履歴を確認  
uv run python manage.py showmigrations
1. テーブルを全て削除
1. appのmigrationsフォルダの中身を削除
1. migrate履歴の削除  
uv run python manage.py migrate --fake [アプリ名] zero
1. 履歴が削除されたかを1と同様のコマンドで確認
1. 通常の手順でmigrateをやり直す


# 【Git / GitHub】
## ● 新規作成時
```
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/momo-muscat/django_study.git
git push -u origin main
```

## ● 更新時
```
git remote add origin https://github.com/momo-muscat/django_study.git
git branch -M main
git push -u origin main
```

