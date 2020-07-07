from SudokuGrid import  SudokuGrid

question = [list("5  91372 "),
            list("3   8 5 9"),
            list(" 9 25  8 "),
            list("68 47 23 "),
            list("  95  46 "),
            list("7 4     5"),
            list(" 2       "),
            list("4  8916  "),
            list("85 72   3")]


sg = SudokuGrid()

# !!!!!!! Change to load method
sg.grid = question.copy()
# !!!!!!! Change to load method


# guesses - when the next step is not clear and there are multiple options, the main process
# will bak up the current grid to guesses.
# It will also keep some other stuff, all in the guesses list, in each row:
# [0] x
# [1] y
# [2] list of available options for this coordinate
# [3] current guess index in [2]
# [4] a backup of the grid before the current guess
#
# each row in this list can have only unique coordinates
# when all guesses in a coordinate are proven bad, the record is poped out and the -1 record is evaluated.
# if  guesses runs out of records, the question is wrong



guesses = []



print( sg.grid)

it =0

while it<500:
    splist = sg.space_list()
    if len(splist)==0:
        print("Solved!")
        break
    elif len(splist[0][0]) == 1:
        for space in splist:
            #print("#########################")
            #print(space)
            if len(space[0]) == 1:
                sg.grid[space[2]][space[1]] = space[0][0]
                sg.log.append("Adding number at (x,y) "+str(space[1])+" "+str(space[2])+ " \n")
    elif len(splist[0][0]) == 0: # error or bad guess
        endloopp=0
        while endloopp==0:
            options = guesses[-1][2]
            bad_guess = guesses[-1][3]
            xx = guesses[-1][0]
            yy = guesses[-1][1]
            grid_from_backup = guesses[-1][4].copy()
            if len(options) == bad_guess+1:
                sg.grid = grid_from_backup
                guesses.pop()
                #wait for the next loop
            else:
                sg.log.append("Guessing at (x,y) " + str(xx)+ " " + str(yy)+ " \n")
                sg.grid = guesses[-1][4].copy()
                guesses[-1][3] = bad_guess + 1
                sg.grid[yy][xx] = guesses[-1][2][bad_guess+1]
                endloopp=1

            if  len(guesses) == 0:
                print("This question has no answer!")
                sg.log.append("This question has no answer!")
                break


    else:
        #print("---------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #print("Guessing at (x,y) ", splist[0])
        sg.log.append("Guessing at (x,y) " + str(splist[0][1]) + " " + str(splist[0][2])+ " \n")
        # As the first space is not 0 or 1, we have to guess this coordinate.
        # This is the first guess iteration for this coordinate so [3] = 0
        # [0] x
        # [1] y
        # [2] list of available options for this coordinate
        # [3] current guess index in [2]
        # [4] a backup of the grid before the current guess
        guesses.append([splist[0][1], splist[0][2], splist[0][0][0], 0, sg.grid.copy()])
        sg.grid[splist[0][2]][splist[0][1]] = splist[0][0][0]

    #Print
    print("-----------",str(it),"------------")
    for lin in sg.grid:
        print(lin)
    for lin in sg.log:
        print(lin)

    it +=1

if it==500:
    print("Too difficult for me!")

#for lin in sg.log:
#    print(lin)

#print(splist)


#splist = sg.space_list()
#print(len(splist))
#print(splist)

#print( sg.grid)
#print (sg.posibilities(7,1))
