input_size = 1057


orbitCount = {"COM" : 0}
orbitCenterMap = {} # orbitCenterMap[A] = B => A orbits B

def find_orbit_count(planet):
    center = orbitCenterMap[planet]
    if center in orbitCount:
        orbitCount[planet] = 1 + orbitCount[center]
    else:
        orbitCount[planet] = 1 + find_orbit_count(center)
    
    return orbitCount[planet]



for i in range(input_size):
    line = input().split(")")
    orbitCenterMap[line[1]] = line[0]


for planet in orbitCenterMap:
    find_orbit_count(planet)

# answer to part 1
# print(sum(orbitCount.values()))



you_orbit = orbitCenterMap['YOU']
you_orbit_trail = []
while you_orbit != 'COM':
    you_orbit_trail.append(you_orbit)
    you_orbit = orbitCenterMap[you_orbit]
you_orbit_trail.append('COM')


san_orbit = orbitCenterMap['SAN']
san_orbit_trail = []
while san_orbit != 'COM':
    san_orbit_trail.append(san_orbit)
    san_orbit = orbitCenterMap[san_orbit]
san_orbit_trail.append('COM')


common_orbit = ''
for planet in you_orbit_trail:
    if planet in san_orbit_trail:
        common_orbit = planet
        break

# ans to part 2
print(san_orbit_trail.index(common_orbit))
print(you_orbit_trail.index(common_orbit))
