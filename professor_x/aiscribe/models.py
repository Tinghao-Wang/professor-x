from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)  # 例如，一個簡單的標題字段
    description = models.TextField()          # 一個文本描述字段
    created_at = models.DateTimeField(auto_now_add=True)  # 創建時間

    def __str__(self):
        return self.title
