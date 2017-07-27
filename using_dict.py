#!/usr/bin/python
# Filename:using_dict.py

ab = { 'Swaroop' : 'swarrr@byteood.info',
       'Larry' : 'larry@wall.org',
       'Mastusan': 'matz@ruby.org',
       'Spamm' : 'spma@hotma.com'
}

print "Swaroop's address is %s" %ab['Swaroop']

ab['Guido']='guido@python.org'

del ab['Spamm']

print '\nThere are %d contacts in the address-book\n' %len(ab)

for name,address in ab.items():
	print 'Contact %s at %s' %(name,address)

if 'Guido' in ab:
	print "\nGuido's address is %s" %ab['Guido']
