import argparse
import makers

'''handle the argument parsing'''
def args_parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('tableName',type=str, nargs=1,
                        help=' the table name')
    parser.add_argument('lines',type=int, nargs=1,
                        help='the number of lines')
    parser.add_argument('column',type=str, nargs='+',
                        help='names for the columns')

    args = parser.parse_args()
    return args


'''columns: the number of columns
table_types: a dictionary of column types(key=column number[1,2,3...], value=column type)
table_wordlists: a dictionary of column wordlists(key=column number[1,2,3...], value=column wordlist)
output_file: the file to print the insertions into'''
def make_line(columns, table_types, table_wordlists, output_file):
    for c in range(1, columns + 1):
        # if the column type has been specified
        if table_types.__contains__(c):
            # if a wordlist has been specified for the column
            if table_wordlists.__contains__(c):
                makers.make_column(output_file, table_types[c], table_wordlists[c])
            else:
                makers.make_column(output_file, table_types[c])
        else:
            makers.make_column(output_file)
        print('' if c == columns else ', ', file=output_file, end='')


def main():
    args = args_parse()
    table_types = dict()
    table_wordlists = dict()
    table_columns = ''
    # loop through the columns and get each one's name and, datatype and a custom wordlist if specified
    for i,c in enumerate(args.column):
        table_columns += args.column[i].split(',')[0] + ', '
        if len(args.column[i].split(',')) > 1:
            table_types[i + 1] = args.column[i].split(',')[1]
        if len(args.column[i].split(',')) > 2:
            table_wordlists[i + 1] = args.column[i].split(',')[2]

    table_columns = table_columns[:len(table_columns)-2]
    table_name = args.tableName[0]
    rows = args.lines[0]
    columns = len(args.column)

    output_file = open('lines.sql', 'wt')
    for r in range(rows):
        # every iteration prints a new insertion
        output_file.write(f'INSERT INTO {table_name}({table_columns}) VALUES(')
        make_line(columns, table_types, table_wordlists, output_file)
        print(');', file=output_file)
    output_file.close()


if __name__ == '__main__': main()
