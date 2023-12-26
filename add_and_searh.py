from create_table_sample import *
from peewee import *

Course.create(id = 1,
              title = "經濟學",
              period = 320,
              description = '都可以選修')
Course.create(id = 2,
              title = "大學英文",
              period = 300,
              description = '大一必修')
Course.create(id = 3,
              title = "哲學",
              period = 100,
              description = '選修')
Course.create(id = 104,
              title = "寫code",
              period = 100,
              description = '資工系必修')

Teacher.create(
    name = 'xia',
    gender = True,
    address = '...',
    course_id = 1
)

Teacher.create(
    name = 'abc',
    gender = True,
    address = '......',
    course_id = 3
)

Teacher.create(
    name = 'egg',
    gender = True,
    address = '..',
    course_id = 2
)

record = Course.get(Course.title == '大學英文')
# print("科目： %s 學習時長： %d" % (record.title, record.period))

record.period = 200
record.save()
# print("科目： %s 學習時長： %d" % (record.title, record.period))

record.delete_instance()

# courses = Course.select()

courses = Course.select().where(Course.id < 10).order_by(Course.period.desc())
# for course in courses:
#     print("科目 ID: %d, 標題: %s, 學習時長: %d, 描述: %s" % (course.id, course.title, course.period, course.description))


total = Course.select(fn.avg(Course.period).alias('avg_period'))
avg_period = total.scalar()
# print("平均學習時長： %f" % avg_period)

Course.update(period = 300).where(Course.id > 100).execute()

Record = Course.select().join(Teacher).where(Teacher.gender == True)

for record in Record:
    print("科目 ID: %d, 標題: %s, 學習時長: %d, 描述: %s" % (record.id, record.title, record.period, record.description))
    for teacher in record.teachers:
        print("教師名字: %s, 地址: %s" % (teacher.name, teacher.address))
    print("------")