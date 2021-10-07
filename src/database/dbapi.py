"""
Database handler for a PostgreSQL database
"""


class Database:
    """Class to handle any database operations

    Returns the database object.
    Usage::

      # connect to database
      db = Database(host="localhost", port=5432)
      db.connect()

      # pass index and record data
      db.insert(1577, ("first", "last", "email"))

      # close connection
      db.close

    """

    def __init__(self, host: str = "127.0.0.1", port: int = 5432):
        self.host = host
        self.port = port

    def close(self):
        """Closes database connection"""
        pass

    def connect(self):
        """Connect to database
        The default value for host is '127.0.0.1'. The default port is 5432.
        """
        print("connecting to ", self.port, " at ", self.host)

    def create_schema(self, name, model):
        """Creates a database schema permanently
        Usage::
          
          # Define schema
          schema = {"first": "str", "last": "str"}
          db.create_schema(schema)
        """
        print("Creating schema: ", name, model)
        pass

    def upsert(self, idx, record):
        """Upserts a record to the database"""
        print("Received ", idx, " with ", record)
        pass

if __name__ == '__main__':
    pass
