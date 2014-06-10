import cmdline

print("\n----- cmdline module -----\n")
print('* ' + '\n* '.join(dir(cmdline)))

print("\n----- parse_args() document -----\n")
print(cmdline.parse_args.__doc__)
