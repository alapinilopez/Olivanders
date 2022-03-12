from uri import db_uri
from mongoengine import connect
import certifi

def db_connect():
    ca = certifi.where()
    connection = connect(host=DB_URI, tlsCAFile=ca)
    return connection["olivanders"]["olivanderspy"]