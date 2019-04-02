def playlist(songs):
  number = songs.pop(0)
  flag = 0
  for i in range(number): #0,1,2,3
    for n in range(i):# 0->/, 1->0, 2->0,1, 3->0,1,2
      val = songs[i] + songs[n]
      print(i)
      print(n)
      print("---")
      if(val % 60 == 0):
        flag = flag + 1

playlist([4,10,50,90,30])