f = open("image.txt", "w+")

for i in range(24, -1, -1):
    for j in range(40):
        f.write("World_{:02d}_{:02d}.png\n".format(j, i))

f.close()
