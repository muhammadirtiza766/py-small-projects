import os

usr_input = int(input("Enter your Desire Range $ "))


def estimate_pi(terms):
    result = 0.0
    for n in range(terms):
        result += (-1.0)**n/(2.0*n+1.0)
    return 4*result

for term in range(0, usr_input+1):
  os.system('cls' if os.name == 'nt' else 'clear')
  i = term
  print(estimate_pi(i))