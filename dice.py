import random

x="y"

while x=="y":
    num = random.randint(1, 6)

    if (num == 1):
        print("--------------")
        print("|            |")
        print("|            |")
        print("|     *      |")
        print("|            |")
        print("--------------")
    if (num == 2):
        print("--------------")
        print("|            |")
        print("|            |")
        print("|     * *    |")
        print("|            |")
        print("--------------")
    if (num == 3):
        print("--------------")
        print("|             |")
        print("|             |")
        print("|   *  *  *   |")
        print("|             |")
        print("--------------")
    if (num == 4):
        print("--------------")
        print("|             |")
        print("|     * *     |")
        print("|     * *     |")
        print("|             |")
        print("--------------")
    if (num == 5):
        print("--------------")
        print("|             |")
        print("|   *     *   |")
        print("|      *      |")
        print("|   *     *   |")
        print("--------------")
    if (num == 6):
        print("--------------")
        print("|             |")
        print("|    * * *    |")
        print("|    * * *    |")
        print("|             |")
        print("--------------")
    x = input("Enter Y to roll again. Or press any key and enter to exit ")



