LANT_INITIALS = {
    "C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"
}
PLANTS_PER_STUDENT = 4
class Garden:
    """
    Represents a garden with `ROWS` rows, where each student is assigned
    `PLANTS_PER_STUDENT` plants.
    """
    def __init__(self, diagram, students=[]):
        if students:
            students.sort()
        else:
            students = [
                "Alice", "Bob",     "Charlie", "David",  "Eve",     "Fred",
                "Ginny", "Harriet", "Illeana", "Joseph", "Kincaid", "Larry"
            ]
        diagram = diagram.splitlines()
        ROWS = len(diagram)
        COLUMNS = len(diagram[0])
        # Only retain as many students as the diagram supports.
        students = students[:ROWS*COLUMNS//PLANTS_PER_STUDENT]
        self.students_plants = {}
        for i, student in enumerate(students):
            plants = []
            for j in range(ROWS):
                for k in range(PLANTS_PER_STUDENT//ROWS):
                    plants.append(PLANT_INITIALS[diagram[j][ROWS*i + k]])
            self.students_plants[student] = plants
    def plants(self, name):
        """
        Return a list of the plants belonging to a student.
        """
        return self.students_plants[name]

