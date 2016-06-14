# Catalog
a sports catalog web app using Flask and deployed on AWS EC2 vm

## Settings

###EC2 VM Version:
Ubuntu 14.04.4 LTS

###IP address:

52.36.114.208(subject to change since the VM instance will be removed, so does the URL)

###URL: 

http://ec2-52-36-114-208.us-west-2.compute.amazonaws.com

###SSH Port(Not the default port 22):

2200

###grader user info:
- private key pass phrase: grader
- user name: grader
- passwd: Grader@udacity.com
- login type: private key authentication only

###List of packages installed:
####apt-get list:
- ntp(ntpd)
- apache2
- libapache2-mod-wsgi
- postgresql
- python-psycopg2
- python-pip
- python-dev
- git
- fail2ban
- unattended-upgrades

####pip list:
- Flask
- sqlalchemy
- oauth2client
- requests
- httplib2
- flask-seasurf
- dicttoxml
- flask_wtf
- glances

###Configuration Changes:
- ssh port changed to 2200
- disable root login
- add grader user to sudoers config
- ufw only allows port: 80, 123, 2200
- update the Google/Facebook oauth client secret according to your application
- add entry for database user catalog in pg_hba.conf
- apaceh site configuration file:

~~~~
<VirtualHost *:80>
                ServerName 52.36.114.208
                ServerAlias ec2-52-36-114-208.us-west-2.compute.amazonaws.com
                ServerAdmin admin@mywebsite.com
                WSGIScriptAlias / /var/www/catalog/catalog.wsgi
                <Directory /var/www/catalog/catalog/>
                        Order allow,deny
                        Allow from all
                </Directory>
                Alias /static /var/www/catalog/catalog/static
                <Directory /var/www/catalog/catalog/static/>
                        Order allow,deny
                        Allow from all
                </Directory>
                Alias /templates /var/www/catalog/catalog/templates
                <Directory /var/www/catalog/catalog/templates/>
                        Order allow,deny
                        Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
~~~~

###Additional Features:
- use unattended-upgrades to automatically install security updates.
- use fail2ban to monitor unsuccessful login attempts and ban attackers.
- use python glances to monitor system

###Great References:

1. [Useful links and possible problems you may encounter as well as its link to stackoverflow][1]
2. [An tutorial to set up configuration in Flask for postgresql][2]

[1]: https://discussions.udacity.com/t/p5-how-i-got-through-it/15342
[2]: http://newcoder.io/scrape/part-3/


I strongly agree with "/var/log/apache2/error.log is you best friend!"
