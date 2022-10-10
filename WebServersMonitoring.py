import mysql.connector


class WebServersMonitoring:
    @staticmethod
    def create_tables():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Monolith',
                                                 user='root',
                                                 password='root')

            Create_requests_history_Query = """CREATE TABLE requests_history (
                                    name varchar(250) NOT NULL,
                                    success_status varchar(10) NOT NULL,
                                    time TIMESTAMP(6) NOT NULL,
                                     PRIMARY KEY (name,time)) """
            Create_web_servers_Query = """CREATE TABLE web_servers (
                                     name varchar(250) NOT NULL,
                                     HTTP_URL TEXT NOT NULL,
                                     health_status varchar(10),
                                     PRIMARY KEY (name)) """
            cursor = connection.cursor()
            cursor.execute(Create_requests_history_Query)
            cursor.execute(Create_web_servers_Query)

        except mysql.connector.Error as error:
            pass
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def __change(action, query, name=0):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Monolith',
                                                 user='root',
                                                 password='root')
            cursor = connection.cursor()
            cursor.execute(query)

            if action == "insert":
                connection.commit()

            elif action == "read":
                record = cursor.fetchone()
                cursor.execute(
                    f"""select success_status from requests_history where name = \'{name}\' order by time desc """)
                statuses = cursor.fetchall()[:10]
                statuses.insert(0, record)
                return statuses

            elif action == "update":
                connection.commit()
            elif action == "delete":
                connection.commit()
            elif action == "getAll":
                record = cursor.fetchall()
                return record
            elif action == "get":
                record = cursor.fetchall()
                return record
            elif action == "request":
                connection.commit()

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def create_webserver(name, url):
        mySql_insert_query = f"""INSERT INTO web_servers (Name, HTTP_URL,health_status)
                                               VALUES
                                               (\'{name}\',\'{url}\',NULL) """
        WebServersMonitoring.__change('insert', mySql_insert_query)

    @staticmethod
    def read_webserver(name):
        mySql_read_query = f"""select * from web_servers where name = \'{name}\'"""
        return WebServersMonitoring.__change('read', mySql_read_query, name)

    @staticmethod
    def update_webserver(old_name, new_name=None, new_url=None, new_health_status=None):
        update = ''
        coma = False
        if new_name:
            update += f"Name = \'{new_name}\'"
            coma = True
        if new_url:
            if coma:
                update += ','
            update += f"http_url = \'{new_url}\'"
        if new_health_status:
            if coma:
                update += ','
            update += f"health_status = \'{new_health_status}\'"

        mySql_update_query = f"""Update web_servers set {update} where Name = \'{old_name}\'"""
        WebServersMonitoring.__change('update', mySql_update_query)

    @staticmethod
    def delete_webserver(name):
        sql_Delete_query = f"""Delete from web_servers where name = \'{name}\'"""
        WebServersMonitoring.__change('delete', sql_Delete_query)
        sql_Delete_query = f"""Delete from requests_history where name = \'{name}\'"""
        WebServersMonitoring.__change('delete', sql_Delete_query)

    @staticmethod
    def get(name):
        mySql_get_query = f"""select success_status from requests_history where name = \'{name}\'"""
        return WebServersMonitoring.__change('get', mySql_get_query)

    @staticmethod
    def get_all():
        mySql_get_all_query = f"""select * from web_servers"""
        return WebServersMonitoring.__change('getAll', mySql_get_all_query)

    @staticmethod
    def request(name, status):
        mySql_request_query = f"""INSERT INTO requests_history (name, success_status,time)
                                                           VALUES
                                                           (\'{name}\',\'{status}\',NOW(6)) """
        WebServersMonitoring.__change('request', mySql_request_query)
