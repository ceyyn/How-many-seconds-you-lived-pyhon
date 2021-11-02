from datetime import datetime
color = "\033[92m"
varsay = "\033[0m"
birthday = datetime.strptime(input( "Your birthday as d.m.Y :"),"%d %m %Y")
now = datetime.now()
result = now - birthday
print(color + "You lived {} seconds".format(result.total_seconds())+varsay)