import os
import ldap3

server = ldap3.Server('ldap://192.168.1.10', get_info=ldap3.ALL)
# doesn't work
conn = ldap3.Connection(server , 'uid=johndoe,ou=People,dc=host,dc=lan', 'badsecret')
assert not conn.bind()

# works
conn = ldap3.Connection(server , 'uid=johndoe,ou=People,dc=host,dc=lan', 'secret')
assert conn.bind()
