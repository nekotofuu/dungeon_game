import pytest
from classes.utils.randgen import randstr, randbool
from sql.entry import DataEntry, SchemaError
from sql.lookup import *

TEST_DB_PATH = "tests/test_object_init.db"
entry_obj = DataEntry(TEST_DB_PATH)

def test_sql_init():
    inst = DataEntry(TEST_DB_PATH)
    assert inst.database.path == TEST_DB_PATH

    inst = DataEntry()
    assert inst.database.path == "sql/object_init.db"

def test_sql_verify_schema():
    item_data = {
        'id': randstr(10),
        'name': randstr(10),
        'desc': randstr(50)
    }

    usable_data = {
        'id': randstr(10),
        'name': randstr(10),
        'desc': randstr(50),
        'use_type': randstr(10),
        'use_param': randstr(30)
    }

    equip_data = {
        'id': randstr(10),
        'name': randstr(10),
        'desc': randstr(50),
        'element': randstr(10),
        'attribute': randstr(50),
        'skill': randstr(50),
        'is_dual_wield': int(randbool())
    }

    assert entry_obj.verify_schema('item', item_data)
    assert entry_obj.verify_schema('usable', usable_data)
    assert entry_obj.verify_schema('equip', equip_data)

def test_sql_insert_retrieve_item():
    data = {
        'id': randstr(10),
        'name': randstr(10),
        'desc': randstr(50)
    }

    # Add item
    entry_obj.add('item', data)
    
    # Get item
    returned_data = entry_obj.get('item', data['id'])

    # Extract data
    extracted_db_data = tuple([returned_data[i] for i in range(1, len(returned_data))])
    extracted_test_data = tuple([value for value in data.values()])
    
    assert extracted_db_data == extracted_test_data

def test_sql_insert_retrieve_usable():
    data = {
        'id': randstr(10),
        'name': randstr(10),
        'desc': randstr(50),
        'use_type': randstr(10),
        'use_param': randstr(40)
    }

    # Add item
    entry_obj.add('usable', data)
    
    # Get item
    returned_data = entry_obj.get('usable', data['id'])

    # Extract data
    extracted_db_data = tuple([returned_data[i] for i in range(1, len(returned_data))])
    extracted_test_data = tuple([value for value in data.values()])
    
    assert extracted_db_data == extracted_test_data
    
def test_sql_insert_retrieve_equip():
    data = {
        'id': randstr(10),
        'name': randstr(10),
        'desc': randstr(50),
        'element': randstr(10),
        'attribute': randstr(10),
        'skill': randstr(50),
        'is_dual_wield': int(randbool())
    }

    # Add item
    entry_obj.add('equip', data)
    
    # Get item
    returned_data = entry_obj.get('equip', data['id'])

    # Extract data
    extracted_db_data = tuple([returned_data[i] for i in range(1, len(returned_data))])
    extracted_test_data = tuple([value for value in data.values()])
    
    assert extracted_db_data == extracted_test_data
    
def test_sql_retrieve_errors():
    # No keys in database
    assert entry_obj.get('item', 'invalid_key') == None
    assert entry_obj.get('equip', 'invalid_key') == None
    assert entry_obj.get('usable', 'invalid_key') == None
    
    # No table in schema
    with pytest.raises(ValueError):
        entry_obj.get('invalid', "null")

def test_sql_insert_errors():
    # Dummy data
    invalid_item_data = {
        'item': randstr(10),
        'desc': randstr(50),
        'name': randstr(10)
    }    
    
    # Invalid data schema
    with pytest.raises(SchemaError):
        entry_obj.add('item', invalid_item_data)
    
    # Invalid table input
    with pytest.raises(ValueError):
        entry_obj.add('invalid_table', invalid_item_data)

def test_get_table_list():
    table_list = entry_obj.query_table_list()
    for table in table_list:
        if table[0] in ('item', 'equip', 'usable'): continue
        raise AssertionError("invalid table listing")
    