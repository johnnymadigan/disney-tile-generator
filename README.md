![unit](https://img.shields.io/badge/IFB104-Building%20IT%20Systems-ff69b4?style=plastic)
![author](https://img.shields.io/badge/Author-Johnny%20Madigan-yellow?style=plastic)
![year](https://img.shields.io/badge/Year-2019-lightgrey?style=plastic)
![python version](https://img.shields.io/badge/Python%20version-2.7%20|%203.8-informational?style=plastic&logo=python)
 
<p align="center">𝔍𝔬𝔥𝔫𝔫𝔶 𝔐𝔞𝔡𝔦𝔤𝔞𝔫 🐰</p>

- [About](#about)
- [How to run via the terminal](#how-to-run-via-the-terminal)
- [How to run via *Visual Studio Code*](#how-to-run-via-visual-studio-code)
- [Call Graph](#call-graph)
- [Dependencies](#dependencies)

# About
This project was my first *Python* assignment at the *Queensland University of Technology*. Using *Turtle Graphics*, the task requires us to design and easily reproduce complex visuals as tiles in a grid. Given a randomly generated pattern via nested lists, the program needs to read these instructions and populate the grid with these tiles accordingly. Tiles vary in size, design, with some broken.

![project running animation](/img/disney-project-eg.gif)

# How to run via the Terminal
- Launch your OS' terminal.
- Navigate to the project folder (*disney-project*) with the 'cd' command.
- Confirm you are in the project folder with the 'ls' command, you should see *main.py* among the files.

```zsh
foo@bar:~$ ls
README.md    goofy.py    main.py    ...
```

- Type 'python2 main.py' to launch the program.

```zsh
foo@bar:~$ python2 main.py
```

# How to run via *Visual Studio Code*
- Download *VScode*: https://code.visualstudio.com
- Follow the *Getting Started with Python* guide: https://code.visualstudio.com/docs/python/python-tutorial
- Launch *VScode*.
- Select *Python* Interpreter version 2.7 or 3.8.
- Open the project folder (*disney-project*) in *VScode*.
- Select *main.py* and click run.

![run button](/img/run-button.png)

# Call Graph

![pyan3 generated call graph](/img/disney-project-pyan3-call-graph.png)

# Dependencies
Relies on *Turtle Graphics* and therefore *tkinter*. If your *Python* Interpreter version supports *Tk* then you can use it to run the program. Versions 2.7 and 3.8 have been proven to work.
