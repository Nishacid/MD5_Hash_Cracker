#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author            : Nishacid
# Python Version    : 3.*

import argparse
from cracker import *
from utils import *
import multiprocessing

if __name__ == "__main__":
    
    # Arguments
    parser = argparse.ArgumentParser(description="Password Cracker")
    parser.add_argument("-f", dest="file", help="Path of wordlist", required=False)
    parser.add_argument("-g", dest="generate", help="Generate MD5 hash of password", required=False)
    parser.add_argument("-md5", dest="md5", help="Hashed Password", required=False)
    parser.add_argument("-l", dest="pass_lenght", help="Password Lenght", required=False, type=int)
    parser.add_argument("-online", dest="online", help="Online Search", required=False, action="store_true")
    args = parser.parse_args()
    
    # MutliProcess
    work_queue = multiprocessing.Queue()
    done_queue = multiprocessing.Queue()
    cracker = Cracker()

    if args.md5:
        print("[*] Cracking hash " + args.md5)
        if args.file and not args.pass_lenght:
            print("[*] Using wordlist : " + args.file)
            
            # Process 1
            proc1 = multiprocessing.Process(target=Cracker.work, args=(work_queue, done_queue, args.md5, args.file, False))
            work_queue.put(cracker)
            proc1.start()
            
            # Process 2
            proc2 = multiprocessing.Process(target=Cracker.work, args=(work_queue, done_queue, args.md5, args.file, True))
            work_queue.put(cracker)
            proc2.start()
            
            while True:
                data = done_queue.get()    
                if data == "FOUND" or data == "NOT FOUND":
                    proc1.kill()
                    proc2.kill()
                    break
        elif args.pass_lenght and not args.file:
            print("[*] Using Incremental mode with " + str(args.pass_lenght) + " letters")
            Cracker.crack_incr(args.md5, args.pass_lenght)
        elif args.online:
            print("[*] Using Online mode")
            Cracker.crack_online(args.md5)
        else:
            print("[*] Please choose -f OR -l arguments")
    elif not args.generate:
        print(Colors.RED + "[-] Please provide a method and a hash [-h for help]" + Colors.END)
    
    if args.generate: 
        print(Colors.GREEN + "[+] MD5 of " + args.generate + " is " + hashlib.md5(args.generate.encode('utf8')).hexdigest() + Colors.END)