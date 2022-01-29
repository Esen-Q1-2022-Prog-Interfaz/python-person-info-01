from msilib import schema
import pymysql.cursors


def createConnectionToDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="personinfodb",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def createNewPersonCard(name, age, salary):
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `personinfodb`.`personinfo`(`id`,`name`,`age`,`salary`) VALUES(0,%s,%s,%s);"
            data = (name, age, salary)
            cursor.execute(sql, data)
        connection.commit()


def getPersonById(id) -> dict:
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM personinfodb.personinfo where id=%s;"
            data = (id,)
            cursor.execute(sql, data)
            result = cursor.fetchone()
            return result


def getAllPersonCards() -> list:
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM personinfodb.personinfo;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


def updatePersonCard(id, name, age, salary):
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `personinfodb`.`personinfo` SET `name` = %s, `age` = %s, `salary` = %s WHERE `id` = %s;"
            data = (name, age, salary, id)
            cursor.execute(sql, data)
        connection.commit()


def deletePersonCard(id):
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `personinfodb`.`personinfo` WHERE id=%s;"
            data = (id,)
            cursor.execute(sql, data)
        connection.commit()
