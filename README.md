# python-mail-queue
Simple Mail Queue using Python and MySQL

## Instalation & Configuration

- Clone repository
- Create MySQL Database and User
- Run `schema.sql` on your Database
- Set variables in both of scripts
  - MySQL
  - SMTP connection
- Set your CRONTAB
  - For example
  ```
  MAILTO=""
  SHELL=/bin/sh
  
  * * * * *	__USER__ python /home/__USER__/send-mail.py >> /var/log/sentmail.log
  * * * * *	__USER__ sleep 20; python /home/__USER__/send-mail.py >> /var/log/sentmail.log
  * * * * *	__USER__ sleep 40; python /home/__USER__/send-mail.py >> /var/log/sentmail.log
  ```

  - Be sure to change __USER__ as correct user used as executive user for python scripts
  - Ensure you have necessary rights
