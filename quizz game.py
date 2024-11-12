import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Optional for adding images to your GUI

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Application")
        self.master.geometry("500x400")
        self.master.config(bg="#f5f5f5")

        # Variables
        self.score = 0
        self.question_index = 0

        # Question and Answer list (10 TCS Python Interview Questions)
        self.questions = [
            ("What is the output of the expression `3 * 1 ** 3` in Python?", ["0", "3", "1", "9"], "3"),
            ("Which of the following is the correct way to create a list in Python?", ["list = ()", "list = []", "list = {}", "list = //"], "list = []"),
            ("Which of the following function is used to generate random numbers in Python?", ["random()", "rand()", "generate()", "randomize()"], "random()"),
            ("What is the output of the following code?\n```print('A' * 3)```", ["AAA", "A3", "3A", "Error"], "AAA"),
            ("Which of the following is used to create an object in Python?", ["A function", "A class", "A method", "A constructor"], "A class"),
            ("How do you declare a function in Python?", ["function myFunc(){}", "def myFunc():", "declare myFunc(){}", "func myFunc(){}"], "def myFunc():"),
            ("Which of the following is true for variable names in Python?", ["They can start with a number", "They can contain spaces", "They are case sensitive", "They are not case sensitive"], "They are case sensitive"),
            ("What is the difference between a tuple and a list in Python?", ["Tuples are immutable", "Lists are immutable", "Tuples can contain only integers", "Lists can only store strings"], "Tuples are immutable"),
            ("Which keyword is used to handle exceptions in Python?", ["catch", "try", "except", "finally"], "except"),
            ("Which of the following is a correct syntax to open a file in Python?", ["open('file.txt', 'r')", "open('file.txt', 'rw')", "file('file.txt', 'open')", "open.file('file.txt', 'r')"], "open('file.txt', 'r')")
        ]

        # Title label
        self.title_label = tk.Label(self.master, text="TCS Python Interview Quiz", font=("Arial", 20, "bold"), bg="#f5f5f5")
        self.title_label.pack(pady=20)

        # Question label
        self.question_label = tk.Label(self.master, text="", font=("Arial", 16), wraplength=400, bg="#f5f5f5")
        self.question_label.pack(pady=10)

        # Radio button variables
        self.radio_var = tk.StringVar()
        self.radio_buttons = []

        # Answer options (created dynamically)
        for i in range(4):
            rb = tk.Radiobutton(self.master, text="", variable=self.radio_var, value=i, font=("Arial", 14),
                                bg="#f5f5f5", anchor="w")
            rb.pack(fill='x', padx=20, pady=5)
            self.radio_buttons.append(rb)

        # Submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font=("Arial", 14),
                                       bg="#007bff", fg="white", width=15, height=2)
        self.submit_button.pack(pady=20)

        # Load the first question
        self.load_question()

    def load_question(self):
        """Load the next question."""
        if self.question_index < len(self.questions):
            question, options, _ = self.questions[self.question_index]
            self.question_label.config(text=question)

            # Update the radio button text
            for i, option in enumerate(options):
                self.radio_buttons[i].config(text=option, value=option)
            self.radio_var.set(None)  # Deselect all options
        else:
            self.show_result()

    def check_answer(self):
        """Check the selected answer."""
        selected = self.radio_var.get()
        if not selected:
            messagebox.showwarning("No Answer", "Please select an answer!")
        else:
            _, _, correct_answer = self.questions[self.question_index]
            if selected == correct_answer:
                self.score += 1
            self.question_index += 1
            self.load_question()

    def show_result(self):
        """Display the final score and end the quiz."""
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
        self.master.quit()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
