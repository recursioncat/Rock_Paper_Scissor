import time
import random
import keyboard

winning_moves = ["rs", "sp", "pr"]
losing_moves = ["sr", "ps", "rp"]
action_dict = {1: "r", 2:"p", 3: "s"}
def rps(x):
      response = action_dict[random.randint(1,3)]
      #print(response)
      output = x+response
      if output in winning_moves:
            return [1, response]
      elif output in losing_moves:
            return [0, response]
      return [2, response]


if __name__ == "__main__":
      user_points = 0
      pc_points = 0
      while True:
            val = None
            val=input("Enter Your Move: ")
            point=rps(val)
            if point[0] == 1:
                  user_points+=1
            elif point[0] == 0:
                  pc_points+=1
            print(f"Points: User - {user_points}, Pc - {pc_points}")
            print()

    