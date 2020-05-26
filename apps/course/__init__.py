# user/__init__.py
default_app_config = 'course.apps.CourseConfig'
import pymysql
pymysql.install_as_MySQLdb()