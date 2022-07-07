#!/usr/sbin/python

from window import Window
import curses


def main(debugWin):
    window = Window(debugWin)
    h = 20
    w = 100
    y = 1
    x = 1

    while True:
        key = window.rootWin.getch()
        if key == ord('q'):
            break
        if key == ord('o'):
            window.new_window(h, w, y, x, None)
            y += 1
            x += 1
        if key == ord('n'):
            window.next_window()
            y += 1
            x += 1
        if key == ord('p'):
            window.prev_window()
            y -= 1
            x -= 1
        if key == ord('i'):
            window.set_item("hello item({}, {})".format(x, y))



curses.wrapper(main)
