from sql.interface import SQLInterface
from typing import Any, Optional
from sql.constant import *

class SchemaError(Exception):
    """
    Raise when data does not fit the provided schema
    """
    pass

class DataEntry:
    def __init__(self, path: Optional[str] = None):
        self.database = SQLInterface(path)

    def verify_schema(
            self, 
            table: str, 
            values: dict[str, Any]
        ) -> bool:
        
        # Verify if table in list
        if table not in TABLE_LIST:
            raise ValueError(f"{table} not in list of accepted tables")
        
        # Verify if keys are equal in size
        dict_keys = {key for key in values.keys()}
        required_schema = SCHEMA_DICT[table]
        if required_schema != dict_keys:
            raise SchemaError(f"{values} does not fit the required schema: {required_schema}")
        
        return True

    def get(
            self, 
            table: str, 
            key: str
        ) -> Any:
        if table not in TABLE_LIST:
            raise ValueError(f"{table} not in list of accepted tables")
        else:
            request = GET_DATA.format(table=table)

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

        self.verify_schema(table, values)

        request = INSERT_DICT[table]
        self.database.db_modify(request, values)
        

    def update(
            self, 
            table: str,
            ref_id: str, 
            values: dict[str, Any]
        ):
        
        self.verify_schema(table, values)

        values["old_id"] = ref_id
        request = UPDATE_DICT[table]

        self.database.db_modify(request, values)
            
    

            