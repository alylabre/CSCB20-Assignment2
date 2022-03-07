from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def user(name):

  def has_number(str):
    return any(char.isdigit() for char in str)
  
  def remove_number(str):
    return ''.join([char for char in str if not char.isdigit()])

  print(name)
  name = name.strip()
  
  if has_number(name):
    name_no_num = remove_number(name)
    new_name = name_no_num.upper()
  elif name.islower():
    print('lower')
    new_name = name.upper()
  elif name.isupper():
    print('upper')
    new_name = name.lower()
  elif not name.islower() and not name.isupper():
    new_name = name[0].upper() + name[1:].lower()

  message = f'Welcome, {new_name}, to my CSCB20 website!'
  return message

if __name__ == '__main__':
  app.run(debug=True)