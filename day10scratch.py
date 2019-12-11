# 2326 -- too high
# 1105 -- too low


# 211 too low
# 242 too low
# 243 -- wrong
# 244
# 245
# 246
# 247
# 248
# 249 -- wrong
# 250
# 251
# 252
# 253
# 254
# 255
# 256
# 257 is wrong
# 258
# 259
# 260
# 261 is wrong
# 262
# 263 -- right
# 264 is wrong
# 265
# 266
# 267
# 268
# 269
# 270
# 271
# 272 too high






def asteroids_visible(coord, field_set, field):
  field_lines = field.splitlines()
  width = len(field_lines[1])
  height = len(field_lines)
  x1,y1 = coord
  asteroids = 0
  max_r = max(width, height)
  for r in range(1, max_r+1):
    # print r
    for d in range(360):
      t = d * pi / 180
      x = x1 + r * sin(t)
      y = y1 + r * cos(t)
      # if x.is_integer() and y.is_integer():
      if x <= width and y <= height:
        print "r, x,y", r, x-1, y-1

  # # up
  # # print "up"
  # for y2 in list(reversed(range(y1))):
  #   # print y2
  #   if (x1, y2) in field_set:
  #     asteroids += 1
  #     break

  # # top left corner to straight up

  # for x2 in range(x1+1):
  #   for y2 in range(y2+1):
  #     print "x2, y2", x2, y2
  #     dx = x1 - x2
  #     dy = y1 - y2
  #     print "dx, dy", dx, dy
  #     for x in range(0, x1):
  #       y = y1 + dy * (x - x1) / dx
  #       print "points", x, y
  #       if (x, y) in field_set:
  #         asteroids += 1
  #       # break

  # # right
  # # print "right"
  # for x2 in range(x1+1, len(field_lines[1])):
  #   # print x2
  #   if (x2, y1) in field_set:
  #     asteroids += 1
  #     break

  # # down 
  # # print "down"
  # for y2 in range(y1+1, len(field_lines[1])):
  #   # print y2
  #   if (x1, y2) in field_set:
  #     asteroids += 1
  #     break

  # # # left
  # # print "left"
  # for x2 in list(reversed(range(x1))):
  #   # print x2
  #   if (x1, y2) in field_set:
  #     asteroids += 1
  #     break

  # return asteroids




# print count_asteroids(field)