# TODO: check documentation
# https://docs.python.org/3/library/argparse.html
# TODO:enhance with this example
# https://github.com/pypa/twine/blob/main/twine/cli.py
import argparse
import sys

parser = argparse.ArgumentParser(description="sum the integers at the command line")
parser.add_argument(
    "integers", metavar="int", nargs="+", type=int, help="an integer to be summed"
)
parser.add_argument(
    "--log",
    default=sys.stdout,
    type=argparse.FileType("w"),
    help="the file where the sum should be written",
)
args = parser.parse_args()
args.log.write("%s" % sum(args.integers))
args.log.close()
