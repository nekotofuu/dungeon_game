from typing import Dict, Set, Literal, Any
from sql.interface import SQLInterface
from enum import Enum

class LookupType(Enum):
    """
    Enum for classifying lookup types and their types of handling/processing on retrieval
    
    `NONE`, `REQUEST` -> no processing; represents plain data/request\n
    `REQ_FORMAT` -> SQL requests that need external formatting\n
    `REQ_LOOKUP` -> for nested lookups; often for table specific SQL requests\n
    `ANY_LOOKUP` -> nested lookups that doesn't involve requests
    """
    NONE = 0
    REQUEST = 0
    REQ_FORMAT = 1
    REQ_LOOKUP = 2
    ANY_LOOKUP = 3

class LookupKey(Enum):
    """
    Enum for simplifying lookup using keys
    Uses constants instead of keys.
    """
    TABLE_LIST = "table_list"
    TABLE_SCHEMA = "table_schema"
    SQL_GET = "sql_get"
    SQL_TABLE_SCHEMA = "sql_query_table_schema"
    SQL_TABLE_LIST = "sql_query_table_list"
    SQL_READ = "sql_read"
    SQL_UPDATE = "sql_update"
    SQL_CREATE = "sql_create"

def lookup(key: str | LookupKey, table: str = ""):
    """
    Main lookup function
    Takes a key and some table information for lookup values that need additional processing
    """

    # Convert lookup key to its string equivalent
    if isinstance(key, LookupKey):
        _key = key.value
    else:
        _key = key
    
    # Access type and values
    lookup_type: LookupType = _SQL_Info[_key]['type'].value
    lookup_value: Any = _SQL_Info[_key]['value']

    if not table == "":
        verify_table(table)

    if lookup_type == 0:
        return lookup_value
    elif lookup_type == 1:
        f_request: str = lookup_value.format(table=table)
        return f_request
    elif lookup_type == 2:
        s_request: str = lookup_value[table]
        return s_request
    elif lookup_type == 3:
        return lookup_value[table]
    else:
        raise NotImplementedError("Something went wrong.")

def verify_table(table: str) -> Literal[True]:
    """
    Verify whether the table is in the table of all possible tables.
    Directly queries SQL database to retrieve a list of tables
    """
    sqlinter = SQLInterface()
    table_list_request: str = _SQL_Info['sql_query_table_list']['value']
    
    table_list = [table[0] for table in sqlinter.db_query(table_list_request)]
    
    if table in table_list:
        return True
    else:
        raise ValueError(f"{table} not in list of accepted tables")
    

_SQL_Info: Dict[str | LookupKey, Dict[str, Any]] = {
    'sql_get': {
        'type': LookupType.REQ_FORMAT,
        'value': "SELECT * FROM {table} WHERE ref_id = :key;"
    },

    'sql_query_table_schema': {
        'type': LookupType.REQ_FORMAT,
        'value': "SELECT name, type FROM PRAGMA_TABLE_INFO('{table}');"
    },

    'sql_query_table_list': {
        'type': LookupType.REQUEST,
        'value': "SELECT name FROM sqlite_schema WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
    },
    
    'sql_read': {
        'type': LookupType.REQ_FORMAT,
        'value': "SELECT * FROM {table};"
    },

    'table_schema': {
        'type': LookupType.ANY_LOOKUP,
        'value': {
            'item': {'id', 'name', 'desc'},
            'usable': {'id', 'name', 'desc', 'use_type', 'use_param'},
            'equip': {'id', 'name', 'desc', 'element', 'attribute', 'skill', 'is_dual_wield'}
        }
    },

    'sql_create': {
        'type': LookupType.REQ_LOOKUP,
        'value': {
            'item': "INSERT INTO item (ref_id, name, desc) VALUES (:id, :name, :desc);",
            'usable': "INSERT INTO usable (ref_id, name, desc, use_type, use_param) VALUES (:id, :name, :desc, :use_type, :use_param);",
            'equip': "INSERT INTO equip (ref_id, name, desc, element, attribute, skill, dual_wield) VALUES (:id, :name, :desc, :element, :attribute, :skill, :is_dual_wield);",
        }
    },

    'sql_update': {
        'type': LookupType.REQ_LOOKUP,
        'value': {
            'item': "UPDATE item SET ref_id = :id, name = :name, desc = :desc WHERE ref_id = :old_id;",
            'usable': "UPDATE usable SET ref_id = :id, name = :name, desc = :desc, use_type = :use_type, use_param = :use_param WHERE ref_id = :old_id;",
            'equip': "UPDATE equip SET ref_id = :id, name = :name, desc = :desc, element = :element, attribute_data = :attribute, skill = :skill, dual_wield = :is_dual_wield WHERE ref_id = :old_id;",
        }
    }   
}