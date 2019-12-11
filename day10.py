field = '''.#..#..##.#...###.#............#.
.....#..........##..#..#####.#..#
#....#...#..#.......#...........#
.#....#....#....#.#...#.#.#.#....
..#..#.....#.......###.#.#.##....
...#.##.###..#....#........#..#.#
..#.##..#.#.#...##..........#...#
..#..#.......................#..#
...#..#.#...##.#...#.#..#.#......
......#......#.....#.............
.###..#.#..#...#..#.#.......##..#
.#...#.................###......#
#.#.......#..####.#..##.###.....#
.#.#..#.#...##.#.#..#..##.#.#.#..
##...#....#...#....##....#.#....#
......#..#......#.#.....##..#.#..
##.###.....#.#.###.#..#..#..###..
#...........#.#..#..#..#....#....
..........#.#.#..#.###...#.....#.
...#.###........##..#..##........
.###.....#.#.###...##.........#..
#.#...##.....#.#.........#..#.###
..##..##........#........#......#
..####......#...#..........#.#...
......##...##.#........#...##.##.
.#..###...#.......#........#....#
...##...#..#...#..#..#.#.#...#...
....#......#.#............##.....
#......####...#.....#...#......#.
...#............#...#..#.#.#..#.#
.#...#....###.####....#.#........
#.#...##...#.##...#....#.#..##.#.
.#....#.###..#..##.#.##...#.#..##
'''

# field = '''
# ......#.#.
# #..#.#....
# ..#######.
# .#.#.###..
# .#..#.....
# ..#....#.#
# #..#....#.
# .##.#..###
# ##...#..#.
# .#....####
# '''

# field = '''.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##
# '''

def count_asteroids(field):
  count = 0
  lines = field.splitlines()
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      print x,y-1
      if char == '#':
        count += 1
  return count

def build_field_set(field):
  field_set = set()
  lines = field.splitlines()
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      # print (x,y)
      if char == '#':
        field_set.add((x,y))
  return field_set

field_set =  build_field_set(field)

# print field_set

# print count_asteroids(field) == len(field_set)

from math import atan2, degrees, hypot, pi, radians

def angles_of_asteroids(coord, field_set):
  x1, y1 = coord
  theta_dictionary = {}
  asteroid_set = field_set.copy()
  asteroid_set.remove(coord)
  # print "size", len(field_set)
  for asteroid in asteroid_set:
    x2, y2 = asteroid
    dx = x1 - x2
    dy = y2 - y1
    theta_radians = atan2(dx, dy)
    r = hypot(dx, dy)
    # print degrees(theta_radians)
    if theta_radians not in theta_dictionary:
      theta_dictionary[theta_radians] = [(r, (x2, y2))]
    else:
      theta_dictionary[theta_radians].append((r, (x2, y2)))

  # print radian_set
  for key in theta_dictionary.keys():
    theta_dictionary[key].sort()
  return theta_dictionary

# print angles_of_asteroids((11,13), field_set)

def find_max_asteroids(field_set): # part 1
  max_asteroids = 0
  best_coord = None
  for point in field_set:
    visible_dict = angles_of_asteroids(point, field_set)
    visible = len(visible_dict.keys())
    if visible > max_asteroids:
      best_coord = point
      max_asteroids = visible
  return max_asteroids, best_coord

# print find_max_asteroids(field_set)

def vaporize(field_set):
  asteroid_count = 0
  asteroid_order = []
  best_coord = find_max_asteroids(field_set)[1]
  # print best_coord
  asteroid_angles_dict = angles_of_asteroids(best_coord, field_set)
  # print asteroid_angles_dict
  # current_coord = None
  # while asteroid_count <= 200:
  float_keys = asteroid_angles_dict.keys()
  float_keys.sort()
  print float_keys
  for key in float_keys:
    asteroid_count += 1
    all_asteroids_at_point = asteroid_angles_dict[key]
    current_coord = all_asteroids_at_point.pop(0)
    if current_coord[1] != best_coord:
      asteroid_order.append(current_coord[1])
  # while len(asteroid_order) < 200:
  #   for degree in range(360):
  #     rad = degree * pi / 180
  #     if rad in asteroid_angles_dict:
  #       # print rad
  #       # asteroid_count += 1
  #       all_asteroids_at_point = asteroid_angles_dict[rad]
  #       current_coord = all_asteroids_at_point.pop(0)
  #       asteroid_order.append(current_coord[1])
  #       if len(all_asteroids_at_point) == 0:
  #         del asteroid_angles_dict[rad]
  return asteroid_order[198]

print vaporize(field_set)

def part2():
  pass
