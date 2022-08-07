from random import randint
def powerball():
  maxm=69
  maxj=5
  m=maxm
# create all numbers from 0 to m
  r= list(range(m+1))
# start with an empty result
  v = []


  for j in range(maxj):
        # get ith number from r...
      i=randint(1,m)
      n=r[i]
    # remove it from r...
      r[i:i+1]= []

      m=m-1
    # and append to the result
      v.append(n)
  power_ball = randint(1,26)
  v.append(f'Power_Ball: {power_ball}')
  return v

def run():
    done=0
    while not done:
      try: x = input('\npress Enter for Powerball picks (Q to quit). ')
      except EOFError:
        x = 'q'
      if x and (x[0] == 'q' or x[0] == 'Q'):
            done=1
            print('done')
      else:
            print(powerball())

# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module powerball imported.")
    print("To run, type: powerball.run()")
    print("To reload after changes to the source, type: reload(powerball)")
# end of lotto.py
