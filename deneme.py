def usernamesSystem(u):
  k = 1
  num = u.pop(0)
  for n in range(num - 1):
    if(u[n] == u[n+1]):
      u[n+1] = u[n+1] + str(k)
      k = k + 1  
    print(u[n])
    print(u[n+1])
  print(u)

usernamesSystem([4,"John","John","Tom","John"])


