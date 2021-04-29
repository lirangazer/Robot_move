def check_grid(grid, board_size):
    numOfBolck = 0
    for i in grid:
       numOfBolck+=len(i)
    if(numOfBolck != (board_size * board_size)):
        print("there are missing info to solve the problem please fix and try again ")
    return

def main():
    input_file = open('files\input.txt','r')
    lines = input_file.read().splitlines()
    algorithem_type=lines[0]
    borad_size = int(lines[1])
    grid=[]
    currentBoard = 0
    count = 0
    for line in lines[2:]:
        grid.append(list(line))

    movement =['U','D','R','L']
    cost={'road': 1 , 'dirt_road' : 4}
    check_grid(grid ,borad_size)


if __name__ == '__main__':
    main()
