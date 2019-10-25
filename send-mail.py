#!/usr/bin/env python
import smtplib
import email
import time
import MySQLdb

def main():
	try:
		db = MySQLdb.connect("__HOST__","__USER__","__PASS__","__DATABASE__")
		cur = db.cursor() 
		cur.execute("SELECT * FROM queue ORDER BY id asc LIMIT 1;")
		mail = cur.fetchone()
		if mail == None:
			return

		cur.execute("DELETE FROM queue WHERE id = "+str(mail[0])+";")
		cur.close()

		msg = email.message_from_string(mail[1])
		to = msg['X-Original-To']
		del msg['delivered-to']

		if to.find('@localhost') != -1:
				print '@localhost'
				return 1

		if to.find('@localhost.localdomain') != -1:
				print '@localhost.localdomain'
				return 1

		## You can specify your own rules for using different SMTP host
		## For example in this situation is used "from" as variable.

		if msg['from'] == "firstmail@yourdomain.ltd":
			# First option
			smtp = smtplib.SMTP('__HOST__', __PORT__)
			smtp.starttls()
			smtp.set_debuglevel(1)
			# Set login if necessary
			smtp.login('__USER__', '__PASS__')
			smtp.sendmail('__EMAIL_OF_RECIEVER__', to,msg.as_string())

		else:
			# Second option
			smtp = smtplib.SMTP('__HOST__', __PORT__)
			smtp.starttls()
			smtp.set_debuglevel(1)
			# Set login if necessary
			smtp.login('__USER__', '__PASS__')
			smtp.sendmail('__EMAIL_OF_RECIEVER__', to,msg.as_string())

	except Exception,e: 
		print 'X', time.ctime(time.time()), ': email od ', msg['from'],' | ', msg['subject'], '| NOT sent to ', to, e
	else:
		smtp.quit()
		print ' ', time.ctime(time.time()), ': email |', msg['subject'], '| sent to ', to
main()
