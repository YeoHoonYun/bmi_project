# 어던 떼이터를 어떤 형태로 데이터 베이스에 저장할 것이냐?
# model에서는 데이터를 저장, 확인, 수정, 삭제하는 액션들을 만들지 X 자동으로 생성된다.
# 이미 models.Model이 ORM 기능을 다가지고 있다.
# ORM : 실제 데이터를 추상화 해놓고 사용한다.
# makemigrations bmi : 변경 사항을 추적해서 반영할 내용을 migration파일로 만들어 둔다.
# migrate bmi 0001 : migration 파일을 실제 DB에 반영한다.

from django.db import models

# Create your models here.

class BMI(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi_score = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "키 : " + str(self.height) + " 체중 : " + str(self.weight) + " BMI : " + str(self.bmi_score)

    # 저장 되기 직전에 사용하고 싶을 때
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.bmi_score = self.weight / ((self.height/100)**2)

        super(BMI, self).save(force_insert, force_update, using, update_fields)