# Puppet that replaces phpp → php in wp-settings.php
exec{'replace':
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php && service apache2 reload',
    provider => 'shell',
}
