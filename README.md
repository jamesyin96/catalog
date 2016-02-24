# Catalog
a catalog app that's deployed in aws ec2 vm

## Settings
###IP address:

52.26.178.19

###URL: 

http://ec2-52-26-178-19.us-west-2.compute.amazonaws.com

###SSH Port:

2200

###List of packages installed:
####apt-get list:
- ntpd
- postgresql
- python-pip

####pip list:
- Flask
- psycopg2
- sqlalchemy
- oauth2client
- requests
- httplib2
- flask-seasurf
- dicttoxml
- flask_wtf

###Configuration Changes:
- ssh port changed to 2200
- add entry for database user catalog in pg_hba.conf
- apaceh site configuration file:

~~~~
<VirtualHost *:80>
                ServerName 52.26.178.19
                ServerAlias ec2-52-26-178-19.us-west-2.compute.amazonaws.com
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

###Great References:

1. [Useful links and possible problems you may encounter as well as its link to stackoverflow][1]
2. [An tutorial to set up configuration in Flask for postgresql][2]

[1]: https://discussions.udacity.com/t/p5-how-i-got-through-it/15342
[2]: http://stackoverflow.com


I strongly agree with "/var/log/apache2/error.log is you best friend!"
