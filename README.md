<img src="screenshots/Banner.jpg" alt="Game Banner" style="width: 100%; height: auto; max-width: 890px; margin: 0 auto; display: block;">

# Meteor Dash: A Pygame Adventure
**Meteor Dash** is a fast-paced 2D survival game developed using Python's Pygame library. Players control a UFO to dodge meteors and survive for 40 seconds to claim victory.

![Python](https://img.shields.io/badge/Python-3.13.1-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green)
![VSCode](https://img.shields.io/badge/VSCode-1.96.2-blue)
![Git](https://img.shields.io/badge/Git-2.39.5-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 🔗 Repository Link
Access the repository here: [Meteor Dash GitHub Repository](https://github.com/jckangsfw/meteor-dash)

---

## 📖 Table of Contents
- [🎯 Overview](#-overview)
- [📂 Repository Structure](#-repository-structure)
- [✨ Features](#-features)
- [🛠️ Tools and Setup](#️-tools-and-setup)
- [🚀 How to Run](#-how-to-run)
- [🎮 Gameplay Mechanics](#-gameplay-mechanics)
- [🖼️ Screenshots](#️-screenshots)
- [🤝 Contributions](#-contributions)
- [📜 License](#-license)

---

## 🎯 Overview
Welcome to **Meteor Dash**, a project combining interactive gameplay with practical programming concepts. This project:
- Showcases my **learning and experimenting journey** with Python and the Pygame library.
- Combines **creativity with technical problem-solving** in a fun and interactive way.
- Serves as a milestone in exploring **2D game mechanics**, from object collisions to dynamic difficulty scaling.

---

## 📂 Repository Structure
The repository is organized into the following categories:

### ⚙️ Core Files (`src/`)
- **`main.py`**: The entry point of the game, handles the main game loop and logic.
- **`Player.py`**: Defines the UFO's movement and interactions.
- **`Meteor.py`**: Manages meteor spawning, movement, and collision logic.

### 📸 Screenshots
- `screenshots/Banner.jpg`: Game banner.
- `screenshots/Gameplay.gif`: Gameplay preview.
- `screenshots/Start Screen.png`: Start screen.

### 📦 Assets
  - 🎨 **Graphics**:
  - `graphics/Icon.png`: Application icon for the taskbar.
  - `graphics/Background Image.png`: Background image for the game.
  - `graphics/Meteor.png`: Sprite for meteors.
  - 🎧 **Audio**:
  - `audio/BGM.mp3`: Looping background music.
  - `audio/Lose SFX.mp3`: Game over sound effect.
  - `audio/Slide SFX.mp3`: UFO sliding sound effect.

### 🗂️ Others
- `README.md`: This file.
- `LICENSE`: Repository license information.

---

## ✨ Features
- **Progressive Difficulty**: Meteors spawn faster as the game progresses.
- **Intuitive Controls**: Use arrow keys for smooth navigation.
- **Audio Integration**: Background music and sound effects to enhance immersion.
- **Winning Condition**: Survive 40 seconds to win the game.

---

## 🛠️ Tools and Setup
To work with this repository, you'll need:
- **Python 3.13.1+**: [Download Python](https://www.python.org/downloads/)
- **Pygame 2.6.1+**: Install via pip:
  ```bash
  pip install pygame
  ```
- **Integrated Development Environment (IDE)**: Recommended: [VSCode](https://code.visualstudio.com/)
- **Git**: [Download Git](https://git-scm.com/)

---

## 🚀 How to Run
Follow these steps to run the game:
1. Clone the repository:
   ```bash
   git clone https://github.com/jckangsfw/Meteor-Dash.git
   ```
2. Ensure you have the required tools installed:
   - Python (3.13.1+)
   - A compatible IDE (e.g., VSCode)
   - Git
3. Open the project in your IDE.
4. Install Pygame:
   ```bash
   pip install pygame
   ```
5. Navigate to the src/ folder and run the main script:
   ```bash
   cd src
   python main.py
   ```

---

## 🎮 Gameplay Mechanics
- **Objective**: Survive for 40 seconds while dodging falling meteors.
- **Controls**:
  - Left Arrow: Move UFO left.
  - Right Arrow: Move UFO right.
  - Spacebar: Pause and resume the game.
- **Progressive Difficulty**: Meteor spawn frequency increases by 2.5% every 2 seconds, with decreasing intervals over time.
- **Game Over**: Colliding with a meteor ends the game.

---

## 🖼️ Screenshots
Start Screen:
<img src="screenshots/Start Screen.png" alt="Start Screen" style="width: 100%; height: auto; max-width: 890px; margin: 0 auto; display: block;">

Gameplay Preview:
<img src="screenshots/Gameplay.gif" alt="Gameplay Preview" style="width: 100%; height: auto; max-width: 890px; margin: 0 auto; display: block;">

---

## 🤝 Contributions
Contributions are welcome to enhance the game or add new features. To contribute:
1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add feature: Description"
   ```
4. Push the branch and open a pull request:
   ```bash
   git push origin feature/YourFeatureName
   ```

---

## 📜 License
This repository is licensed under the [MIT License](LICENSE). You may use, modify, and distribute the code if proper attribution is provided.
