#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from time import sleep
from os import system
import socket    
import requests,re,os
from subprocess import call
import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)

print("""


                                 .'.                             ..                                 
                                ,l;                              .:,                                
                               :KNx.             CPS             .oXK:                               
                             .cXMMW0;                          ,kWMMXl.                             
                            .dNMMMMMNd'                      .oXMMMMMNd.                            
                            lNMMMMMMMWXd,                  .oKWMMMMMMMWo                            
                            ;KMMMMMMMMMMXx:.            .,dKWMMMMMMMMMK;                            
                            .dWMMMMMMMMMMMN0l'.       .ckNMMMMMMMMMMMWx.                            
                             ;XMMMMMMMMMMMMW0l,..  ..,cOWMMMMMMMMMMMMX:                             
                             .dWMMMMMMMMMWKl'......    .cOWMMMMMMMMMWk.                             
                              'OWMMMMMMMXx,. ........    .oKMMMMMMMMK;                              
                               :KMMMMMWKd:;;lxO0KKKKKk;  ;cc0WMMMMMXl                               
                               'oXMMMW0xkO0KK0OOkxddkXXdckKocOWMMMNx'                               
                               'cxNMMKlo0K0d,.......,oONX0KKdcOWMWOl'                               
                               .dxOWXolKMMM0,'oO0kxdllld0XK00dl0W0xd'                               
                               .o0k0xl0MMMWKxdkkOKKXNNK00KX0Okod0kOd.                               
                                ;KKolOWMMNOdxkOkkxkkOOKXNWWWXKkoo0X:                                
                                .OW0OWMMMKooKXKKXXNNNNNNWWMMMW0xONO'                                
                                 oWMMMMMMKdxXWWNXKKKKXNWMMMMMM0OWWd.                                
                                 ;KMMMMMM0oclkKNWMMMWNNWMMMMMMKONX;                                 
                                 .xWMMMMM0olc,,cdO0KNMMMMMMMMMXOKx.                                 
                                  :XMMMMMNdc;. .,d0XWMMMMMMMMMWOd,                                  
                                  .kMMMMMMXd'    ,lxXWMMMMMMMMMK:                                   
                                   cNMMMMMWk.    .;cokNMMMMMMMMNl                                   
                                   .OMMMMMXc.    .';lo0WMMMMMMMMk.                                  
                                    cNMMMWx.      .,llkNMMMMMMMMX;                                  
                                    .xWMMX:        .clxNMMMMMMMMWo                                  
                                     ;KMWx.        .:lxXMMMMMMMMMk.                                 
                                     .dNK;          'cdKMMMMMMMMMK,                                 
                                      ,ko.           'cxXMMMMMMMW0;                                 
                                      .;.             .:dKWMMMMNOc.                                 
                                                       .,lxOKK0x:.                                  
                                                         .;llll,                                    
                                                           .:c'                                     
                                                             .                        



""")
time.sleep(5)
call(["python", "Cam-info.py"])
