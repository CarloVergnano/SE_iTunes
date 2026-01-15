from database.DB_connect import DBConnect
from model.album import Album
from model.connalbum import ConnAlbum
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

    def readConnAlbum():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)



        query = """
            SELECT DISTINCT
                    t1.album_id AS album1,
                    t2.album_id AS album2
                    FROM playlist_track pt1, playlist_track pt2, track t1, track t2
                    where pt1.playlist_id = pt2.playlist_id AND pt1.track_id = t1.id and pt2.track_id = t2.id 
                    and t1.album_id <> t2.album_id 

        """



        cursor.execute(query)

        for row in cursor:

            result.append(ConnAlbum( row['album1'], row["album2"]))



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