c = 'k'
thickness = 5
for i in range(thickness+1):
    print((c*thickness).rjust(thickness*2)+(c*thickness).ljust(thickness*6))

