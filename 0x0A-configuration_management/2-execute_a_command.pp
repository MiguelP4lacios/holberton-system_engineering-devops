# this kill to ./killmenow
exec {'pkill killmenow':
  path    => "/usr/bin:/usr/sbin:/bin",
  onlyif  => 'ps -a | grep killmenow'
}
