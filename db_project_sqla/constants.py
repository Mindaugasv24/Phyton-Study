URL = 'database/project.db'

transmision_table = """
CREATE  TABLE IF NOT EXISTS transmision (
transmision_id INTEGER PRIMARY KEY,
transision char,
transision_type char);
"""

TABLES = [transmision_table]

DROP_TABLES = ['transision', 'engine', 'model_type', 'model', 'market']
