from flask import Flask, Blueprint
from 급뭐.settings import SettingManager
from .db import DBManager

app = Flask(__name__)

conf = SettingManager().setting
db_engine = conf.get("Envrn").get("DB_Engine")

conf = conf.get("Server")
db_conf = conf.get(db_engine)
web_conf = conf.get("Web")

DB = DBManager(db_conf)