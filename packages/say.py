import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.draw("hello world", sys.argv[1])