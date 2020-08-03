# this kill to ./killmenow
exec {'pkill killmenow':
  path => "/usr/bin:/usr/sbin:/bin",
}
