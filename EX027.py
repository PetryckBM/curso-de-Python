import time
print("OS fogos vao ser lançados em ")
regreco = 11
for segundo in range(11):  # 0 até 10
    regreco -= 1
    print(f"{regreco} s")
    if segundo < 10:
        time.sleep(1)
print("Booom")

