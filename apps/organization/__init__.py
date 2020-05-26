# user/__init__.py

default_app_config = 'organization.apps.OrganizationConfig'

import pymysql
pymysql.install_as_MySQLdb()