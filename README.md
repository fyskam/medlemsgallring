# medlemsgallring

En samling script för att gallra i medlemsregistret.

## Användning
```bash
$ python main.py
```

### Installation
```bash
$ git clone https://github.com/fyskam/medlemsgallring.git
```
Flytta `activate.php` till ett lämpligt ställe. Andra uppgifterna för mysqlservern i `activate.php`, `main.py`, `clean_members.py`, och eventuellt `create_hash.py`.

#### Konfigurera `sendmail`
Installera sendmail:
```bash
$ apt-get install sendmail mailutils
```
Skapa en ny auth-map med en ny auth-fil:
```bash
$ mkdir -m 700 /etc/mail/authinfo
$ cd /etc/mail/authinfo
$ echo 'AuthInfo: "U:root" "I:some.address@gmail.com" "P:myPassWord"' > gmail-auth
$ makemap hash gmail-auth < gmail-auth
```
Lägg till följande i `/etc/mail/sendmail.mc` före första `MAILER_DEFINITIONS`:
```
define(`SMART_HOST',`[smtp.gmail.com]')dnl
define(`RELAY_MAILER_ARGS', `TCP $h 587')dnl
define(`ESMTP_MAILER_ARGS', `TCP $h 587')dnl
define(`confAUTH_OPTIONS', `A p')dnl
TRUST_AUTH_MECH(`EXTERNAL DIGEST-MD5 CRAM-MD5 LOGIN PLAIN')dnl
define(`confAUTH_MECHANISMS', `EXTERNAL GSSAPI DIGEST-MD5 CRAM-MD5 LOGIN PLAIN')dnl
FEATURE(`authinfo',`hash -o /etc/mail/authinfo/gmail-auth.db')dnl
```
Bygg och starta om:
```bash
$ make -C /etc/mail
$ /etc/init.d/sendmail reload
```
