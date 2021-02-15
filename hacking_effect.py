# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:20:38 2021

# running this code in command prompt will give effect of hacking

"""

from time import sleep


import sys

string = """  I am Hacked your system
You are under my control
Get intro on Hacking
=====================

Hacking is the activity of identifying weaknesses in a computer system or a network to exploit 
the security to gain access to personal data or business data. An example of computer hacking can be: 
    using a password cracking algorithm to gain access to a computer system.

Computers have become mandatory to run a successful businesses. It is not enough to have isolated
 computers systems; they need to be networked to facilitate communication with external businesses.
 This exposes them to the outside world and hacking. System hacking means using computers to commit fraudulent acts 
 such as fraud, privacy invasion, stealing corporate/personal data, etc. Cyber crimes cost many organizations millions 
 of dollars every year. Businesses need to protect themselves against such attacks.
 
 
 Your system access is granted to me
 =============================================
 
 Now i am scanning your system.
 
 ==========================================
 
 A Hacker is a person who finds and exploits the weakness in computer systems and/or networks to gain access. 
 Hackers are usually skilled computer programmers with knowledge of computer security.

Types of Hackers
Hackers are classified according to the intent of their actions. The following list classifies types of hackers 

according to their intent:
    
Ethical Hacker (White hat): A security hacker who gains access to systems with a view to fix the identified weaknesses. 
They may also perform penetration Testing and vulnerability assessments.

Cracker (Black hat): A hacker who gains unauthorized access to computer systems for personal gain. The intent is usually
to steal corporate data, violate privacy rights, transfer funds from bank accounts etc.

Grey hat: A hacker who is in between ethical and black hat hackers. He/she breaks into computer systems without 
 authority with a view to identify weaknesses and reveal them to the system owner.
 
=====================================================================

Now your system in my control

=======================================================================
    
 
"""
for letter in string:
  sleep(0.01) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()
