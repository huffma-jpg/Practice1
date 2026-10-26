GO_THRU = 24

SHRP_GRN = 1.0
SHRP_BLUE = 1.15
SHRP_WHITE = 1.2
SHRP_PINK = 1.3

PRT_HEAD = 21
PRT_BODY = 19
PRT_LEG = 21
PRT_WING = 19
PRT_TAIL = 24

mon_health = int(100)
u_health = int(100)
sharpness = SHRP_PINK

def menu():
    global mon_health, u_health

    print("1. Head")
    print("2. Body")
    print("3. Leg")
    print("4. Wing")
    print("5. Tail")
    part = str(input("Choose a part to swing at!: "))

    while True:
        if part == "1":
            if sharpness * PRT_HEAD >= GO_THRU:
                mon_health -= 20
            else:
                u_health -= 20
                break
        elif part == "2":
            if sharpness * PRT_BODY >= GO_THRU:
                mon_health -= 20
            else:
                u_health -= 20
                break
        elif part == "3":
            if sharpness * PRT_LEG >= GO_THRU:
                mon_health -= 20
            else:
                u_health -= 20
                break
        elif part == "4":
            if sharpness * PRT_WING >= GO_THRU:
                mon_health -= 20
            else:
                u_health -= 20
                break
        elif part == "5":
            if sharpness * PRT_TAIL >= GO_THRU:
                mon_health -= 20
            else:
                u_health -= 20
                break
        else:
            print("Invalid option!")
            u_health -= 20
            break

    print(f"Your Health: {u_health}")
    print(f"Monster Health: {mon_health}")

if __name__ == "__main__":
    menu()
    

