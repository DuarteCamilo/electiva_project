# settings.py
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = {
    "name": os.getenv("MYSQL_DATABASE"),
    "engine": "peewee.MySQLDatabase",  # MySQL como motor de base de datos
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT")),
}
