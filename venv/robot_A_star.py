

def main():
    input_file = open('files\input.txt','r')
    lines = input_file.read().splitlines()
    algorithem_type=lines[0]
    borad_size = lines[1]
    grid = [list(lines[2]),list(lines[3]) ,list(lines[4])]
    


if __name__ == '__main__':
    main()