from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

# create a table to store data about instances of department class.


    @classmethod
# create and drop table methods are the job of class, not instances.
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
            """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS departments
            """
        CURSOR.execute(sql)
        CONN.commit()

# save the attributes of an object as a new table row.

    def save(self):
        sql = """
            INSERT INTO departments (name, location)
            VALUES (?,?)
            """
        CURSOR.execute(sql, (self.name, self.location))
        self.id = CURSOR.lastrowid
        CONN.commit()

    
    @classmethod
    def create(cls, name, location):
        department = cls(name, location)
        department.save()
        return department
    

    #update an object's corresponding table row
    def update(self):
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ? 
            """
        
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    
    #DELETE from departments 
    def delete(self):
        sql = """
            DELETE FROM departments
            WHERE id =?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()


