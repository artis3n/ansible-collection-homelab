from passlib.hash import argon2
import argparse

parser = argparse.ArgumentParser("passgen")
parser.add_argument("input", help="Data to hash with argon2", type=str)
args = parser.parse_args()

print(argon2.hash(args.input), end='')
