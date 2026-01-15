from database.DB_connect import DBConnect
from model.album import Album
from model.track import Track
from model.playlist import Playlist

class DAO:

    """

        Implementare tutte le funzioni necessarie a interrogare il database.

        """

    def __init__(self):

        pass



    @staticmethod

    def readAlbum(durata):

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)



        query = """
           SELECT 
        t.album_id,
        a.title,
        SUM(t.milliseconds) / (1000 * 60) AS minuti_totali
        FROM track t, album a 
        where a.id = t.album_id 
        GROUP BY t.album_id
        HAVING minuti_totali > %s;

        """



        cursor.execute(query, (durata,))

        for row in cursor:

            result.append(Album(row['album_id'], row['title'], row["minuti_totali"]))



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

    @staticmethod

    def readPlaylist():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)



        query = """
            SELECT *
            FROM playlist
        """



        cursor.execute(query)

        for row in cursor:

            result.append(Playlist(row['playlist_id'], row['track_id']))



        cursor.close()

        conn.close()

        return result