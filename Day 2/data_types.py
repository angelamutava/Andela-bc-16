def data_type(argument):
  """
  this is a function that checks the type of argument passed and for a given type perfoms the given task
  string:return the length of the string
  bool:return the boolean
  int :checks whether the value passed is less,equal or more than 100 and returns appropriate message
  list returns the third element in the list
  """
  if isinstance(argument, str):
    return len(argument)
  elif argument is None:
    return 'no value'
  elif isinstance(argument, bool):
    return argument
  elif isinstance(argument, int):
    if argument == 100:
      return 'equal to 100'
    elif argument < 100:
      return 'less than 100'
    elif argument > 100:
      return 'more than 100'
  elif isinstance(argument, list):
    len_of_list = len(argument) - 1
    if len_of_list >= 2:
      return argument[2]
    else:
      return None