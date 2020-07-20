import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('square', help='get the squared number', type=int)
args = parser.parse_args()
print(args.square**2)
