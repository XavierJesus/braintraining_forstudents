import mysql.connector
import datetime
import csv

filename_activities = "activities.csv"

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                            user='root', password='Domingos50', database='projdbpy',
                                            buffered=True, autocommit=True)


def close_dbconnection():
    db_connection.close()


def add_activities(activities_name):
    query = "INSERT INTO activities (name) values (%s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (activities_name,))
    cursor.close()


def get_activity_id(activity_name):
    query = "SELECT id FROM activities WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (activity_name,))
    row = cursor.fetchone()
    cursor.close()
    return row[0]


def get_username_id(username_name):
    query = "SELECT id FROM users WHERE username = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (username_name,))
    row = cursor.fetchone()
    cursor.close()
    return row[0]


def add_results(nb_trials, nb_success, activity_id, user_id):
    query = "INSERT INTO results (nb_trials, nb_success, activity_id, user_id) values (%s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (nb_trials, nb_success, activity_id, user_id))
    cursor.close()


def delete_data():
    query = "SET FOREIGN_KEY_CHECKS = 0"
    query2 = "TRUNCATE table activities"
    query3 = "TRUNCATE table results"
    query4 = "TRUNCATE table users"
    query5 = "SET FOREIGN_KEY_CHECKS = 1"

    cursor = db_connection.cursor()
    cursor.execute(query)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    cursor.close()


def open_activities_fromcsv():
    with open(filename_activities, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=(";"))
        next(csvreader, None)
        for row in csvreader:
            add_activities(row[0])

open_dbconnection()
delete_data()
close_dbconnection()

open_dbconnection()
open_activities_fromcsv()
close_dbconnection()