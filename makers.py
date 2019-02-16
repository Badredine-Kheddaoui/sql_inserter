from random import *

''':returns the number of lines in a file'''
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


'''returns a random file from a wordlist'''
def getLine(wordlist):
    input_file = open(wordlist, 'r')
    random_int = randrange(0, file_len(wordlist) - 3)
    s = ''
    for i, line in enumerate(input_file):
        if i == 0:
            i = random_int
            continue
        if i > random_int:
            s = input_file.readline()
            s = s[:len(s) - 1]
            break
    return s


def make_varchar(output_file, wordlist):
    s = getLine(wordlist)
    if s[0] != '\'':
        s = '\'' + s
    if s[len(s) - 1] != '\'':
        s += '\''
    print(f'{s}', file=output_file, end='')


def make_number(output_file, wordlist):
    # if no wordlist was specified then make a random number
    if wordlist == 'randomWords.txt':
        random_int = randrange(1236, 9932)
    else:
        random_int = getLine(wordlist)
    print(f'{random_int}', file=output_file, end='')


def make_float(output_file, wordlist):
    # if no wordlist was specified then make a random float
    if wordlist == 'randomWords.txt':
        random_float = round(random.uniform(1236, 9932), 2)
    else:
        random_float = format(float(getLine(wordlist)),'.2f')
    print(f'{random_float}', file=output_file, end='')


def make_column(output_file, column_type='varchar', wordlist='randomWords.txt'):
    if column_type == 'varchar':
        make_varchar(output_file, wordlist)
        return

    elif column_type == 'number':
        make_number(output_file, wordlist)
        return

    elif column_type == 'float':
        make_float(output_file, wordlist)
        return