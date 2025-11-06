from .student import Student


def find_by_id_student(cursor, id) -> Student | None:
    sql = "SELECT * FROM student WHERE id = %s"

    data = [id]
    cursor.execute(sql, data)
    row = cursor.fetchone()

    student_obj = None
    if row is not None:
        student_obj = Student(
            id=row["id"], name=row["name"], birthday=row["birthday"], clazz=row["class"]
        )
    return student_obj


def select_all(cursor) -> list[Student]:
    sql = "SELECT * FROM student ORDER BY id"

    cursor.execute(sql)
    rows = cursor.fetchall()

    students = []
    for row in rows:
        student_obj = Student(
            id=row["id"], name=row["name"], birthday=row["birthday"], clazz=row["class"]
        )
        students.append(student_obj)

    return students


def insert_student(cursor, student: Student) -> None:
    sql = "INSERT INTO student (id, name, birthday, class) VALUES (%s, %s, %s, %s)"
    data = [student.id, student.name, student.birthday, student.clazz]
    cursor.execute(sql, data)
