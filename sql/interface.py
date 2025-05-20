import sqlite3
from typing import Any, Optional

class SQLInterface:

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
            data: dict[str, Any]
        ) -> list[Any]:
        
        with sqlite3.connect(self.__database_path) as conn:
            cur = conn.cursor()

            cur.execute(request, data)
            return cur.fetchall()
        

    def db_modify(
            self,
            request: str,
            data: dict[str, Any]
        ):

        with sqlite3.connect(self.__database_path) as conn:
            cur = conn.cursor()

            cur.execute(request, data)
            conn.commit()


