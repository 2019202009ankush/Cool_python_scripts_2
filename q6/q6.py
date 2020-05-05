import random

import curses

from curses import textpad

def make_suitable_screen(stdscr):

    curses.init_color(curses.COLOR_BLACK, 0, 0, 0)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)

    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN)

    curses.curs_set(0)

    stdscr.nodelay(1)

    stdscr.timeout(200)

def make_frog_cordinate(python_snake, game_board):

    frog = None

    while frog is None:

        frog = [random.randint(game_board[0][0]+1, game_board[1][0]-1),random.randint(game_board[0][1]+1, game_board[1][1]-1)]

        if frog in python_snake:

            frog = None

    return frog

def print_score(stdscr, point,level):

    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    temp=level+0

    sh,sw = stdscr.getmaxyx()

    point_txt = "Point={}".format(point)

    level_txt = "level={}".format(level)

    # print(level_txt)
    yp=10

    stdscr.addstr(0, sw//2 - yp//2, point_txt, curses.color_pair(3))

    stdscr.addstr(0, (sw//2 - yp//2)+10, level_txt, curses.color_pair(5))

    stdscr.timeout(200-(20*temp))

    stdscr.refresh()

def main(stdscr):

    make_suitable_screen(stdscr)

    sh, sw = stdscr.getmaxyx()

    game_board = [[1,1], [sh-3, sw-3]]

    textpad.rectangle(stdscr, game_board[0][0], game_board[0][1], game_board[1][0], game_board[1][1])

    python_snake = [[sh//2, sw//2+1], [sh//2, sw//2], [sh//2, sw//2-1],[sh//2, sw//2-2]]

    #print(python_snake)

    direction = curses.KEY_UP

    for y, x in python_snake:

        stdscr.addstr(y, x, '$', curses.color_pair(1))

    frog = make_frog_cordinate(python_snake, game_board)

    stdscr.addstr(frog[0], frog[1], '^',curses.color_pair(2))

    point = 0

    level=1

    print_score(stdscr, point,level)

    while 1:

        key = stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:

            direction = key

        front = python_snake[0]

        if direction == curses.KEY_RIGHT:

            new_head = [front[0], front[1]+1]

        elif direction == curses.KEY_LEFT:

            new_head = [front[0], front[1]-1]

        if direction == curses.KEY_UP:

            new_head = [front[0]-1, front[1]]

        if direction == curses.KEY_DOWN:

            new_head = [front[0]+1, front[1]]

        python_snake.insert(0, new_head)
        #print(python_snake)

        stdscr.addstr(new_head[0], new_head[1], '$', curses.color_pair(1))

        if python_snake[0] == frog:

            frog = make_frog_cordinate(python_snake, game_board)

            stdscr.addstr(frog[0], frog[1], '^',curses.color_pair(2))

            point += 1

            if point % 3 == 0 :

                level+=1

            print_score(stdscr, point,level)

            if level == 10:

                string_ = "YOU WIN"

                stdscr.addstr(sh//2, sw//2-len(string_)//2, string_)

                stdscr.nodelay(0)

                stdscr.getch()

                exit()
        else:

            stdscr.addstr(python_snake[-1][0], python_snake[-1][1], ' ')

            python_snake.pop()

        if (python_snake[0][0] in [game_board[0][0], game_board[1][0]] or python_snake[0][1] in [game_board[0][1], game_board[1][1]] or python_snake[0] in python_snake[1:]):

            string_ = "Snake_Crashed"

            stdscr.addstr(sh//2, sw//2-len(string_)//2, string_)

            stdscr.nodelay(0)

            stdscr.getch()

            break

        stdscr.refresh()

    stdscr.getch()

curses.wrapper(main)

