import asyncio
from concurrent.futures import ProcessPoolExecutor #this gives us pool of worker process
import time
import threading

def square(num):
    return num * num

async def main():
    loop = asyncio.get_running_loop() # this gets the event loop currently running in main()
    # we need loop because we will ask it to run the work in another process.
    with ProcessPoolExecutor() as pool: # creates a process pool, with block automatically cleanup the process when finished
        result = await loop.run_in_executor(
            pool, #where to run it
            square, #what function to run it
            5 #function argument
        )
        # For above line, read it as Event loop, run sqaure(5) using pool inside worker process, and give me result when ready


# daemon and non daemon threads
def monitoring():
   while True:
        print('Monitoring task ...')
        time.sleep(3)
        print('wake up after 3s')

print('main function done')
t = threading.Thread(target= monitoring, daemon= False)
t.start()

# After t.start():

# The new thread begins running monitoring().
# The main thread continues immediately.
# The main thread reaches the end of the file.
# The only remaining thread is a daemon thread.
# Python exits the entire process.
# The daemon thread is destroyed while it is sleeping.