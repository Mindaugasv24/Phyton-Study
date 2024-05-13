import sqlite3  # You can replace this with your preferred database library

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        """Connect to the database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            print("Connected to the database successfully!")
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def execute_query(self, query):
        """Execute an SQL query."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully!")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def create_table(self, table_name, columns):
        """Create a table with specified columns."""
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_query(query)

    def insert_data(self, table_name, values):
        """Insert data into a table."""
        query = f"INSERT INTO {table_name} VALUES ({values})"
        self.execute_query(query)

    def delete_table(self, table_name):
        """Delete a table."""
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.execute_query(query)

    def delete_data(self, table_name, condition):
        """Delete data from a table based on a condition."""
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query)

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    db_manager = DatabaseManager("my_database.db")
    db_manager.connect()

    # Create a table
    db_manager.create_table("employees", "id INTEGER PRIMARY KEY, name TEXT, salary REAL")

    # Insert data
    db_manager.insert_data("employees", "(1, 'John Doe', 50000)")
    db_manager.insert_data("employees", "(2, 'Jane Smith', 60000)")

    # Delete data
    db_manager.delete_data("employees", "id = 1")

    # Delete the table
    db_manager.delete_table("employees")

    db_manager.close_connection()