ves_bez_gruza = int(input("ves_bez gruza:"))
vysota_platformy = int(input("vysota_platformy:"))
ves_pianino = int(input("ves_pianino:"))
vysota_pianino = int(input("vysota_pianino:"))
ves_holod = int(input("ves_holod:"))
vysota_holod = int(input("vysota_holod:"))
max_ves = int(input("max_ves:"))
max_vysota = int(input("max_vysota:"))

ves = ves_bez_gruza + ves_pianino + ves_holod
if vysota_pianino >= vysota_holod:
    vysota = vysota_platformy + vysota_pianino
else:
    vysota = vysota_platformy + vysota_holod

if max_ves >= ves and max_vysota >= vysota:
    print("YES")
else:
    print("NO")
