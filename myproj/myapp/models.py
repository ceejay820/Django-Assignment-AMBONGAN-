from django.db import migrations, models

class my_tb(models.Model):
    attribute_1 = models.TextField(max_length=200)

    def __str__(self):
        return self.attribute_1
    