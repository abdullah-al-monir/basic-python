# Sets are mutable, meaning we can add or remove elements.

planets = {'Mercury', 'Venus', 'Earth'}
print(f"Initial Set: {planets}")

# 1. Adding a single element (.add())
planets.add('Mars')
print(f"1. After adding 'Mars': {planets}")

# Adding an existing element has no effect
planets.add('Venus')
print(f"   After adding 'Venus' again (no change): {planets}")

# 2. Adding multiple elements (.update())
# Use update() to add items from another iterable (like a list or tuple)
new_planets = ['Jupiter', 'Saturn']
planets.update(new_planets)
print(f"2. After updating with list: {planets}")

# 3. Removing an element (.remove())
# If the element is not found, a KeyError is raised.
planets.remove('Mercury')
print(f"3. After removing 'Mercury': {planets}")

try:
    planets.remove('Pluto')
except KeyError as e:
    print(f"   Error when removing non-existent element: {e}")

# 4. Removing an element safely (.discard())
# If the element is not found, no error is raised.
planets.discard('Jupiter')
planets.discard('Pluto') # No error here
print(f"4. After discarding 'Jupiter' and 'Pluto': {planets}")

# 5. Clearing the set (.clear())
planets.clear()
print(f"5. Set after using clear(): {planets}")