import sqlite3
from typing import Any, Optional

class SQLInterface:
    """
    Class interface for sending queries to the SQL database
    `path` defaults to `"sql/object_init.db"` but can be specified to any valid SQL database path.
    """
    def __init__(
            self, 
            path: Optional[str] = "sql/object_init.db"
        ):
        self.__database_path = path if path is not None else "sql/object_init.db"

    @property
    def path(self):
        return self.__database_path
    
    def db_query(
            self, 
            request: str, 
            data: dict[str, Any] = {}
        ) -> list[Any]:
        """
        Requests data from the database and returns its fetch result.
        `request` must be a valid SQL request.
        `data` is any optional data needed by request (such as named replacement fields) 
        """
        with sqlite3.connect(self.__database_path) as conn:
            cur = conn.cursor()

            cur.execute(request, data)
            return cur.fetchall()
        

    def db_modify(
            self,
            request: str,
            data: dict[str, Any] = {}
        ) -> None:
        """
        Modifies data from the database
        `request` must be a valid SQL request.
        `data` is any optional data needed by request (such as named replacement fields) 
        """
        with sqlite3.connect(self.__database_path) as conn:
            cur = conn.cursor()

            cur.execute(request, data)
            conn.commit()


