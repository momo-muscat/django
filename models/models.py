from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# 切り分けテーブル
class KiriTbl(models.Model):

    denno = models.CharField(verbose_name="親伝票番号", db_column="親伝票番号", max_length=14)
    s_denno = models.CharField(verbose_name="子伝票番号", db_column="子伝票番号", max_length=14, primary_key=True)
    ins_at = models.DateTimeField(auto_now_add=True)
    upd_at = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.s_denno
    
    class Meta:
        db_table = "kiri_tble"
        verbose_name = "切り分けテーブル"
        verbose_name_plural = "切り分けテーブル"

# 配送情報テーブル
class HaiinfoTbl(models.Model):

    denno = models.CharField(verbose_name="伝票番号", db_column="伝票番号", max_length=14, primary_key=True)
    den_type = models.CharField(verbose_name="伝票タイプ", db_column="伝票タイプ", max_length=1)
    ins_at = models.DateTimeField(auto_now_add=True)
    upd_at = models.DateTimeField(auto_now=True, editable=True)
    order_date = models.DateTimeField(null=True, verbose_name="注文日時", db_column="注文日時")

    def __str__(self):
        return self.denno
    
    class Meta:
        db_table = "haiinfo_tbl"
        verbose_name = "配送情報テーブル"
        verbose_name_plural = "配送情報テーブル"


# 整数テスト
class IntTest(models.Model):

    int1 = models.PositiveIntegerField(verbose_name="null=False, blank=False")
    int2 = models.PositiveIntegerField(verbose_name="null=False, blank=True", blank=True)
    int3 = models.PositiveIntegerField(verbose_name="null=True, blank=False", null=True)
    int4 = models.PositiveIntegerField(verbose_name="null=True, blank=True", null=True, blank=True)

    class Meta:
        db_table = "int_test"
        verbose_name = "整数型テスト"
        verbose_name_plural = "整数型テスト"

# 文字列テスト
class CharTest(models.Model):

    char1 = models.PositiveIntegerField(verbose_name="null=False, blank=False")
    char2 = models.PositiveIntegerField(verbose_name="null=False, blank=True", blank=True)
    char3 = models.PositiveIntegerField(verbose_name="null=True, blank=False", null=True)
    char4 = models.PositiveIntegerField(verbose_name="null=True, blank=True", null=True, blank=True)

    class Meta:
        db_table = "char_test"
        verbose_name = "文字列テスト"
        verbose_name_plural = "文字列テスト"

# 日付テスト
class DateTest(models.Model):

    date1 = models.DateTimeField(verbose_name="null=False, blank=False")
    date2 = models.DateTimeField(verbose_name="null=False, blank=True", blank=True)
    date3 = models.DateTimeField(verbose_name="null=True, blank=False", null=True)
    date4 = models.DateTimeField(verbose_name="null=True, blank=True", null=True, blank=True)

    class Meta:
        db_table = "date_test"
        verbose_name = "日付テスト"
        verbose_name_plural = "日付テスト"


# フィールドテスト
class FieldTest(models.Model):

    int1 = models.PositiveIntegerField(
        verbose_name="PositiveInteger1", db_column="PositiveInteger1",
        null=False, blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(9999)],
        )
    int2 = models.PositiveIntegerField(
        verbose_name="PositiveInteger2", db_column="PositiveInteger2",
        null=False, blank=False,
        default=0, db_default=0,
        validators=[MinValueValidator(0), MaxValueValidator(9999)],
        )
    
    char1 = models.CharField(
        verbose_name="Char1", db_column="Char1",
        null=False, blank=False,
        max_length=4,
        )
    char2 = models.CharField(
        verbose_name="Char2", db_column="Char2",
        null=False, blank=True,
        max_length=4,
        )
    char3 = models.CharField(
        verbose_name="Char3", db_column="Char3",
        null=False, blank=True,
        default="", db_default="",
        max_length=4,
        )
    
    date1 = models.DateTimeField(
        verbose_name="DateTime1", db_column="DateTime1",
        null=False, blank=False,
        )
    date2 = models.DateTimeField(
        verbose_name="DateTime2", db_column="DateTime2",
        null=True, blank=True,
        )

    # def __str__(self):
    #     return ""

    class Meta:
        db_table = "field_test"
        verbose_name = "フィールドテスト"
        verbose_name_plural = "フィールドテスト"


# 名称マスタ
class NameMst(models.Model):
    cd = models.PositiveIntegerField(verbose_name="コード", db_column="コード", primary_key=True,
            default=0, db_default=0, validators=[MinValueValidator(0), MaxValueValidator(9999)])
    nm = models.CharField(verbose_name="名称", db_column="名称", max_length=10, blank=True)
    digit = models.PositiveIntegerField(verbose_name="表示桁数", db_column="表示桁数", default=0, db_default=0)
    sort = models.PositiveIntegerField(verbose_name="表示順", db_column="表示順", default=0, db_default=0,
            validators=[MinValueValidator(0), MaxValueValidator(99)])
    memo = models.TextField(verbose_name="備考", db_column="備考", blank=True, default="", db_default="")
    ins_at = models.DateTimeField(auto_now_add=True)
    upd_at = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.nm
    
    class Meta:
        db_table = "name_mst"
        verbose_name = "名称マスタ"
        verbose_name_plural = "名称マスタ"

