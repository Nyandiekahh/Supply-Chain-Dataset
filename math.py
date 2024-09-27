import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.correct = 0
        self.incorrect = 0
        self.total_attempts = 0

        # Create widgets
        self.label = tk.Label(root, text="Select Operation: 1.Addition 2.Subtraction 3.Multiplication 4.Division")
        self.label.pack()

        self.operation_entry = tk.Entry(root)
        self.operation_entry.pack()

        self.start_button = tk.Button(root, text="Start Quiz", command=self.generate_question)
        self.start_button.pack()

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.stats_button = tk.Button(root, text="Show Stats", command=self.display_statistics)
        self.stats_button.pack()

        # Possible responses
        self.correct_responses = ['Very good!', 'Nice work!', 'Keep up the good work!']
        self.incorrect_responses = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']

    def generate_question(self):
        self.num1, self.num2 = random.randint(1, 10), random.randint(1, 10)
        operation = int(self.operation_entry.get())
        if operation == 1:
            self.correct_answer = self.num1 + self.num2
            question_text = f"What is {self.num1} + {self.num2}?"
        elif operation == 2:
            self.correct_answer = self.num1 - self.num2
            question_text = f"What is {self.num1} - {self.num2}?"
        elif operation == 3:
            self.correct_answer = self.num1 * self.num2
            question_text = f"What is {self.num1} * {self.num2}?"
        elif operation == 4:
            self.num2 = random.randint(1, 10)  # Avoid division by 0
            self.correct_answer = self.num1 // self.num2
            question_text = f"What is {self.num1} // {self.num2}?"
        else:
            question_text = "Invalid operation. Please enter a number between 1 and 4."
        self.question_label.config(text=question_text)

    def check_answer(self):
        user_answer = int(self.answer_entry.get())
        if user_answer == self.correct_answer:
            response = random.choice(self.correct_responses)
            self.result_label.config(text=f"Correct! {response}", fg="green")
            self.correct += 1
        else:
            response = random.choice(self.incorrect_responses)
            self.result_label.config(text=f"Incorrect. {response} The correct answer was {self.correct_answer}.", fg="red")
            self.incorrect += 1
        self.total_attempts += 1

    def display_statistics(self):
        labels = ['Correct', 'Incorrect']
        values = [self.correct, self.incorrect]
        plt.bar(labels, values)
        plt.title(f"Quiz Stats: {self.total_attempts} Attempts")
        plt.show()

# GUI Initialization
root = tk.Tk()
app = MathQuizApp(root)
root.mainloop()
