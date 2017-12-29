import argparse

parser = argparse.ArgumentParser( description= "This program is meant to be an example for positional arguments. Follow the position of the arguments while executing the scripts")

#Positional Arguments
parser.add_argument("arg_one", help="Help about first argument")
parser.add_argument("arg_two", help="Help about second argument, it takes int as argument type.", type=int)
parser.add_argument("arg_three", help="Help about third argument")

#Optional Arguments
parser.add_argument("-o1", "opt_arg_one", help="Help about first optional argument")
parser.add_argument("-o2", "opt_arg_two", help="Help about second optional argument, it takes int as argument type.", type=int)
parser.add_argument("-o3", "opt_arg_three", help="Help about third optional argument")


args = parser.parse_args()

print( args.arg_one )
print( args.arg_two )
print( args.arg_three )

print( args.opt_arg_one )
print( args.opt_arg_two )
print( args.opt_arg_three )
