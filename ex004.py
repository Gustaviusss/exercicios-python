# um programa que diz o que o input é ou não
content = input('digite algo: ')
print(content.isalnum(),
      content.isalpha(),
      content.isascii(),
      content.isdecimal(),
      content.isdigit(),
      content.isprintable(),
      content.isidentifier(),
      content.islower(),
      content.isnumeric(),
      content.isspace(),
      content.isupper()
      )