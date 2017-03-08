def fizz_buzz(argument):
	"""
     this is a function that checks the divisibility of number by 3,5,3 and 5
     if number is divisible by 3 return fizz
     if number is divisible by 5 return Buzz
     if number is divisible by both 3 and 5 return FizzBuzz
	"""
  if argument % 3 == 0 and argument % 5 == 0:
    return 'FizzBuzz'
  elif argument % 3 == 0:
    return 'Fizz'
  elif (argument % 5 == 0):
    return 'Buzz'
  else:
    return argument 