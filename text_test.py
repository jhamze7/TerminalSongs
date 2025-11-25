import time
import sys

trtn = r"""
___________    .__              .__       .__                             .__                    __  .__                            __  .__               
\__    ___/___ |  |   _______  _|__| _____|__| ____   ____   _______ __ __|  |   ____   ______ _/  |_|  |__   ____     ____ _____ _/  |_|__| ____   ____  
  |    |_/ __ \|  | _/ __ \  \/ /  |/  ___/  |/  _ \ /    \  \_  __ \  |  \  | _/ __ \ /  ___/ \   __\  |  \_/ __ \   /    \\__  \\   __\  |/  _ \ /    \ 
  |    |\  ___/|  |_\  ___/\   /|  |\___ \|  (  <_> )   |  \  |  | \/  |  /  |_\  ___/ \___ \   |  | |   Y  \  ___/  |   |  \/ __ \|  | |  (  <_> )   |  \
  |____| \___  >____/\___  >\_/ |__/____  >__|\____/|___|  /  |__|  |____/|____/\___  >____  >  |__| |___|  /\___  > |___|  (____  /__| |__|\____/|___|  /
             \/          \/             \/               \/                         \/     \/             \/     \/       \/     \/                    \/ 
"""

atw = r"""
   _____ __________ ________   ____ __________  ________    ______________ ______________  __      __________ __________.____     ________   
  /  _  \\______   \\_____  \ |    |   \      \ \______ \   \__    ___/   |   \_   _____/ /  \    /  \_____  \\______   \    |    \______ \  
 /  /_\  \|       _/ /   |   \|    |   /   |   \ |    |  \    |    | /    ~    \    __)_  \   \/\/   //   |   \|       _/    |     |    |  \ 
/    |    \    |   \/    |    \    |  /    |    \|    `   \   |    | \    Y    /        \  \        //    |    \    |   \    |___  |    `   \
\____|__  /____|_  /\_______  /______/\____|__  /_______  /   |____|  \___|_  /_______  /   \__/\  / \_______  /____|_  /_______ \/_______  /
        \/       \/         \/                \/        \/                  \/        \/         \/          \/       \/        \/        \/ 
"""

PAUSE_COL  = 60
PAUSE_TIME = 2

def clear():
    print("\033c", end="", flush=True)

def trtn_animation(text):
    lines = text.splitlines()
    max_width = max(len(line) for line in lines)
    padded = [line.ljust(max_width) for line in lines]

    speed = 0.03   # starting speed

    for col in range(max_width + 1):
        clear()

        # Draw current frame
        for line in padded:
            print(line[:col])

        # Pause at the special column
        if col == PAUSE_COL:
            time.sleep(PAUSE_TIME)
            speed = 0.015     # <-- just update speed here
                             #     next loop iteration will be faster

        time.sleep(speed)

i = 0
while i < 4:
    trtn_animation(trtn)
    time.sleep(0.1)
    clear()
    print(atw)
    time.sleep(2)
    i+=1