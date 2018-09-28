# Make-HtDigest

make-htdigest is a tool to create an Apache/Wildfly/JBOSS file for Digest Authentication for Lookup / Brute Force passwords.

### Prerequisites

Python 2.7.x +

### Usage

make-htdigest.py -u \<username\> -r \<realm\> -f \<wordlist>

### High Level Description on how it works:

Wildfly stores username/password in the file mgmt-users.properties as well Apache using HTTP Digest Authentication in the .htdigest file
Password is saved using HTTP Digest Authentication based on the RFC 2617 in the following format:<br>
   md5(username:realm:password)<br>
<br>
This tool creates entries for a username with different passwords based on a wordlist. It can be used for passwod lookup during assessment/pentesting/auditing<br>
<br>
Output file name has the following format:<br>
\<username\>:\<realm\>.txt<br>
  e.g admin:ManagementRealm.txt<br>
<br>
 Example - Wildfly mgmt-users.properties<br>
 admin:5ea41921c65387d904834f8403185412<br>
<br>
 Example - Apache password files (.htdigest)<br>
 user1:Realm:5ea41921c65387d904834f8403185412<br>
<br>
### Authors

* **Ismael Goncalves** -  [Sharingsec](https://sharingsec.blogspot.com)

