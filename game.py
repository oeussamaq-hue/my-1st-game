import random


start = 1
end = 100
target: int = random.randint(start, end)
num: int | None = None
retries: int = 5

while retries > 0:
    try:
        num = int(input(">>> enter a number: "))
    except ValueError as e:
        print("+ not a valid number")
        num = 0

    if num < target:
        print(f"+ to high! [retries left {retries}]")
        retries -= 1
    elif num > target:
        print(f"+ too low! [retries left {retries}]")
        retries -= 1

    else:
        print(f">> you guessed it!, it was {target}!")
        break

else:
	print(f">> out of retries, it was {target}")
