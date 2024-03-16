# login with the holberton user and open a file without any error message.
exec { 'hard limit':
  command => "sed -i 's/5/4000/' /etc/security/limits.conf",
  path    => '/bin'
}
exec { 'soft limit':
  command => "sed -i 's/4/2000/' /etc/security/limits.conf",
  path    => '/bin'
}
