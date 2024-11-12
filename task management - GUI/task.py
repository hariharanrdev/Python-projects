class Task:
    def __init__(self, title, deadline, priority):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.status = "Not Started"

    def __str__(self):
        return f"Task: {self.title}, Deadline: {self.deadline}, Priority: {self.priority}, Status: {self.status}"