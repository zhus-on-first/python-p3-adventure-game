import sqlite3

# Set up a connection and cursor for SQLite3
CONN = sqlite3.connect('game.db')
CURSOR = CONN.cursor()

class Scenario:
    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description

    @classmethod
    def create_table(cls):
        # SQL command to create a new Scenarios table
        sql = """
            CREATE TABLE IF NOT EXISTS scenarios (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        # Save scenario instance to the new database row
        sql = """
            INSERT INTO scenarios (name, description)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.description))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_random_scenarios(cls, num_scenarios):
        # Fetch a specified number of random scenarios from the database
        sql = """
            SELECT * FROM scenarios
            ORDER BY RANDOM()
            LIMIT ?
        """
        rows = CURSOR.execute(sql, (num_scenarios,)).fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]

# Creating the table
Scenario.create_table()

# Adding scenarios to the table
scenario1 = Scenario(name="Enchanted Cavern", description="You stumble upon the mesmerizing Glowworm Guardian.")
scenario1.save()
# ... (Add other scenarios here)
