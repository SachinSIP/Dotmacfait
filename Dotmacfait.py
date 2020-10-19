#! /usr/bin/env python
#officially coded by Dot Intro
#uses python 2

import subprocess
import optparse
import re
#The module subprocess is used to type the input in the terminal 
#The module optparse is used to input the values in the terminal by the user using set of steps
#The module re is used for searching the current mac address
#Officially developed by Dotintro

def macfaitparse():
    parser=optparse.OptionParser()
    parser.add_option("-n","--ncard",dest="ncard",help="Type the network card name ")
    parser.add_option("-m","--mac",dest="fakemac",help="Type the fake mac id")
    (opts,args)=parser.parse_args()
    if not opts.ncard:
      parser.error("That's an error,man!!Please type the name of the network adapter")
    elif not opts.fakemac:
      parser.error("That's an error,man!!Please type the 12 digit MAC id with semicolons")
    return opts

def macfaitmain(ncard,fakemac):
  print("# Changing MAC id of  " + ncard + " to " + fakemac)
  subprocess.call(["ifconfig",ncard,"down"])
  subprocess.call(["ifconfig",ncard,"hw","ether",fakemac])
  subprocess.call(["ifconfig",ncard,"up"])
  
def currentmac(ncard):
  a=subprocess.check_output(["ifconfig",ncard])
  b=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",a)
  if b:
   return b.group(0)
  else: 
   print("Couldn't find a mac id")
print("Dotmacfait")
opts=macfaitparse()
current_mac=currentmac(opts.ncard)
print("Current mac:"+str(current_mac))
macfaitmain(opts.ncard,opts.fakemac)
print("New mac:"+opts.fakemac)

if current_mac!=opts.fakemac :
  print("# Mac address changed successfully")
