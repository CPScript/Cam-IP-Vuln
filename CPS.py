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



                                                            ..                                                    .                                                            
                                                          .,:,        _________     ________       _____         .;,.                                                          
                                                         :dc;'        CCCCCCCCCC   PPPPPPPPPP     SSSSSSS        ';l;                                                         
                                                        :KWKl.       CC            PP       PP   SS              ,xXXc                                                        
                                                       cXMMMNd.      CC            PP       PP    SSSSSSS       :KWMMXl.                                                      
                                                     .oXMMMMMWk,     CC            PPPPPPPPPP           SS     .oXMMMMMNo.                                                     
                                                    .xNMMMMMMMMKl.   CC            PP                    SS    ;OWMMMMMMMWx.                                                    
                                                   ,OWMMMMMMMMMMWO;.  CCCCCCCCCC   PP              SSSSSSS   'dXMMMMMMMMMMWO,                                                   
                                                  :KMMMMMMMMMMMMMMNx;.     ==========================     .oKWMMMMMMMMMMMMMKc.                                                 
                                                 '0MMMMMMMMMMMMMMMMMXx;.           I tried <3           'oKWMMMMMMMMMMMMMMMM0'                                                 
                                                 .oNMMMMMMMMMMMMMMMMMMNkc.                           .,dKWMMMMMMMMMMMMMMMMMWd.                                                 
                                                  '0MMMMMMMMMMMMMMMMMMMMW0o'.                      .:kXWMMMMMMMMMMMMMMMMMMMK,                                                  
                                                   oNMMMMMMMMMMMMMMMMMMMMMWKx:.                 .,o0NMMMMMMMMMMMMMMMMMMMMMWo.                                                  
                                                   ,0MMMMMMMMMMMMMMMMMMMMMMMWXkc,..          .':dKWMMMMMMMMMMMMMMMMMMMMMMMK;                                                   
                                                   .dWMMMMMMMMMMMMMMMMMMMMMMMMNklc;'.     ..,clxXMMMMMMMMMMMMMMMMMMMMMMMMWx.                                                   
                                                    ;XMMMMMMMMMMMMMMMMMMMMMMW0o;''..........'',;lONMMMMMMMMMMMMMMMMMMMMMMXc                                                    
                                                    .dWMMMMMMMMMMMMMMMMMMMW0l'.                  .:kNMMMMMMMMMMMMMMMMMMMMO.                                                    
                                                     .kWMMMMMMMMMMMMMMMMWKo'.                      .:ONMMMMMMMMMMMMMMMMMK:                                                     
                                                      ,0MMMMMMMMMMMMMMMNk:..        ........        .,oXMMMMMMMMMMMMMMMNl                                                      
                                                      .cXMMMMMMMMMMMMMXo,,:.  .,coddxkkkOO0KOc.     ;;':0WMMMMMMMMMMMMWx.                                                      
                                                      .'oNMMMMMMMMMMWKo;;cc;:d0NWMMMMMMMMMWWMWO;   ,xxc';kWMMMMMMMMMMMO,.                                                      
                                                      .',xWMMMMMMMMWkxOO00KNWMMWWNXXXK00OkxkXWMNd..oNNkl,,xNMMMMMMMMMK:..                                                      
                                                      .;,;OMMMMMMMWO::k0KXXXKOkdlcccc:::;;:ld0WMWKooKWW0o,,xNMMMMMMMXl',.                                                      
                                                       ,o;:KMMMMMM0:':dkkxxxl..           .:lokXWMWOdONW0o,,kWMMMMMWd;l;                                                       
                                                       .dk;lNMMMMXc'cONMMWWWO'    ':c:,'.. .,cldONMMXkxKWKo,;OWMMMWk:dx.                                                       
                                                       .lKk:xWMMNd':ONMMMMMMNo..;kXWMMWNX0xl;;:cld0NMW0x0NKo':KMMM0cdKo.                                                       
                                                        ;0WkcOWMO,;kNMMMMMMMWklxKXXXNWWMMMMMWKOxdoodkKXKkOXKl'oNMXloXK;                                                        
                                                        .xWNdc0Xl,xNMMMMMMMN0OkxollodxkO0KNWMMMMMWNX0000OddOO:;0NdlKWk.                                                        
                                                         lNMXood;oNMMMMMMWKkxlcloddoolccccldk0XNWWWWMMMMWNKOOx:odc0MNo.                                                        
                                                         ;0MMKl'cKMMMMMMMXdccd0NMMMWWNXKK0OkxxkO0KXNWMMMMMMWOkd;;kWMK;                                                         
                                                         .xWMM0lOMMMMMMMM0c,cO0OOO0KXWMMMMMMMMWWWMMMMMMMMMMMKdkdxNMMk.                                                         
                                                          lNMMWWWMMMMMMMM0:c0WMWNK0OOkkkOKNWMMMMMMMMMMMMMMMMNdxNWMMNo                                                          
                                                          ,0MMMMMMMMMMMMMOlok0WMMMMMMWXK0OkO0XWMMMMMMMMMMMMMWkdNMMMK;                                                          
                                                          .dWMMMMMMMMMMMWkloccx0NWMMMMMMMMWNKKKXNMMMMMMMMMMMMOoKMMMk.                                                          
                                                           :XMMMMMMMMMMMNdclc:;cdk0XWMMMMMMMMMMWWMMMMMMMMMMMMKlOMMNc                                                           
                                                           .kMMMMMMMMMMMWxclllc;,:loxkO00KXNWMMMMMMMMMMMMMMMMXoxWMO.                                                           
                                                            cNMMMMMMMMMMMOcclll,...,:clodOKXWMMMMMMMMMMMMMMMMWxdNXc                                                            
                                                            'OMMMMMMMMMMMXo;cl:.   .'cdkKWMMMMMMMMMMMMMMMMMMMM0oOx.                                                            
                                                             lNMMMMMMMMMMMKc;c,      .;cxXMMMMMMMMMMMMMMMMMMMMNo:,                                                             
                                                             '0MMMMMMMMMMMMXd;.       ..,o0NMMMMMMMMMMMMMMMMMMWk,.                                                             
                                                             .oWMMMMMMMMMMMMXc         .,cldOKNWMMMMMMMMMMMMMMMK;                                                              
                                                              ,KMMMMMMMMMMMMk'          'lllldKWMMMMMMMMMMMMMMMWo.                                                             
                                                              .dWMMMMMMMMMMNc           .cllloOWMMMMMMMMMMMMMMMMO.                                                             
                                                               ;KMMMMMMMMMWk.           .:lllldKMMMMMMMMMMMMMMMMNc                                                             
                                                               .dWMMMMMMMMX:             ,lllloOWMMMMMMMMMMMMMMMWx.                                                            
                                                                ,0MMMMMMMWx.             .cllllkNMMMMMMMMMMMMMMMM0'                                                            
                                                                 lNMMMMMMX:              .:llllkNMMMMMMMMMMMMMMMMXc                                                            
                                                                 'kWMMMMWx.               ,llllkNMMMMMMMMMMMMMMMMWd.                                                           
                                                                 .cKMMMMK;                .clllkNMMMMMMMMMMMMMMMMMO.                                                           
                                                                  .dXMMWd.                 ;lllxXMMMMMMMMMMMMMMMMMK;                                                           
                                                                  .:OWMK;                  .;llo0WMMMMMMMMMMMMMMMMWd.                                                          
                                                                   'oKNo.                   .;lld0WMMMMMMMMMMMMMMMXo.                                                          
                                                                   .:xk,                     .,cld0WMMMMMMMMMMMMWKd;                                                           
                                                                    'c,.                       'clokXWMMMMMMMMMN0d:.                                                           
                                                                    .,.                         .;lldOXWMMMMMWKxo:.                                                            
                                                                                                  'clloxO0KK0xol;.                                                             
                                                                                                   .;clllllllll;.                                                              
                                                                                                     .:llllllc,                                                                
                                                                                                       'clll:.                                                                 
                                                                                                        .,c:.                                                                  
                                                                                                          .                                                                    
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               

""")
time.sleep(5)
call(["python", "Cam-info.py"])
