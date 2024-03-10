class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating_for_course()}"

    def rating_for_course(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        return round(sum_rating / len_rating, 2)

    def __lt__(self, other):
        return self.rating_for_course() < other.rating_for_course()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        if not len_rating:
            return 0
        return round(sum_rating / len_rating, 2)

    def rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        if not len_rating:
            return 0
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def rate_lecturer(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer) or (
                course not in lecturer.courses_attached
        ) or (not 0 <= grade <= 10) or (
                course not in self.courses_in_progress
        ):
            raise ValueError("Ошибка")
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]

    def __str__(self):
        return f"""Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за домашние задания: {self.rating()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}"""


student_1 = Student('Роман', 'Круглов', 'м')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

student_2 = Student('Анна', 'Русских', 'ж')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['OOP']

lecturer_1 = Lecturer('Петр', 'Петров')
lecturer_1.courses_attached += ['Python']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)

lecturer_2 = Lecturer('Иван', 'Иванов')
lecturer_2.courses_attached += ['Python']
student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 7)

print(lecturer_1 > lecturer_2)

reviewer_1 = Reviewer('Анжела', 'Смирнова')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Полина', 'Метелёва')
reviewer_2.courses_attached += ['Python']
