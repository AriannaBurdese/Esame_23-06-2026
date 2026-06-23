from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.user import User

class Dao:
    def __init__(self):
        pass

    """"@staticmethod
    def read_all_users():
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = SELECT * FROM Users 

        cursor.execute(query)

        for row in cursor:
            user = User(
                row["user_id"],
                row["votes_funny"],
                row["votes_useful"],
                row["votes_cool"],
                row["name"],
                row["average_stars"],
                row["review_count"]
            )

            results.append(user)

        cursor.close()
        cnx.close()

        return results"""

    @staticmethod
    def get_users(n_bus):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = ("""select u.*
                    from users u, reviews r 
                    where u.user_id = r.user_id 
                    group by u.user_id 
                    having COUNT( r.business_id) >= %s""")
        try:
            cursor.execute(query, (n_bus,))
            for row in cursor:
                user = User(**row)
                result.append(user)

        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_connessioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = ("""select distinct u1.user_id as user1, u2.user_id as user2, COUNT(distinct r1.business_id) as peso
                    from users u1, users u2, reviews r1, reviews r2
                    where u1.user_id = r1.user_id and u2.user_id = r2.user_id and u1.user_id < u2.user_id and r1.business_id = r2.business_id 
                    group by user1, user2 
                    having peso > 0""")
        try:
            cursor.execute(query)
            for row in cursor:
                connessione = Connessione(**row)
                result.append(connessione)

        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result


