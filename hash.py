#!/usr/bin/python3

# Juliet Yu
# 04APR21
# SY401 Lab08

# Hashing program to detect changes


import sys, os, hashlib
from datetime import datetime

def main():
    # open the output file to write to
    out = open('output.txt', 'w')
    names = ['/dev', '/proc', '/run', '/sys', '/tmp', '/var/lib', '/var/run'] 

    # walking through the directories beginning from root
    for root, directories, fileNames in os.walk('/', topdown=False):
        for f in fileNames:
            f = os.path.join(root, f)
             
            # ignores the stated list of directories
            if f in names:
                pass

            else:
                try:
                    # returns date/time
                    current = datetime.now()
                    timestamp = current.strftime("%d/%m/%Y %H:%M:%S")
                    
                    hashy = hashlib.sha256()
                    byte = bytearray(128*1024)
                    mem = memoryview(byte)

                    with open(f, 'rb', buffering=0) as fd:
                        for n in iter(lambda : fd.readinto(mem), 0):
                            hashy.update(mem[:n])
                        h = hashy.hexdigest() 
                    
                    outString = 'Filename: '+f+'\n'+'Hash: '+h+'\n'+'Date & Time: '+timestamp+'\n\n'
                    # writes the final string to out file
                    out.write(outString)
                    
                except:
                    continue
    return
main() 



