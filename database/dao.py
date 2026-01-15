from database.DB_connect import DBConnect
from model.album import Album
from model.track import Track

class DAO:

    """

        Implementare tutte le funzioni necessarie a interrogare il database.

        """

    def __init__(self):

        pass



    @staticmethod

    def readAlbum():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)



        query = """
            SELECT *
            FROM album
        """



        cursor.execute(query)

        for row in cursor:

            result.append(Album(row['id'], row['title'], row["artist_id"]))



        cursor.close()

        conn.close()

        return result

    @staticmethod
    def read_playlist_track() -> list | None:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT *
                    FROM playlist_track pt 
                        """  #
        try:
            cursor.execute(query)
            for row in cursor:
                result.append({
                    "track_id": row["track_id"],
                    "playlist_id": row["playlist_id"]
                })

        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result



    @staticmethod

    def readTrack():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)



        query = """
            SELECT id, album_id , (milliseconds/(1000*60)) as minuti
            FROM track

        """



        cursor.execute(query)

        for row in cursor:

            result.append(Track(row['id'], row['album_id'], row["minuti"]))



        cursor.close()

        conn.close()

        return result