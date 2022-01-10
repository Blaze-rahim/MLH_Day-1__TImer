import time
import winsound


t = int(input("Enter your time in seconds"))
var = t
for i in range(t):
    time.sleep(1)
    var -=1
    print(f"{var} seconds left!")
print ("Time OVER")

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)