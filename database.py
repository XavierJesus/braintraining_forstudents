import mysql.connector


def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                            user='root', password='Domingos50', database='projdbpy',
                                            buffered=True, autocommit=True)


def close_dbconnection():
    db_connection.close()


def get_activity_id(activity_name):
    query = "SELECT id FROM activities WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (activity_name,))
    row = cursor.fetchone()
    cursor.close()
    return row[0]


def add_results(nb_trials, nb_success, activity_id, user_id):
    query = "INSERT INTO results (nb_trials, nb_success, activity_id, user_id) values (%s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (nb_trials, nb_success, activity_id, user_id))
    cursor.close()
