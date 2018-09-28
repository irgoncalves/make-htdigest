#!/usr/bin/python
#
# Make-HtDigest - creates an Apache/Wildfly/JBOSS file for Digest Authentication for Lookup / Brute Force passwords
# Author: Ismael Goncalves - https://sharingsec.blogspot.com
#
# Usage: make-htdigest.py -u <username> -r <realm> -f <wordlist>
#
# High-level description:
#
# Wildfly stores username/password in the file mgmt-users.properties as well Apache using HTTP Digest Authentication in the .htdigest file
# Password is saved using HTTP Digest Authentication based on the RFC 2617 in the following format:
# md5(username:realm:password)
#
# This tool creates entries for a username with different passwords based on a wordlist. It can be used for passwod lookup during assessment/pentesting/auditing
#
# Output file name has the following format:
# <username>:<realm>.txt
#   e.g admin:ManagementRealm.txt
#
#
# Example - Wildfly mgmt-users.properties
# admin:5ea41921c65387d904834f8403185412
#
# Example - Apache password files (.htdigest)
# user1:Realm:5ea41921c65387d904834f8403185412
#
# Pre-requisites: Python 2.7


import os,hashlib,sys,argparse

def parse_args():

    # Parsing CLI arguments
    sample = "Sample: python make-htdigest.py -u admin -r ManagementRealm -f wordlist.txt"
    parser = argparse.ArgumentParser(description='''Make-HtDigest - Generates an Apache/WildFly/JBOSS file for Digest Authentication for Lookup / Brute Force Password
    Written by: Ismael Goncalves - https://sharingsec.blogspot.com''', prog="make-htdigest", epilog=sample,formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-u", "--username", help="Username being audited", required=True)
    parser.add_argument("-r", "--realm", help="Realm in which the user belongs" , required=True)
    parser.add_argument("-f", "--wordlist", help="Wordlist with passwords", required=True)
    try:
       args = parser.parse_args()
    except:
       parser.print_help()
       sys.exit(0)
    return args

def gen_htdigest(args):

   usr_domain = args.username + ':' + args.realm + ':'
   filepath = args.username + ':' + args.realm + '.txt'
   fileoutput = open(filepath,'a+')
   with open(args.wordlist) as fp:
      line = fp.readline()
      cnt = 1
      dgst_md5 = hashlib.new('md5')
      dgst_md5.update(usr_domain + line.strip())
      print dgst_md5.hexdigest()
      fileoutput.write(usr_domain + line.strip() + ":" + dgst_md5.hexdigest() + '\n')
      while line:
         line = fp.readline()
         print line
         cnt += 1
         dgst_md5 = hashlib.new('md5')
         dgst_md5.update(usr_domain + line.strip())
         print dgst_md5.hexdigest()
         fileoutput.write(usr_domain + line.strip() + ":" + dgst_md5.hexdigest() + '\n')
   fileoutput.close()
   print 'Operation Concluded'

if __name__ == "__main__":
    args = parse_args()
    gen_htdigest(args)
