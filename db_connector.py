from config import DATABASE_CONFIG
import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.conn_string = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/wmata_db"
        self._connection = None
        
    def connect(self):
        try:
            self._connection = psycopg2.connect(self.conn_string)
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False