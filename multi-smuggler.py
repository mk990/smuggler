import concurrent.futures
import logging
import threading
import time
import argparse
import os
import time
import sys
global Args

def thread_function(line):
    os.system(Args.bin+ "-x -c "+Args.config+" -u "+line.replace("\n",""))

if __name__ == "__main__":

    Parser = argparse.ArgumentParser()
    Parser.add_argument('-l', '--list', help="URL Lists")
    Parser.add_argument('-w', '--worker', default=5.0, help="Workers. Default: 5")
    Parser.add_argument('-c', '--config', default="default.py", help="Filepath to the configuration file of payloads")
    Parser.add_argument('-b', '--bin', default="smuggler", help="Filepath to the configuration file of payloads")
    Args = Parser.parse_args()
#    global Args
    workers=int(Args.worker)
    print(workers)
    if not Args.list or not os.path.isfile(Args.list):
        if sys.stdin.isatty():
                print("No URLs.")
                exit(1)
        else:
                lines=sys.stdin.read().split("\n")
    else:
        lines=open(Args.list,'r')
#    for line in lines:
#    format = "%(asctime)s: %(message)s"
 #   logging.basicConfig(format=format, level=logging.INFO,
#                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(thread_function, lines)



