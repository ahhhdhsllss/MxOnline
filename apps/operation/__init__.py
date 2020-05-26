# user/__init__.py

default_app_config = 'operation.apps.OperationConfig'
import pymysql
pymysql.install_as_MySQLdb()