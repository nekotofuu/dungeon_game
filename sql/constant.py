# Request lookup tables

# Valid table list
TABLE_LIST = (
    'item', 'usable', 'equip'
)

# Schema lookup table
SCHEMA_DICT = {
    'item': {'id', 'name', 'desc'},
    'usable': {'id', 'name', 'desc', 'use_type', 'use_param'},
    'equip': {'id', 'name', 'desc', 'element', 'attribute', 'skill', 'is_dual_wield'}
}

# Update Request lookup table
UPDATE_DICT = {
    'item': "UPDATE item SET ref_id = :id, name = :name, desc = :desc WHERE ref_id = :old_id;",
    'usable': "UPDATE usable SET ref_id = :id, name = :name, desc = :desc, use_type = :use_type, use_param = :use_param WHERE ref_id = :old_id;",
    'equip': "UPDATE equip SET ref_id = :id, name = :name, desc = :desc, element = :element, attribute_data = :attribute, skill = :skill, dual_wield = :is_dual_wield WHERE ref_id = :old_id;",
}

# Insert Request Lookup table 
INSERT_DICT = {
    'item': "INSERT INTO item (ref_id, name, desc) VALUES (:id, :name, :desc);",
    'usable': "INSERT INTO usable (ref_id, name, desc, use_type, use_param) VALUES (:id, :name, :desc, :use_type, :use_param);",
    'equip': "INSERT INTO equip (ref_id, name, desc, element, attribute, skill, dual_wield) VALUES (:id, :name, :desc, :element, :attribute, :skill, :is_dual_wield);",
}

# Get data lookup table
GET_DATA =  "SELECT * FROM {table} WHERE ref_id = :key;"
