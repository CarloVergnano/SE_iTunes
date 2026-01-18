
from model.album import Album
from database.DB_connect import DBConnect
from model.connessioni import Connessione


class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_album(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select a.id, a.title, sum(t.milliseconds/(1000*60)) as minuti_tot
                    from album a , track t 
                    where a.id = t.album_id
                    group by t.album_id 
                    having sum(t.milliseconds) > %s*1000*60 """

        cursor.execute(query, (durata, ))

        for row in cursor:
            result.append(Album(row["id"], row["title"], row["minuti_tot"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessione(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct t1.album_id  album1, t2.album_id  album2
                    from playlist_track pt1, playlist_track pt2, track t1, track t2
                    where pt1.playlist_id = pt2.playlist_id and pt1.track_id <> pt2.track_id 
                    and pt1.track_id = t1.id and t1.album_id in(
                    select a.id
                    from album a , track t 
                    where a.id = t.album_id
                    group by t.album_id 
                    having sum(t.milliseconds) > %s*1000*60)
                    and pt2.track_id = t2.id and t2.album_id in(
                    select a.id
                    from album a , track t 
                    where a.id = t.album_id
                    group by t.album_id 
                    having sum(t.milliseconds) > %s*1000*60) and t1.album_id < t2.album_id  """

        cursor.execute(query, (durata,durata))

        for row in cursor:
            result.append(Connessione(row["album1"], row["album2"]))

        cursor.close()
        conn.close()
        return result

