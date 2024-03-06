# Exercise 40. Sound volume

volume_level = int(input('Input volume level in decibels(dB): '))
numbers = [40 , 70 , 106 , 130]

if 40 <= volume_level <= 130:
    if volume_level in numbers:
        if volume_level == 40:
            print('Quiet room. ')
        if volume_level == 70:
            print('Alarm. ')
        if volume_level == 106:
            print('Gas lawn mower. ')
        if volume_level == 130: 
            print('Jackhammer. ')
    else:
        if 40 <= volume_level <= 70:
            if volume_level - 40 < 70 - volume_level:
                print('Quiet room. ')
            else:
                print('Alarm. ')
        if 70 <= volume_level <= 106:
            if volume_level - 70 < 106 - volume_level:
                print('Alarm. ')
            else:
                print('Gas lawn mower.')
        if 106 <= volume_level <= 130:
            if volume_level - 106 < 130 - volume_level:
                print('Gas lawn mower. ')
            else:
                print('Jackhammer. ')
else:
    print('Number shloud be > 39 and < 131')