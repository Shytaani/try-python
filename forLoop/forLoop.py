onCourt = ['Schroder', 'Caldwell-Pope', 'James', 'Davis', 'Gasol']
subs = ['Caruso', 'Horton-Tucker', 'Matthews', 'Kuzma', 'Harrell']

print("Starting 5!")
for i, player in enumerate(onCourt):
    if i == 0:
        print(f"PG:{player}")
    elif i == 1:
        print(f"SG:{player}")
    elif i == 2:
        print(f"SF:{player}")
    elif i == 3:
        print(f"PF:{player}")
    elif i == 4:
        print(f"C:{player}")

subPosition = input("Select position to substitute(PG=1, SG=2, SF=3, PF=4, C=5).\n")
index = int(subPosition) - 1
if index in range(0, 5):
    onCourt[index] = subs[index]
    print("Substitute!")
    for i, player in enumerate(onCourt):
        if i == 0:
            print(f"PG:{player}")
        elif i == 1:
            print(f"SG:{player}")
        elif i == 2:
            print(f"SF:{player}")
        elif i == 3:
            print(f"PF:{player}")
        elif i == 4:
            print(f"C:{player}")
else:
    print("Input a number between 1 and 5")