# MD5 Hash Cracker

MD5 Hash cracker with 3 differents modes

    - Using a wordlist 
    - Using an incremental mode
    - Using an online mode 

Just for fun and python training, it's not really the best way to find an md5 hash ^^

## Installation

```
git clone https://github.com/Nishacid/MD5_Cracker.git
cd MD5_Cracker/
pip3 install -r requirements.txt
```

## Usage

```
usage: main.py [-h] [-f FILE] [-g GENERATE] [-md5 MD5] [-l PASS_LENGHT] [-online]

Password Cracker

optional arguments:
  -h, --help      show this help message and exit
  -f FILE         Path of wordlist
  -g GENERATE     Generate MD5 hash of password
  -md5 MD5        Hashed Password
  -l PASS_LENGHT  Password Lenght
  -online         Online Search
```

## Example 

### Generate a MD5 hash

```
python3 main.py -g abcd                                
[+] MD5 of abc is e2fc714c4727ee9395f324cd2e7f331f
```

### Cracking MD5 hash using a wordlist 

```
python3 main.py -md5 e2fc714c4727ee9395f324cd2e7f331f -f ./wordlist.txt                         
[*] Cracking hash e2fc714c4727ee9395f324cd2e7f331f
[*] Using wordlist : ./wordlist.txt
[+] Password found : abcd
[+] Found in 3 milisecondes.
```

### Cracking MD5 hash using incremental mode 

```
python3 main.py -md5 e2fc714c4727ee9395f324cd2e7f331f -l 3
[*] Cracking hash e2fc714c4727ee9395f324cd2e7f331f
[*] Using Incremental mode with 3 letters
[+] Password found : abcd
[+] Found in 1 milisecondes.
```

### Cracking MD5 hash using online mode ([md5decrypt.net](https://md5decrypt.net/))

```
python3 main.py -md5 e2fc714c4727ee9395f324cd2e7f331f -online
[*] Cracking hash e2fc714c4727ee9395f324cd2e7f331f
[*] Using Online mode 
[+] Password found : abcd
[+] Found in 391 milisecondes.
```