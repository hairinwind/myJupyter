import sys, getopt

def main(argv):
    # getopt.getopt(args, shortopts, longopts=[])
    # https://docs.python.org/3.1/library/getopt.html
    optlist, args = getopt.getopt(argv, 'abc:d:x', ['condition=', 'output-file=', 'testing'])
    print(optlist)
    print(args)

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])
    # python commandline.py -a -b -cfoo -d bar a1 a2
    
    # long option names
    # python commandline.py -a -b -cfoo -d bar --condition=c1 --testing --output-file abc.def -x a1 a2