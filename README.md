Two-Point Perspective Projection of 3D Figures Using OpenGL

Overview
This project showcases a Python application that visualizes 3D figures—tetrahedron, hexahedron, and octahedron—using two-point perspective projection in OpenGL. Users can select a figure from the main menu and rotate it using mouse controls for detailed viewing. The project emphasizes the fundamentals of 3D graphics, perspective projection, and interactive user interfaces.

Table of Contents
Project Details
Technologies Used
Project Structure
Setup Instructions
Features
Conclusion
Project Details

The primary objective is to implement a two-point perspective projection for three-dimensional figures, providing realistic visual depth. Key objectives include:

Developing an interactive main menu to select a 3D figure.
Displaying wireframe models of selected figures with perspective effects.
Enabling real-time rotation of figures using mouse interaction.
Optimizing rendering functions for smooth transitions between menu and figure display.
Technologies Used
Programming Language: Python
Development Environment: PyCharm Community Edition
Graphics Libraries:
OpenGL (PyOpenGL)```markdown
# Two-Point Perspective Projection of 3D Figures Using OpenGL

This project showcases a Python application that visualizes 3D figures—tetrahedron, hexahedron, and octahedron—using two-point perspective projection in OpenGL. Users can select a figure from the main menu and rotate it using mouse controls for detailed viewing. The project emphasizes the fundamentals of 3D graphics, perspective projection, and interactive user interfaces.

## Table of Contents

- [Project Details](#project-details)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Features](#features)
- [Conclusion](#conclusion)

## Project Details

The primary objective is to implement a two-point perspective projection for three-dimensional figures, providing realistic visual depth. Key objectives include:

- Developing an interactive main menu to select a 3D figure.
- Displaying wireframe models of selected figures with perspective effects.
- Enabling real-time rotation of figures using mouse interaction.
- Optimizing rendering functions for smooth transitions between menu and figure display.

## Technologies Used

- **Programming Language:** Python
- **Development Environment:** PyCharm Community Edition
- **Graphics Libraries:** OpenGL (PyOpenGL), Pygame (for window creation and input handling)

## Project Structure

The repository is organized as follows:

```
├── main.py             # Main script for menu and figure display
├── figures.py          # Module defining 3D figure geometry
├── buttons.py          # Button rendering functions for the menu
├── render_text.py      # Text rendering functions
├── render_figure.py    # Functions for figure display and interaction
└── README.md           # Project documentation
```

## Setup Instructions

To set up this project locally:

### Prerequisites

- Python 3.x (installable from [python.org](https://www.python.org))
- PyCharm (optional but recommended for development)

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Nissmoline/pythonProject.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd pythonProject
   ```
3. **Install dependencies:**
   ```bash
   pip install pygame PyOpenGL
   ```
4. **Run the application:**
   ```bash
   python main.py
   ```

## Features

- **3D Figures and Perspective Projection:** Renders a tetrahedron, hexahedron, and octahedron in wireframe using a two-point perspective.
- **Interactive Menu and Controls:** A main menu allows figure selection and displays a "Back" button. Real-time rotation of figures through mouse movements for enhanced visualization.
- **Structured and Modular Code:** Separate modules for figure definitions, rendering buttons, text, and figures improve maintainability.

