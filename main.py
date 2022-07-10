#!/usr/sbin/python

from window import Window
import curses


def main():
    mainWin = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    window = Window(mainWin)
    h = 20
    w = 100
    y = 1
    x = 1

    while True:
        key = window.rootWin.getch()
        if key == ord('q'):
            curses.endwin()
            break
        if key == ord('o'):
            window.new_window(h, w, y, x, None)
            y += 1
            x += 1
        if key == ord('n'):
            window.next_window()
        if key == ord('p'):
            window.prev_window()
        if key == ord('i'):
            window.new_item("hello item({}, {})".format(x, y))
        if key == ord('j'):
            window.next_item()
        if key == ord('k'):
            window.prev_item()

main()
# curses.wrapper(main)
