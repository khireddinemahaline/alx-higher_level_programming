def print_arg(*argv):
    x = len(argv)
    count = x + 1
    i = 0
    
    if x == 0:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
        while i < count:
                try:
                    print("{}: {}".format(i ,argv[i]))
                    i += 1
                except:
                    continue
    else:
        print("{} arguments:".format(x))
        while i < count:
                try:
                    print("{}: {}".format(i ,argv[i]))
                    i += 1
                except:
                    continue
