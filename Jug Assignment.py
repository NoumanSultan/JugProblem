import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from collections import deque

# Function to check if we reached the goal state
def is_goal(state, goal_state):
    return state == goal_state

# Function to pour water between jugs
def pour(source, target, target_cap):
    transfer_amount = min(source, target_cap - target)
    return source - transfer_amount, target + transfer_amount

# Function to return possible moves from a given state
def get_next_states(state):
    a, b, c = state
    next_states = []
    
    # Pour from 8ml jug to 5ml jug
    new_a, new_b = pour(a, b, 5)
    next_states.append((new_a, new_b, c))
    
    # Pour from 8ml jug to 3ml jug
    new_a, new_c = pour(a, c, 3)
    next_states.append((new_a, b, new_c))
    
    # Pour from 5ml jug to 8ml jug
    new_b, new_a = pour(b, a, 8)
    next_states.append((new_a, new_b, c))
    
    # Pour from 5ml jug to 3ml jug
    new_b, new_c = pour(b, c, 3)
    next_states.append((a, new_b, new_c))
    
    # Pour from 3ml jug to 8ml jug
    new_c, new_a = pour(c, a, 8)
    next_states.append((new_a, b, new_c))
    
    # Pour from 3ml jug to 5ml jug
    new_c, new_b = pour(c, b, 5)
    next_states.append((a, new_b, new_c))
    
    return next_states

# Function to solve the water jug problem
def solve_water_jug_problem(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    
    while queue:
        current_state, path = queue.popleft()
        
        if is_goal(current_state, goal_state):
            return path + [current_state]
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
    
    return None

# GUI Application
class WaterJugGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Water Jug Problem Solver")
        self.geometry("400x450")
        self.create_widgets()
        
    def create_widgets(self):
        # Labels and Entry widgets for the initial state
        tk.Label(self, text="Initial State (8ml, 5ml, 3ml)").grid(row=0, column=0, columnspan=3, pady=5)
        
        tk.Label(self, text="8ml Jug:").grid(row=1, column=0, padx=5)
        self.initial_8ml = tk.Entry(self)
        self.initial_8ml.grid(row=1, column=1)
        
        tk.Label(self, text="5ml Jug:").grid(row=2, column=0, padx=5)
        self.initial_5ml = tk.Entry(self)
        self.initial_5ml.grid(row=2, column=1)
        
        tk.Label(self, text="3ml Jug:").grid(row=3, column=0, padx=5)
        self.initial_3ml = tk.Entry(self)
        self.initial_3ml.grid(row=3, column=1)
        
        # Labels and Entry widgets for the goal state
        tk.Label(self, text="Goal State (8ml, 5ml, 3ml)").grid(row=4, column=0, columnspan=3, pady=5)
        
        tk.Label(self, text="8ml Jug:").grid(row=5, column=0, padx=5)
        self.goal_8ml = tk.Entry(self)
        self.goal_8ml.grid(row=5, column=1)
        
        tk.Label(self, text="5ml Jug:").grid(row=6, column=0, padx=5)
        self.goal_5ml = tk.Entry(self)
        self.goal_5ml.grid(row=6, column=1)
        
        tk.Label(self, text="3ml Jug:").grid(row=7, column=0, padx=5)
        self.goal_3ml = tk.Entry(self)
        self.goal_3ml.grid(row=7, column=1)
        
        # Solve, Reset, and Save buttons
        tk.Button(self, text="Solve", command=self.solve).grid(row=8, column=0, padx=5, pady=10)
        tk.Button(self, text="Reset", command=self.reset).grid(row=8, column=1, padx=5, pady=10)
        tk.Button(self, text="Save as .txt", command=self.save_to_file).grid(row=8, column=2, padx=5, pady=10)
        
        # ScrolledText to display the solution steps
        self.solution_text = scrolledtext.ScrolledText(self, height=10, width=40)
        self.solution_text.grid(row=11, column=0, columnspan=3, pady=5)
        
    def solve(self):
        try:
            # Get the initial and goal states from user input
            initial_state = (int(self.initial_8ml.get()), int(self.initial_5ml.get()), int(self.initial_3ml.get()))
            goal_state = (int(self.goal_8ml.get()), int(self.goal_5ml.get()), int(self.goal_3ml.get()))
            
            # Validate jug capacities
            if (initial_state[0] > 8 or initial_state[1] > 5 or initial_state[2] > 3 or 
                goal_state[0] > 8 or goal_state[1] > 5 or goal_state[2] > 3):
                messagebox.showerror("Invalid Input", "Jug capacities exceed the jug limits.")
                return
            
            # Solve the problem
            solution = solve_water_jug_problem(initial_state, goal_state)
            
            # Clear previous results
            self.solution_text.delete(1.0, tk.END)
            
            if solution:
                self.solution_text.insert(tk.END, "Solution Steps:\n")
                for step in solution:
                    self.solution_text.insert(tk.END, f"Jug states: {step}\n")
            else:
                self.solution_text.insert(tk.END, "No solution possible.")
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for jug capacities.")
    
    def reset(self):
        # Clear all entry fields and solution text area
        self.initial_8ml.delete(0, tk.END)
        self.initial_5ml.delete(0, tk.END)
        self.initial_3ml.delete(0, tk.END)
        self.goal_8ml.delete(0, tk.END)
        self.goal_5ml.delete(0, tk.END)
        self.goal_3ml.delete(0, tk.END)
        self.solution_text.delete(1.0, tk.END)
    
    def save_to_file(self):
        # Get the text from the solution text box
        solution_steps = self.solution_text.get(1.0, tk.END).strip()
        
        # If there are no steps to save, show a message
        if not solution_steps:
            messagebox.showinfo("No Solution", "There is no solution to save.")
            return
        
        # Open file dialog to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(solution_steps)
            messagebox.showinfo("Success", "Solution saved successfully!")

# Run the application
if __name__ == "__main__":
    app = WaterJugGUI()
    app.mainloop()
