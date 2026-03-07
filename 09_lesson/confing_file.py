from sqlalchemy import create_engine 


db_user = "postgres"
db_pass = "mnb098890bnm" 
db_host = "localhost"
db_port = "5432"
db_name = "QA2"

database_url = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

db = create_engine(database_url)

sql_create_table = """
create table if not exists students (
    user_id serial primary key,
    user_name varchar(100) NOT NULL,
    user_age int
);
"""
sql_insert = "INSERT INTO students (user_name, user_age) VALUES (:name, :age) RETURNING user_id;"
sql_select_id = "SELECT * FROM students WHERE user_id = :id;"
sql_update = "UPDATE students SET user_name = :name WHERE user_id = :id;"
sql_delete = "DELETE FROM students WHERE user_id = :id;"
