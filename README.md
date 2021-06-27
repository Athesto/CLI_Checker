# ⚡ CLI_Checker ⚡
 > A Holberton School checker tool to avoid using your browser to check manaully every task of your current project.

## How to install

clone the repo and run the instalation script
```console
$ git clone https://github.com/DiegoCol93/CLI_Checker
$ cd CLI_Checker
$ ./install.sh
$ checker
```
the program are going to ask for:
 - your holberton's __email__ (xxxx@holbertonshcool.com)
 - your __API__ key ([link][api_link])
   - it's in the __Intranet > Tools > Holberton's Intranet API key__
   - it's an HEX string of 32 chars ex. `123abc123abcdef99001122cdef12351`
 - your intranet's __password__ (it will be hidden so don't worry if you don't see the chars)

after finishing the credentials it will ask for storing credentials
 - note: it has problem so write «__yes__» in lowercase

## How to use
just run cecker in your terminal ant the checker terminal will start

```console
$ checker
CLI-Checker ⚡
```
Now that you are in the console, you has to select the project with `project <num>`.
The project's number is the last number of the url<br>

#### Example of use
Suppose that you want to check the project __0x00. C - Hello, World__<br>
The url is `https://intranet.hbtn.io/projects/212`<br>
So, the project's number is __212__
```console
CLI-@Checker ⚡$ project 212
0 - Preprocessor
1 - Compiler
2 - Assembler
3 - Name
4 - Hello, puts
5 - Hello, printf
6 - Size is not grandeur, and territory does not make a nation
7 - What happens when you type gcc main.c
8 - Intel
9 - UNIX is basically a simple operating system, but you have to be a genius to understand the simplicity

  ┌─ You may now run:
  │
  └─┬─ check <task number>
    ├ To check a specific task.
    │
    ├─ check Not implemented yet🤕, Sorry.
    ├ To check all tasks of current project.
    └─┐
      ├─ To check only task 2 you would run
      │
      └─ Example: check 2

CLI-@Checker ⚡$ check 1
Task 1 Compiler
Checking your code... 🎉
🔥 Check 0: Approved 🏆
⚡ Check 1: Approved 🔥
🤩 Check 2: Approved 🎊
🥂 Check 3: Approved 🔥
```

### Available commands
 - help: show help. `available` is misspelled
 - EOF: (Ctrl-D) finish the console
 - quit: finish the console (same as EOF)
 - project: select project
 - check: slect task


## Contributors
- [Diego Lopez][@DiegoCol93]
- [Wiston Venera][@wsvem]
- [Leonardo Valencia][@4ions]
- [Gustavo Mejía][@Athesto] (README)

<!--links-->
[api_link]: https://intranet.hbtn.io/dashboards/my_tools
[@Athesto]: https://github.com/Athesto
[@wsvem]: https://github.com/wisvem
[@4ions]: https://github.com/4ions
[@DiegoCol93]: https://github.com/DiegoCol93
