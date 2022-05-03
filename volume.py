pi = 3.142
def print_volume(radius):
    radius_cube =(radius * radius * radius)
    fraction = 4 / 3
    volume = fraction * pi * radius_cube
    print(volume)



print_volume(5)
print_volume(8)
print_volume(10)

