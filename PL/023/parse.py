import png

class Level:
  def __init__(self, data, no):
    self.no = no
    pos = 0
    self.level = data[pos:pos+1440]
    pos += 1440
    self.unused = data[pos:pos+4]
    pos += 4
    self.gravity = data[pos:pos+1]
    pos += 1
    self.speed_fix = data[pos:pos+1]
    pos += 1
    self.title = data[pos:pos+23]
    pos += 23
    self.freeze_zones = data[pos:pos+1]
    pos += 1
    self.infotrons = data[pos:pos+1]
    pos += 1
    self.gravity_ports_count = data[pos:pos+1]
    pos += 1
    self.gravity_ports = data[pos:pos+60]
    pos += 60
    self.unknown = data[pos:pos+4]
    pos += 4
    #print 'ok'


org = open('LEVELS.org','rb').read()
new = open('LEVELS.DAT','rb').read()

org_len = len(org)/1536
new_len = len(new)/1536

org_levels = []

for i in xrange(org_len):
  org_levels.append(Level(org[i*1536:(i+1)*1536],i+1))

new_levels = []

for i in xrange(new_len):
  new_levels.append(Level(new[i*1536:(i+1)*1536],i+1))

for l1,l2 in zip(org_levels,new_levels):
  print l1.title, l1.unused.encode('hex'), l1.unknown.encode('hex'),' - ',l2.unused.encode('hex'), l2.unknown.encode('hex')
