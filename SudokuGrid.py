import math
import petl

class SudokuGrid:
    def __init__ (self, sizex=9, sizey=9, blockx=3, blocky=3, numbers="123456789"):
        # Is the block size and x,y the amount of digits in numbers, does it devide
        if len(numbers) == blockx * blocky and sizex % blockx ==0 and sizey % blocky == 0 \
                and len(numbers) == sizey and sizex == sizey :
            self.sizex = sizex
            self.sizey = sizey
            self.blockx = blockx
            self.blocky = blocky
            self.numbers = list(numbers)
            self.grid = []
            self.log = []
        else:
            print( "Wrong params")


    def posibilities (self, x, y):

        # Initiate pos to have all possible symbols and then remove the symbols that are in the row, column and block:
        pos = self.numbers.copy()
        # in y
        for ix in range(self.sizex):
            try:
                pos.remove(self.grid[y][ix])
            except ValueError:
                pass
        #print(pos)
        # in x
        for iy in range(self.sizey):
            try:
                pos.remove(self.grid[iy][x])
            except ValueError:
                pass
        #print(pos)
        # in block
        bx = math.floor(x / self.blockx)
        by = math.floor(y / self.blocky)
            # the following should be round (we checked it) just converting them to integers...
        dx = math.floor(self.sizex / self.blockx)
        dy = math.floor(self.sizey / self.blocky)
        #print (bx,by,dx,dy)
        for iy in range(by*dy , (by+1)*dy):
            #print (iy)
            for ix in range(bx * dx,(bx +1)* dx):
                #print(iy,ix)
                #print( self.grid[iy][ix])
                try:
                    pos.remove(self.grid[iy][ix])
                except ValueError:
                    pass
        #print(pos)
        return pos

    def space_list (self):
        list = []
        for y in range(self.sizey):
            ystr = self.grid[y]
            for x in range(self.sizex):
                if ystr[x] == " ":
                    #print(self.posibilities(x,y),x,y)
                    list.append([self.posibilities(x,y),x,y])
        list.sort()
        return  list
