# Water Jug Problem Solver

This is a simple GUI-based application built with Python and Tkinter that solves the classic Water Jug Problem. The Water Jug Problem involves determining how to measure out exactly a certain amount of water using jugs of different capacities. This program solves the problem for jugs with capacities of 8ml, 5ml, and 3ml.

## Features

- Input initial and goal water levels for each jug.
- Solve the Water Jug Problem with detailed step-by-step solutions.
- Reset inputs and clear solutions for new problems.
- Save the solution steps as a `.txt` file for later reference.

## Installation

To run the project, you need to have Python installed on your system along with the Tkinter package (which usually comes pre-installed with Python).

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/water-jug-problem-solver.git
    ```

2. Navigate to the project directory:

    ```bash
    cd water-jug-problem-solver
    ```

3. Run the application:

    ```bash
    python water_jug_solver.py
    ```

## How to Use

1. Enter the initial state of the jugs (8ml, 5ml, 3ml capacities) in the appropriate fields.
2. Enter the goal state you wish to reach for the jugs.
3. Click the **Solve** button to find the solution.
4. The steps to reach the goal will be displayed in the text box below.
5. Use the **Reset** button to clear all inputs and results.
6. You can also save the solution as a `.txt` file using the **Save as .txt** button.

### Example

For example, if you want to go from (8, 0, 0) to (4, 4, 0):

- Input the initial state: 8ml = 8, 5ml = 0, 3ml = 0
- Input the goal state: 8ml = 4, 5ml = 4, 3ml = 0
- Click **Solve**, and the solution will show the series of steps to reach the goal state.

## Files

- `water_jug_solver.py`: The main Python script that contains the code for the GUI and water jug logic.

## Dependencies

- **Tkinter**: Used to create the graphical user interface.
- **collections.deque**: Used for the queue structure in the BFS algorithm.
- **messagebox** and **filedialog** from Tkinter: Used for error handling and file saving.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to improving the project.

## License

This project is licensed under the MIT License.
