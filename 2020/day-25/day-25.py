card_public_key = 1965712
door_public_key = 19072108

number = 1
subject_number = 7

loop = 0
found = []
while True:
    loop += 1
    number = number * subject_number
    number %= 20201227

    if number == card_public_key:
        found.append((door_public_key, loop))
    if number == door_public_key:
        found.append((card_public_key, loop))
    if len(found) == 2:
        break

for public_key, loop_size in found:
    encryption_key = 1
    for _ in range(loop_size):
        encryption_key *= public_key
        encryption_key %= 20201227
    print(encryption_key)
