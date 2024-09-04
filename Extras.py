import time

def scanPrint(str):
  
  for i in str:
    print(i, end="", flush=True)
    time.sleep(0.08)
  print("\n")
