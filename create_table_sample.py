from peewee import *

# 建立 sample.db
db = SqliteDatabase('sample.db')


# 定義一個基礎類別，指定這個ORM所使用的資料庫
# 這樣就不用重複宣告
class BaseModel(Model):
    class Meta:
        database = db

# 定義 Course 這張表
class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null = False)
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
        # 資料庫表名
        db_table = 'course'

# 定義 Teacher 這張表
class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null = False)
    gender = IntegerField()
    address = CharField()
    # 這邊是為了之後要輸出，所以關聯才改成 teachers
    course_id = ForeignKeyField(Course, to_field = "id", related_name = "teachers")

    class Meta:
        order_by = ('name',)
        db_table = 'teacher'

# 這裡只要建立一次
Course.create_table()
Teacher.create_table()