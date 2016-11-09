epic_programmer_dict = {
    'tim berners-lee':['tbl@gmail.com',111],
    'guido van rossum': ['gvr@gmail.com',222],
    'linus torvalds': ['lt@gmail.com',333],
    'larry page': ['lp@gmail.com',444],
    'sergey brin': ['sb@gmail.com',555]}

try:
    personsInfo = epic_programmer_dict['sergey brin'].title()
    print 'Name: '+ 'sergey brin'.title()
    print 'Email: '+ personsInfo[0]
    print 'Number: '+ str(personsInfo[1])
except:
    print 'No information found'

