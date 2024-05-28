import sqlite3

class TextProcessor:
    """r"""
    def __init__(self, text):
        self.text = text

    def find_words_with_fragment(self, fragment):
        """r"""
        words = self.text.split()
        return [word for word in words if fragment in word]

    def find_longest_words(self, num_words):
        """r"""
        words = self.text.split()
        sorted_words = sorted(words, key=len, reverse=True)
        return sorted_words[:num_words]

    def remove_fragments(self, fragments):
        """r"""
        for fragment in fragments:
            self.text = self.text.replace(fragment, "")
        return self.text

class DatabaseWriter(TextProcessor):
    """r"""
    def write_to_database(self, db_name):
        """r"""
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS processed_text (id INTEGER PRIMARY KEY, text TEXT)")
        cursor.execute("INSERT INTO processed_text (text) VALUES (?)", (self.text,))
        cursor.execute()
        conn.commit()
        conn.close()

# Example usage:
if __name__ == "__main__":
    sample_text = "Tai yra pavyzdinis tekstas su fragmentais."
    processor = TextProcessor(sample_text)
    print("Words with 'fragmentas':", processor.find_words_with_fragment("fragmentas"))
    print("5 longest words:", processor.find_longest_words(5))
    processed_text = processor.remove_fragments(["fragmentais", "pavyzdinis"])
    print("Processed text after fragment removal:", processed_text)

    db_writer = DatabaseWriter(sample_text)
    db_writer.write_to_database("my_database.db")
