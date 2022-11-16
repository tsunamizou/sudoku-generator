import numpy as np

n = 9

#the percentage of blanks
percentage = 0.5


while True:
  # generate the array base
  base = np.zeros((n,n),dtype=int)
  rg = np.arange(1,n+1)

  # generate the first row 
  base[0,:] = np.random.choice(rg,n,replace=False)
  try:
    for r in range(1,n):
      for c in range(n):

        #Return the unique values in 1-9 that are not in the rest of the column/row
        # [a:b], a is inclusive, b is exclusive

        c_rest = np.setdiff1d(rg, base[:r,c])
        r_rest = np.setdiff1d(rg, base[r,:c])

        #return the available numbers based on column and row
        available1 = np.intersect1d(c_rest, r_rest)

        #return the available numbers based on the 3*3 grid
        #get the subordinates of the top left number in the 3*3 grid
        sub_r = r//3*3
        sub_c = c//3*3

        #use .ravel() to convert the 3*3 grid into a contiguous flattened array
        available2 = np.setdiff1d(np.arange(1,n+1), base[sub_r:(sub_r+3), sub_c:(sub_c+3)].ravel())

        #get the intersection of available1 and available2 and assign a random number to the base[r,c]
        available = np.intersect1d(available1, available2)
        base[r,c] = np.random.choice(available)
    break
  except ValueError:
    #valueerror happens when available is an empty list, meaning we have to start all over again
    pass



puzzle = base.copy()

#apply a boolean mask to the answer, true=0, false=orginal number
mask = np.random.choice([True, False], size=puzzle.shape, p=[percentage, 1-percentage])
puzzle[mask]=0
print(puzzle)

show = input("Do you want to show the answer? (Y/N)")
if show.upper() == "Y":
  print(base)
else:
  pass
