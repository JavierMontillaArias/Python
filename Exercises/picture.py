picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill = '*'
empty = ' '

for image in picture:
    for pixel in image:
        if pixel:
            print(fill, end=' ')
        else:
            print(empty, end=' ')
    print('')