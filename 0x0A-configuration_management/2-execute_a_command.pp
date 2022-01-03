# Execute a command that create a manifest that kills a process named killmenow

exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/local/bin/:/bin/',
    #path    => [ '/usr/local/bin/', '/bin/' ],  # alternative syntax
}
