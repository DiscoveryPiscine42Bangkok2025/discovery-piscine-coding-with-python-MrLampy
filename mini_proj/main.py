#!/usr/bin/env python
from checkmate import checkmate
def main():
    board = """\
.....
.....
..Q.B
.....
KP..R\
""" 
    checkmate(board)
if __name__ == "__main__":
    main()