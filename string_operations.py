from collections import Counter
import tkinter as tk
import matplotlib.pyplot as plt

class StringOperationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Operations")

        # Widgets
        self.label = tk.Label(root, text="Enter a string:")
        self.label.pack()

        self.string_entry = tk.Entry(root)
        self.string_entry.pack()

        self.process_button = tk.Button(root, text="Process String", command=self.process_string)
        self.process_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.stats_button = tk.Button(root, text="Show Letter Frequency", command=self.display_letter_frequency)
        self.stats_button.pack()

    def process_string(self):
        self.input_string = self.string_entry.get().lower()
        self.processed_string = [char for char in self.input_string if char.isalpha()]
        self.letter_count = Counter(self.processed_string)
        self.result_label.config(text=f"Letter Frequencies: {self.letter_count}")

    def display_letter_frequency(self):
        labels, values = zip(*self.letter_count.items())
        plt.bar(labels, values)
        plt.title("Letter Frequency")
        plt.show()

# GUI Initialization
root = tk.Tk()
app = StringOperationsApp(root)
root.mainloop()
