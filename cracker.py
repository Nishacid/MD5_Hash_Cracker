#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author            : Nishacid
# Python Version    : 3.*

import requests
import sys
import time
import string
import hashlib
from bs4 import BeautifulSoup
from utils import *

class Cracker:
        
    # Dictionnary Bruteforce Fonction
    @staticmethod
    def crack_dict(md5, file, order, done_queue):
        try:
            start = time.time()
            found = False
            wordlist = open(file, "r")
            if Order.ASCEND == order:
                content = reversed(list(wordlist.readlines()))
            else:
                content = wordlist.readlines()
            for words in content:
                words = words.strip("\n")
                file_hashs = hashlib.md5(words.encode("utf8")).hexdigest()
                
                if md5 == file_hashs:
                    found = True
                    print(Colors.GREEN + "[+] Password found : " + words + Colors.END)
                    print(Colors.GREEN + "[+] Found in " + time_format(time.time() - start) + Colors.END)
                    done_queue.put("FOUND")
                    break
            if not found:
                    print(Colors.RED + "[-] Bad wordlist, password not found" + Colors.END)
                    done_queue.put("NOT FOUND")
            
            wordlist.close()
        except FileNotFoundError:
            print(Colors.RED + "[-] File not found" + Colors.END)
            sys.exit(1)
            
        except Exception as err: 
            print(Colors.RED + "[-] Error : " + str(err) + Colors.END)
            sys.exit(2)

    # Incrementation Fonction
    @staticmethod
    def crack_incr(md5, lenght, _currpass=[]):
        start = time.time()
        letters = string.ascii_letters
        if lenght >= 1:
            if len(_currpass) == 0:
                _currpass = ['a' for i in range(lenght)]
                Cracker.crack_incr(md5, lenght, _currpass)
            else: 
                for carac in letters:
                    _currpass[lenght -1] = carac
                    if hashlib.md5("".join(_currpass).encode("utf8")).hexdigest() == md5:
                        print(Colors.GREEN + "[+] Password found : " + "".join(_currpass) + Colors.END)
                        print(Colors.GREEN + "[+] Found in " + time_format(time.time() - start) + Colors.END)
                        break
                    else:
                        Cracker.crack_incr(md5, lenght -1, _currpass)
        
    # Online Fonction
    @staticmethod                  
    def crack_online(md5):
        try:  
            start = time.time()
            url = 'https://md5decrypt.net/'
            data = {
                'hash': md5,
                'captcha6866': '',
                'ahah6866': '1c755dae9828b491df95ea770206b494',
                'decrypt': 'D%C3%A9crypter'
            }
            headers = {
                    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
                    'Content-Type' : 'application/x-www-form-urlencoded',
                    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9;image/webp,*/*;q=0.8',
                    'DNT' : '1',
                    'Host' : 'md5decrypt.net'
            }
            r = requests.post(url = url, data = data, headers = headers)
            if r.status_code == 200:
                soup = BeautifulSoup(r.content.decode('utf-8'),'lxml')
                for element in soup.find_all('b') :
                    print(Colors.GREEN + "[+] Password found : " + element.text.strip() + Colors.END)
                    print(Colors.GREEN + "[+] Found in " + time_format(time.time() - start) + Colors.END)
                if not soup.find_all('b'):
                    print(Colors.RED + "[-] Password not found" + Colors.END)
            else: 
                print('Error : ' + str(r.status_code()))
        except requests.ConnectionError:
            print("Error, failed to etablish connection on : " + url)
        except requests.Timeout:
            print("Error, request time out")
               
    # Work Fonction
    @staticmethod        
    def work(work_queue, done_queue, md5, file, order):
        o = work_queue.get()
        o.crack_dict(md5, file, order, done_queue)