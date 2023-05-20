# Djangoのsettingsモジュールから設定をインポート
from django.conf import settings
# DjangoのmodelsモジュールからModelクラスをインポート
from django.db import models
# Djangoのutilsモジュールからtimezone関数をインポート
from django.utils import timezone


# Modelクラスを継承したPostクラスを定義
class Post(models.Model):
    # ForeignKeyフィールドを定義して、設定からAUTH_USER_MODELを参照して、
    # UserモデルとPostモデルを関連付ける
    # (on_delete = models.CASCADEにより、Userモデルが削除されたときに、Postモデルも削除される)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharFieldフィールドを定義して、最大長が200文字のタイトルを保存する
    title = models.CharField(max_length=200)
    # TextFieldフィールドを定義して、テキストを保存する
    text = models.TextField()
    # DateTimeFieldフィールドを定義して、デフォルト値として現在時刻を設定する
    created_date = models.DateTimeField(default=timezone.now)
    # DateTimeFieldフィールドを定義して、投稿された日時を保存する。初期値はnull。
    published_date = models.DateTimeField(blank=True, null=True)

    # 投稿を公開するためのメソッドを定義
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # モデルの文字列表現を定義するメソッドを定義
    def __str__(self):
        return self.title
