for i in range(1, 22):
    if (i % 3==0) and (i % 5==0):
      print("Fizz_Buzz")
      
# """       I started with the above line of code because starting with (i%3==0) will mean 15 will have been processed early on, and by the time its its to run the "both" instruction it wont be effective. """
      
    elif  i%3==0:
      print("Fizz")
      
    elif i%5==0:
      print('Buzz')
  
      
    else:
      print(i)   
      
      