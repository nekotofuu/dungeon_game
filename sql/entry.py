from sql.interface import SQLInterface
from typing import Any, Optional, Literal
from sql.lookup import lookup, LookupKey

"""
Module that contains all classes involved in data entry and database manipulation.
"""

class SchemaError(Exception):
    """
    Raises when data does not fit the provided schema
    """
    pass

class DataEntry:
    """
    Class that serves as the data model/interface for the DataEntry GUI app in `gui/`
    """
    def __init__(self, path: Optional[str] = None):
        self.database = SQLInterface(path)

    def request(self, key: LookupKey | str, table: str = "") -> str:
        """
        Responsible for looking up requests inside sql.lookup
        """ 
        request = lookup(key, table)
        if not isinstance(request, str):
            raise ValueError(f"Invalid request format: required str, got {type(request)}")
        return request

    def verify_schema(
            self, 
            table: str, 
            values: dict[str, Any]
        ) -> Literal[True]:
        """
        Verifies schema for data creation and updates
        """
        
        # Verify if keys are equal in size
        dict_keys = {key for key in values.keys()}
        required_schema = lookup(LookupKey.TABLE_SCHEMA, table)
        if required_schema != dict_keys:
            raise SchemaError(f"{values} does not fit the required schema: {required_schema}")
        
        return True

    def get(
            self, 
            table: str, 
            key: str
        ) -> Any:
        """
        Retrieves a single item from the database
        """

        request = self.request(LookupKey.SQL_GET, table)

        search_key = {'key': key}
        data = self.database.db_query(request, search_key)

        if len(data) == 0:
            return None
        else:
            return data[0]

    def add(
            self, 
            table: str, 
            values: dict[str, Any]
        ):
        """
        Adds a row inside the database
        """

        self.verify_schema(table, values)

        request = self.request(LookupKey.SQL_CREATE, table)
        self.database.db_modify(request, values)
        
    def update(
            self, 
            table: str,
            ref_id: str, 
            values: dict[str, Any]
        ):
        """
        Updates an existing row inside the database
        """
        
        self.verify_schema(table, values)

        values["old_id"] = ref_id
        request = self.request(LookupKey.SQL_UPDATE, table)
        self.database.db_modify(request, values)
            
    def read(
            self,
            table: str
        ):
        """
        Retrieves all data from a single table.
        """
        request = self.request(LookupKey.SQL_READ, table)
        data = self.database.db_query(request)
        return data

    def query_table_list(self) -> list[tuple[str]]:
        """
        Retrieves the list of all tables 
        """
        request = self.request(LookupKey.SQL_TABLE_LIST)
        data = self.database.db_query(request)

        return data
    
    def query_table_schema(self, table: str) -> list[tuple[str, str]]:
        """
        Retrieves a list of all tables and their schemas
        """
        request = self.request(LookupKey.SQL_TABLE_SCHEMA, table)
        data = self.database.db_query(request)

        return data