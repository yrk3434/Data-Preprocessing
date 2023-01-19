'''
유동적으로 함수 선언하기
'''

regex = '...'
string_function = f'''
def my_fnt(a, b):
  {regex}
  return result
'''

exec(string_function, globals())
my_fnt(10, 20)
