import pymysql.cursors


def createConnectionToDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="personinfodb",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def createNewPersonCard():
    pass
