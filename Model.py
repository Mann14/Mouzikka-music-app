import cx_Oracle
class Model:
    def __init__(self):
        self.song_dict ={}
        self.db_status = True
        self.conn = None
        self.cur = None
        try:
            self.conn = cx_Oracle.connect("mouzikka/mannmusic@127.0.0.1/xe")
            self.cur = self.conn.cursor()
            print("Connected successfully")
        except cx_Oracle.DatabaseError as ex:
            print("IN module DB Error",ex )
            self.db_status = False
    
    def get_db_status(self):
        return self.db_status
    
    def close_db_conn(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
        print("Disconnected successfully")
    
    def add_song(self,song_name,song_path):
        self.song_dict[song_name]=song_path
    
    def get_song_path(self,song_name):
        return self.song_dict[song_name]
    
    def remove_song(self,song_name):
        self.song_dict.pop(song_name)
    
    def search_song_in_favourites(self,song_name):
        self.cur.execute("select song_name from myfavourites where song_name = :1",(song_name,))
        song_tuple = self.cur.fetchone()
        if song_tuple is None:
            return False
        return True
    
    def add_song_in_favourites(self,song_name,song_path):
        is_song_present = self.search_song_in_favourites(song_name)
        if is_song_present:
            return "Song already present in favourites"
        self.cur.execute("select max(song_id) from myfavourites")
        result = self.cur.fetchone()
        last_song_id = result[0]
        next_song_id = 1
        if last_song_id is not None:
            next_song_id = last_song_id + 1
        self.cur.execute("Insert into myfavourites values(:1,:2,:3)",(next_song_id,song_name,song_path))
        self.conn.commit()
        return "Song added to favourites"
    
    def load_song_from_favourites(self):
        self.cur.execute("select song_name,song_path from myfavourites")
        song_present = False
        for song_name,song_path in self.cur:
            self.song_dict[song_name] = song_path
            song_present = True
        if song_present:
            return "List populated with favourites"
        else:
            return "No songs is present in favourites"
    
    def remove_song_from_favourites(self,song_name):
        self.cur.execute("Delete from myfavourites where song_name = :1",(song_name,))
        if self.cur.rowcount == 0:
            return "Song not present in your favourites"
        self.song_dict.pop(song_name)
        self.conn.commit()
        return "Song deleted from your favourites"
    
    def get_song_count(self):
        return len(self.song_dict)        