while True:

  name=input('请输入你的姓名：')

  book=name+',你好！欢迎光临!'

  print(book)

  My_file=open('guest_book.txt','a')

  My_file.write(name+',你好！欢迎光临!\n')


  My_file.close()
