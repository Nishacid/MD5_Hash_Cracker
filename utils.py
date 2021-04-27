#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author            : Nishacid
# Python Version    : 3.*

# Class for colors
class Colors:
    RED  = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'
    
# Order Class for mutli processing 
class Order:
    ASCEND = True
    DESCEND = False
    
# Time format
def time_format(delta_t, units = ["heures","minutes","secondes","milisecondes"]):
    out = ""
    if delta_t // 3600 != 0: # heures
        out = out + str(int(delta_t // 3600)) + " " + units[0]
        delta_t = delta_t % 3600
    if delta_t // 60 != 0: # minutes
        out = out + " " +  str(int(delta_t // 60)) + " " + units[1]
        delta_t = delta_t % 60
    if int(delta_t) != 0: # secondes
        out = out + " " + str(int(delta_t)) + " " + units[2]
        delta_t = delta_t - int(delta_t)
    if delta_t // 0.001 != 0: # milisecondes
        out = out + " " + str(int(delta_t//0.001)) + " " + units[3]
    if len(out) == 0:
        out = "0 "+units[3]
    out = out + "."
    if out.startswith(" "):
        out = out[1:]
    return out