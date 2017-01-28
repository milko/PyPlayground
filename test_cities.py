from library import *

# Load graph.
g = Graph()

g.relateNodes("Montreal", "Boston", 69)
g.relateNodes("Montreal", "New York", 99)
g.relateNodes("Montreal", "Toronto", 115)
g.relateNodes("Boston", "New York", 74)
g.relateNodes("New York", "Pittsburgh", 69)
g.relateNodes("New York", "Washington", 76)
g.relateNodes("Toronto", "Pittsburgh", 80)
g.relateNodes("Toronto", "Sault Ste Marie", 90)
g.relateNodes("Pittsburgh", "Chicago", 81)
g.relateNodes("Pittsburgh", "Washington", 85)
g.relateNodes("Washington", "Raleigh", 47)
g.relateNodes("Sault Ste Marie", "Winnipeg", 156)
g.relateNodes("Sault Ste Marie", "Duluth", 110)
g.relateNodes("Chicago", "Duluth", 157)
g.relateNodes("Chicago", "Omaha", 142)
g.relateNodes("Chicago", "Saint Louis", 142)
g.relateNodes("Raleigh", "Nashville", 128)
g.relateNodes("Raleigh", "Atlanta", 96)
g.relateNodes("Raleigh", "Charleston", 96)
g.relateNodes("Winnipeg", "Duluth", 103)
g.relateNodes("Winnipeg", "Helena", 137)
g.relateNodes("Winnipeg", "Calgary", 180)
g.relateNodes("Duluth", "Omaha", 74)
g.relateNodes("Duluth", "Helena", 150)
g.relateNodes("Omaha", "Helena", 174)
g.relateNodes("Omaha", "Denver", 130)
g.relateNodes("Saint Louis", "Nashville", 85)
g.relateNodes("Saint Louis", "Little Rock", 60)
g.relateNodes("Saint Louis", "Kansas City", 68)
g.relateNodes("Nashville", "Atlanta", 67)
g.relateNodes("Nashville", "Little Rock", 94)
g.relateNodes("Atlanta", "Charleston", 63)
g.relateNodes("Atlanta", "Miami", 116)
g.relateNodes("Atlanta", "New Orleans", 120)
g.relateNodes("Charleston", "Miami", 80)
g.relateNodes("Helena", "Calgary", 130)
g.relateNodes("Helena", "Seattle", 189)
g.relateNodes("Helena", "Salt Lake City", 116)
g.relateNodes("Helena", "Denver", 126)
g.relateNodes("Calgary", "Vancouver", 100)
g.relateNodes("Calgary", "Seattle", 118)
g.relateNodes("Denver", "Kansas City", 135)
g.relateNodes("Denver", "Santa Fe", 70)
g.relateNodes("Denver", "Phoenix", 128)
g.relateNodes("Denver", "Salt Lake City", 101)
g.relateNodes("Little Rock", "New Orleans", 100)
g.relateNodes("Little Rock", "Dallas", 74)
g.relateNodes("Little Rock", "Oklahoma City", 72)
g.relateNodes("Kansas City", "Oklahoma City", 61)
g.relateNodes("Miami", "New Orleans", 151)
g.relateNodes("Seattle", "Vancouver", 45)
g.relateNodes("Seattle", "Portland", 44)
g.relateNodes("Salt Lake City", "Portland", 175)
g.relateNodes("Salt Lake City", "San Francisco", 156)
g.relateNodes("Salt Lake City", "Las Vegas", 156)
g.relateNodes("New Orleans", "Houston", 80)
g.relateNodes("Santa Fe", "Oklahoma City", 121)
g.relateNodes("Santa Fe", "El Paso", 65)
g.relateNodes("Santa Fe", "Phoenix", 85)
g.relateNodes("Phoenix", "Los Angeles", 109)
g.relateNodes("Dallas", "Houston", 46)
g.relateNodes("Dallas", "El Paso", 140)
g.relateNodes("Portland", "San Francisco", 151)
g.relateNodes("San Francisco", "Los Angeles", 100)
g.relateNodes("Las Vegas", "Los Angeles", 66)
g.relateNodes("El Paso", "Los Angeles", 191)

print(str(g))
print("===========================")

print( "Shortest path from Miami to Vancouver" )
x = g.leastNodes("Miami", "Vancouver")
print(str(x))

print( "Least cost path from Miami to Vancouver" )
x = g.leastCost("Miami", "Vancouver")
print(str(x))

print("===========================")

print( "Shortest path from Charleston to Seattle" )
x = g.leastNodes("Charleston", "Seattle")
print(str(x))

print( "Least cost path from Charleston to Seattle" )
x = g.leastCost("Charleston", "Seattle")
print(str(x))