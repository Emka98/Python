MIN_LIKES = 500

MIN_SHARES = 100


num_likes = 1300

num_shares= 55


if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:

    print('GREAT! Today our prizes drop 10% !!!')

else:

    print('We still need more likes and shares to start the promotion')


##############################################


isPizzaOrdered = True

isWeekend = True

isBigDrinkOrdered = True


if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:

    print('Burger for FREE!!!')

else:

    print('Come to us on week day and consider buying Pizza or BigDrink to have Burger for free')


##############################################


diskSize = 140

diskSizeUsed = 133

fileSize = 10


if diskSize - diskSizeUsed >= fileSize :

    print('The file can be downloaded')

else:

    print('There isn\'t enough free disk space to download the file. Sorry :(')
