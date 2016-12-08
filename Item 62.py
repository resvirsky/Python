from datetime import datetime, timedelta
import calendar


#define times
nowPORTLAND=datetime.utcnow()-timedelta(hours=8)
nowLONDON=nowPORTLAND+timedelta(hours=8)
nowNY=nowPORTLAND+timedelta(hours=3)

#try to define the open/close time of the branches in Portland time
openNY = datetime(*datetime.fromtimestamp(calendar.timegm(datetime.today().utctimetuple())).utctimetuple()[:3], hour=5, minute=00)
closeNY = datetime(*datetime.fromtimestamp(calendar.timegm(datetime.today().utctimetuple())).utctimetuple()[:3], hour=17, minute=00)
openLD = datetime(*datetime.fromtimestamp(calendar.timegm(datetime.today().utctimetuple())).utctimetuple()[:3], hour=00, minute=00)
closeLD = datetime(*datetime.fromtimestamp(calendar.timegm(datetime.today().utctimetuple())).utctimetuple()[:3], hour=12, minute=00)


#want to compare the time in portland to the relative open hours

if nowPORTLAND<openNY:
    print 'NY Closed'
elif nowPORTLAND>closeNY:
    print 'NY Closed'
else:
    print 'NY Open'

if nowPORTLAND<openLD:
    print 'London Closed'
elif nowPORTLAND>closeLD:
    print 'London Closed'
else:
    print 'London Open'


#print nowPORTLAND
#print nowNY
#print nowLONDON

