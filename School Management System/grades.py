import database

def get_student_grades(student_id):
    grades = database.get_all_grades()
    output = ""
    for gid, record in grades.items():
        if record["student"] == student_id:
            output += f"Class: {record['class']} - Marks: {record['marks']}\n"
    return output or "No grades available."

def add_grade(student_id, class_id, marks):
    grades = database.get_all_grades()
    grade_id = f"{student_id}_{class_id}"
    grades[grade_id] = {
        "student": student_id,
        "class": class_id,
        "marks": marks
    }
    database.save_all_grades(grades)
