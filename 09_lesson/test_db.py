import pytest
from sqlalchemy import create_engine, text
from confing_file import database_url, sql_insert, sql_select_id, sql_update, sql_delete

db = create_engine(database_url)

def test_add_student():
    with db.connect() as my_db:
        new_student = my_db.execute(text(sql_insert), {"name": "Darya", "age": 23})

        new_id = new_student.fetchone()[0]
        my_db.commit()

        check = my_db.execute(text(sql_select_id), {"id": new_id}).fetchone()
        assert check.user_name == "Darya"

        my_db.execute(text(sql_delete), {"id": new_id})
        my_db.commit()


def test_update_student():
    with db.connect() as my_db:
        new_student = my_db.execute(text(sql_insert), {"name": "Vadim", "age": 22})
        student_id = new_student.fetchone()[0]
        my_db.commit()

        my_db.execute(text(sql_update), {"name": "Vadim_Updated", "id": student_id})
        my_db.commit()

        check = my_db.execute(text(sql_select_id), {"id": student_id}).fetchone()
        assert check.user_name == "Vadim_Updated"
        
        my_db.execute(text(sql_delete), {"id": student_id})
        my_db.commit()

def test_delete_student():
    with db.connect() as my_db:
        new_student = my_db.execute(text(sql_insert), {"name": "Elena", "age": 25})
        student_id = new_student.fetchone()[0]
        my_db.commit()

        my_db.execute(text(sql_delete), {"id": student_id})
        my_db.commit()

        check = my_db.execute(text(sql_select_id), {"id": student_id}).fetchone()
        assert check is None
