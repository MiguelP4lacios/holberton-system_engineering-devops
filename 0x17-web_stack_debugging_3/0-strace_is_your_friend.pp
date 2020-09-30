# Puppet that replaces phpp → php in wp-settings.php

exec { 'replace':
    command => 'sudo apt-get mysql && service mysql start'
}
