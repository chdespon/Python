import time
# Write a script that formats the dates this way "Seconds since January 1,
# 1970: 1,666,355,857.3622 or time in scientific notation$
# Oct 21 2022$", of course your date will not be mine
# as in the example but it must be formatted the same


if __name__ == '__main__':
    timeS = time.time()
    timeF = f"{timeS: ,}"
    print("Seconds since January 1, 1970: " + str(timeF) + f" or {timeS:.2e} "
          + " in scientific notation")
    print(time.strftime("%b %d %Y", time.localtime()))
