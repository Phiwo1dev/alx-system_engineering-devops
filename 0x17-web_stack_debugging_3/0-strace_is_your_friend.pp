# fix 500 error when GET HTTP method is requested to Apache web server.

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
