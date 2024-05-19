URL = 'project.db'

TRANSMISSION_TABLE = """
CREATE  TABLE IF NOT EXISTS transmision (
transmision_id INTEGER PRIMARY KEY,
transision char,
transision_type char);
"""

TABLES = [TRANSMISSION_TABLE]
DROP_TABLES = ['transision', 'engine', 'model_type', 'model', 'market']
