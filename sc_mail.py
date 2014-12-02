from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def send(_subj, _msg, _toaddr):
    msg = MIMEText(_msg)
    msg["To"] = _toaddr
    msg["From"] = "FysKams medlemsregister"
    msg["Subject"] = _subj
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())
