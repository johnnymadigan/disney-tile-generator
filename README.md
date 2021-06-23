![unit](https://img.shields.io/badge/IFB104-Building%20IT%20Systems-ff69b4?style=plastic)
![author](https://img.shields.io/badge/Author-Johnny%20Madigan-yellow?style=plastic)
![year](https://img.shields.io/badge/Year-2019-lightgrey?style=plastic)

                                   .x88888x.            x*8888x.:*8888: -"888;                                   
                                  :8**888888X.  :>     X   48888X/`8888H/`8888H
                                  f    `888888x./     X8x.  8888X  8888X  8888X;
                                 '       `*88888~     X8888 X8888  88888  88888;
                                  \.    .  `?)X.      '*888!X8888  X8888  X8888;
                                   `~=-^   X88> ~       `?8 `8888  X888X  X888X
                                          X8888  ~      ~"  '888"  X888   X888
                                          488888           !888;  !888;  !888;
                                  .xx.     88888X         888!   888!   888!
                                 '*8888.   '88888>       88"    88"    88"
                                   88888    '8888>        "~     "~     "~
                                   `8888>    `888                       
                                    "8888     8%           Johnny Madigan
                                     `"888x:-"    https://johnnymadigan.github.io/

- [What is this project?](#about)
- [How to run via the terminal](#how-to-run-via-the-terminal)
- [How to run via *Visual Studio Code*](#how-to-run-via-visual-studio-code)
- [Call Graph](#call-graph)
- [Dependencies](#dependencies)

# About
This project is my first *Python* assignment at the *Queensland University of Technology*. Using *Turtle Graphics*, the task requires us to design and easily reproduce complex visuals as tiles in a grid. Given a randomly generated pattern via nested lists, the program needs to read these instructions and populate the grid with these tiles accordingly. Tiles vary in size, design, with some broken.

![project running animation](/img/eg.gif)

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

![python version](/img/py-version.png)

- Open the project folder (*disney-project*) in *VScode*.
- Select *main.py* and click run.

![run button](/img/run-button.png)

# Call Graph

![pyan3 generated call graph](/img/pyan3-call-graph.png)

# Dependencies
Relies on *Turtle Graphics* and therefore *tkinter*. If your *Python* Interpreter version supports *Tk* then you can use it to run the program. Versions 2.7 and 3.8 have been proven to work.
