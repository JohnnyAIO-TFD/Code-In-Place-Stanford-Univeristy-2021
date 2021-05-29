
class Section:

    def __init__(self, section_number, section_leader, ohyay_link):
        self.section_number = section_number
        self.section_leader = section_leader  # this property is a Participant!
        self.ohyay_link = ohyay_link
        self.students = []  # no students when a section is created! this is a list of Participants

    def add_student(self, student):
        self.students.append(student)

    def get_student_names(self):
        student_names = []

        for student in self.students:
            student_names.append(student.name)

        return student_names
