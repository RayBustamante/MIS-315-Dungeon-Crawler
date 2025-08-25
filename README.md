# 🗡️ Turn-Based Strategy Mini-Game

A simple turn-based combat simulator inspired by classics like **World of Warcraft**, **Dungeons & Dragons**, **Castle Crashers**, **Darkest Dungeon**, and **Diablo**. Built as a solo project for learning and experimenting with core gameplay mechanics, this prototype focuses on combat while laying the groundwork for a dungeon-crawling experience.

> ⚠️ This project is for educational and demonstration purposes only. All third-party assets are used under fair use for non-commercial development.

---

## 🎮 Game Features

- **Turn-Based Combat System**  
- **Customizable Hero**: Start with **Richard the Lionheart**, or rename your hero  
- **Stat-Based Mechanics**: HP, Strength, Defense, and Tooltips  
- **Bounty Board**: Choose enemies and view their bounty values  
- **Save/Load System**: Automatically saves progress to a `.csv` file  
- **Battle Simulation**: Includes animations, music, sound effects, and two unique attacks  
- **Modular and Expandable Design** for future dungeon implementation

---

## 🛠️ How It Works

### 🔹 New Game Flow

1. Launch the program (no save file should exist on first run).
2. Click **New Game** to open the combat menu.
3. Your hero starts at:
   - **Level**: 1  
   - **HP**: 300  
   - **Strength**: 5  
   - **Defense**: 5  
4. Choose an enemy from the dropdown (currently only **Bandit** is available).
5. Combat screen appears with:
   - Custom background and enemy sprite  
   - Battle music and sound effects  
   - Two available attacks:  
     - **Slash Attack**  
     - **Bull Charge**

6. After each move, the enemy counters.
7. Upon defeating the enemy, a victory message appears.
8. The game generates a `.csv` file to save your hero's stats and closes.

### 🔹 Load Game Flow

- Relaunch the game and choose **Load Game**.
- The program reads the `.csv` file and restores your saved hero.

---

## 📁 Assets Disclaimer

This project uses third-party assets to enhance the experience:

| Asset Type | Source             | Note                        |
|------------|--------------------|-----------------------------|
| Art        | *Darkest Dungeon*  | Character & background art |
| Music/SFX  | *Castle Crashers*  | Battle music & sounds      |

> **I do not own or claim rights to these assets.** They are used solely for educational purposes and are not included for redistribution or commercial use.

---

## 📦 Dependencies

To run the game, make sure you have the following Python modules installed:

- [`csv`](https://docs.python.org/3/library/csv.html) *(standard library)*
- [`random`](https://docs.python.org/3/library/random.html) *(standard library)*
- [`winsound`](https://docs.python.org/3/library/winsound.html) *(Windows only)*
- [`pygame`](https://pypi.org/project/pygame/) *(fo*
