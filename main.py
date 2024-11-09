file_write = open('students.txt' , 'w')
file_write.write("10/1/24")
file_write.close()

file_append = open('students.txt' , 'a')
file_append.write("\nSiddarsh is an excellent coder \n Jeffrey talks only when necessary \n John does not eat during class.")
file_append.close()