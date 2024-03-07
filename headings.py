"""Convert Markdown headings to rst headings"""
import sys

underlines = {
    '######' : '°',
    '#####' : '+',
    '####' : '^',
    '###' : '~',
    '##' : '-',
    '#' : '=',
    }
    
def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    newlines = []
    for line in lines:
        if line.startswith('#'):
            prefix, heading = line.split(' ', maxsplit=1)
            newlines.append(heading)
            newlines.append(underlines[prefix] * (len(heading) - 1))
            newlines.append('\n')
        else:
            newlines.append(line)
    
    for newline in newlines:
        print(newline)
    with open(f'{filename}.rst', 'w', encoding='utf-8') as f:
        f.writelines(newlines)

if __name__ == '__main__':
    main(sys.argv[1])