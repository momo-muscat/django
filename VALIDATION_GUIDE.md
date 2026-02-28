# バリデーション資料（概要・目的・方法）

## 1. バリデーションとは（概要）
バリデーション（Validation）とは、**入力データや状態が、アプリケーションのルールを満たしているかを検証する処理**です。

Django開発では、主に次のレイヤーで実施します。

- **クライアント側**: HTML属性やJavaScriptによる入力チェック（UX向上が目的）
- **サーバ側（Django）**: Form/Model/Serializerでの検証（信頼できる本命の検証）
- **DB側**: `UNIQUE`、`CHECK`、`NOT NULL` などの制約（最終防衛ライン）

> 重要: クライアント側だけでは不十分です。必ずサーバ側・DB側でも検証します。

---

## 2. バリデーションの目的

### 2.1 不正データの防止
- 想定外の値（空文字、範囲外、型不一致など）を保存しない
- システムの整合性を保つ

### 2.2 セキュリティ向上
- 悪意ある入力や異常なリクエストを受けても、危険なデータを通さない
- 業務ロジック上の抜け道を減らす

### 2.3 ユーザー体験（UX）向上
- 入力ミスを早期に具体的に通知する
- 「何がダメか」「どう直すか」を明確に伝える

### 2.4 保守性・品質向上
- ルールをコードとして明示できる
- テストしやすく、将来の仕様変更にも対応しやすい

---

## 3. バリデーションの基本方針

1. **早く・複数層で検証する（Defense in Depth）**
2. **エラーメッセージは利用者に分かりやすくする**
3. **ルールは1か所に集約し重複を減らす**
4. **DB制約を必ず併用する**
5. **正常系/異常系をテストで担保する**

---

## 4. Djangoでの主なバリデーション方法

### 4.1 Modelフィールドのバリデータ
フィールド定義時に、長さ・最小値・正規表現などを設定します。

```python
from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(0)])
```

#### 向いている用途
- 単一フィールドのルール
- 再利用される基本ルール

---

### 4.2 `clean_<field>()`（Form）
フォーム上で特定フィールドを個別検証します。

```python
from django import forms

class UserForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        value = self.cleaned_data["email"]
        if value.endswith("@example.com"):
            raise forms.ValidationError("このドメインは利用できません。")
        return value
```

#### 向いている用途
- 画面入力に近い粒度での検証
- UIと密接な入力ルール

---

### 4.3 `clean()`（Form/Model）
複数フィールドをまたぐ整合性チェックに使います。

```python
from django.core.exceptions import ValidationError
from django.db import models

class Reservation(models.Model):
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def clean(self):
        if self.start_at and self.end_at and self.start_at >= self.end_at:
            raise ValidationError("終了日時は開始日時より後にしてください。")
```

#### 向いている用途
- 相関ルール（開始 < 終了 など）
- 業務ルールの整合性検証

---

### 4.4 `full_clean()`
Modelインスタンスに対して、フィールド検証 + `clean()` + 一意性検証をまとめて実行します。

```python
obj = Reservation(start_at=..., end_at=...)
obj.full_clean()  # ValidationErrorが発生する可能性あり
obj.save()
```

#### 注意点
- `save()` はデフォルトで `full_clean()` を自動実行しません。
- 必要に応じて、保存前に明示的に呼び出します。

---

### 4.5 ModelForm
Model由来の検証をフォーム処理に自然に統合できます。

- `is_valid()` 実行時に、フォームとモデル双方のルールを考慮
- 管理画面や通常フォームで特に有効

---

### 4.6 Django REST Framework（使用時）
API入力にはSerializerの検証を使います。

- `validate_<field>()`: 単一フィールド
- `validate(self, attrs)`: 複合検証
- `UniqueValidator`: 一意性検証

---

### 4.7 DB制約（必須）
アプリ層のチェックをすり抜けても、DB側で不正データを防ぎます。

例:
- `unique=True`
- `null=False`
- `CheckConstraint`
- 複合一意制約（`UniqueConstraint`）

---

## 5. どこで何を検証するか（実務の目安）

- **クライアント**: 必須入力、形式補助（即時フィードバック）
- **Form/Serializer**: リクエスト単位の妥当性チェック
- **Model**: ドメインルール（アプリ内で共通化したいルール）
- **DB**: 一意性・整合性の最終保証

---

## 6. よくある失敗と対策

- **失敗1**: クライアント側だけで満足してしまう
  - **対策**: サーバ側とDB側で必ず再検証

- **失敗2**: ルールがフォーム・ビュー・モデルに重複
  - **対策**: コアとなる業務ルールをModel/共通関数に寄せる

- **失敗3**: エラーメッセージが曖昧
  - **対策**: 「原因」と「修正方法」を短く明示

- **失敗4**: バリデーション未テスト
  - **対策**: 異常系テスト（境界値、重複、欠損）を追加

---

## 7. テスト観点（最低限）

- 正常系: 妥当な入力で保存/登録できる
- 異常系: 必須漏れ、型不正、範囲外、重複でエラーになる
- 境界値: 最小値、最大値、文字数上限ちょうど
- 相関チェック: フィールド間ルール違反でエラーになる

---

## 8. まとめ

- バリデーションは「**品質・安全性・整合性**」を守る要です。
- Djangoでは、**Form/Model/Serializer + DB制約**を組み合わせるのが実践的です。
- 単一フィールドはフィールド定義、複合条件は`clean()`、最終保証はDB制約、という役割分担を明確にすると保守しやすくなります。