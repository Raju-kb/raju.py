theBoard = {'top-L':'','top-m':'','top-r':'',
            'mid-l':'','mid-m':'','mid-r':"",
            'low-l':'','low-m':'','low-r':""
            }

def printBoard(board):
    print(board['top-L']+ '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l']+ '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l']+ '|' + board['low-m'] + '|' + board['low-r'])
turn = 'x'
for i in range(9):
    printBoard(theBoard)
    print('turn for ' + turn + '-move on which space')
    move = input()
    theBoard[move] = turn
    if turn == 'x':
        turn = '0'
    else:
        turn = 'x'
printBoard(theBoard)
