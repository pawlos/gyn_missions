import png

org = open('LEVELS.org','rb').read()
new = open('LEVELS.DAT','rb').read()


level_mappings = {0:0,1:1,2:2,3:3,4:4,5:5,6:6}

levels_count = len(new)/1536

pal = [(255,255,255),(0,0,0),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(192,0,0),(0,192,0),(0,0,192),(192,192,0),(192,0,192),(0,192,192),(50,99,0),(200,0,200),(100,0,20),(200,40,80),(255,128,90),(90,128,128),(128,128,128),(50,0,0),(0,0,50),(0,50,0),(99,99,0),(0,99,40),(40,99,129),(77,66,0),(55,155,255),(99,99,99),(192,150,0),(150,192,0),(0,150,192),(77,99,111),(111,99,77),(99,77,111),(20,80,160),(160,60,0),(0,60,160),(160,0,60),(30,60,90)]
print 'Levels count: ', levels_count
f = open('levels-all.png', 'wb')      # binary mode is important
w = png.Writer(60*levels_count, 24*2)

lines = []
items = []
for y in range(w.height):
  line = []
  iteml = []
  d = None
  if y < 24:
    d = new
  else:
    d = org
  for x in range(w.width):
    nb = x / 60
    
    if nb in level_mappings:
      nb = nb if y > 24 else level_mappings[nb]
    elif nb not in level_mappings and y > 24 and nb != 111:
      #print nb, len(d)/1536
      nb = 117-nb
    real_x = x % 60
    pos = nb * 1536 + (y % 24) * 60 + real_x
    if nb == 111 and y < 24:
      pos += 5
    item_new = 0
    if pos >= len(d) and y>=24:
      pos = 7*1536 + (y % 24) * 60 + real_x
    item_new = int(d[pos].encode('hex'),16)
    if item_new >= len(pal):
      print 'Outside: ',item_new
      item_new = 0
    color = pal[item_new]
    iteml.append(item_new)
    line.append(color[0])
    line.append(color[1])
    line.append(color[2])
  lines.append(line)
  items.append(iteml)

w.write(f, lines)
f.close()

print levels_count
print len(lines[0])
print len(lines)

f2 = open('levels-diff.png','wb')
w2 = png.Writer(60*levels_count, 24)

lines2 = []
for y in range(24):
  line = []
  for x in range(0, 60*levels_count*3,3):
    r1,g1,b1 = lines[y][x], lines[y][x+1], lines[y][x+2]
    r2,g2,b2 = lines[y+24][x], lines[y+24][x+1], lines[y+24][x+2]
    if r1 != r2 or g1 != g2 or b1 != b2:
      line.append(r1)
      line.append(g1)
      line.append(b1)
    else:
      line.append(254)
      line.append(254)
      line.append(254)
  lines2.append(line)
w2.write(f2, lines2)
f2.close()

f3 = open('levels-diff2.png','wb')
w3 = png.Writer(60*levels_count, 24)

lines3 = []
for y in range(24):
  line = []
  for x in range(60*levels_count):
    i1, i2 = items[y][x],items[y+24][x]
    if i1 != i2:
      i = i1-i2
      #c1, c2 = pal[i1],pal[i2]
      c = pal[i1]#(c2[0] - c1[0],c2[1]-c1[1],c2[2]-c1[2])
      line.append(c[0])
      line.append(c[1])
      line.append(c[2])
    else:
      line.append(255)
      line.append(255)
      line.append(255)

  lines3.append(line)

w3.write(f3, lines3)
f3.close()
