from .exam import Exam


def select_all(cursor) -> list[Exam]:
    sql = """
    SELECT * FROM exam
    ORDER BY id, score DESC
    """

    cursor.execute(sql)
    rows = cursor.fetchall()

    exams = []
    for row in rows:
        exam_obj = Exam(
            id=row["id"],
            subject=row["subject"],
            score=row["score"],
        )
        exams.append(exam_obj)

    return exams


def find_by_id(cursor, id) -> list[Exam]:
    sql = """
    SELECT * FROM exam
    WHERE id = %s
    ORDER BY id, score DESC
    """

    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    exams = []
    for row in rows:
        exam_obj = Exam(
            id=row["id"],
            subject=row["subject"],
            score=row["score"],
        )
        exams.append(exam_obj)
    return exams


def find_by_id_and_subject(cursor, id, subject) -> Exam | None:
    sql = """
    SELECT * FROM exam
    WHERE id = %s AND subject = %s
    ORDER BY id DESC
    """

    data = [id, subject]
    cursor.execute(sql, data)
    row = cursor.fetchone()

    exam_obj = None
    if row:
        exam_obj = Exam(
            id=row["id"],
            subject=row["subject"],
            score=row["score"],
        )
    return exam_obj


def insert_exam(cursor, exam: Exam) -> None:
    sql = """
    INSERT INTO exam (id, subject, score)
    VALUES (%s, %s, %s)
    """

    data = [exam.id, exam.subject, exam.score]
    cursor.execute(sql, data)


def update_exam(cursor, exam: Exam, change_subject: str) -> None:
    sql = """
    UPDATE exam
    SET subject = %s, score = %s
    WHERE id = %s AND subject = %s
    """

    data = [change_subject, exam.score, exam.id, exam.subject]
    cursor.execute(sql, data)


def delete_exam(cursor, id, subject) -> None:
    sql = """
    DELETE FROM exam
    WHERE id = %s AND subject = %s
    """

    data = [id, subject]
    cursor.execute(sql, data)
