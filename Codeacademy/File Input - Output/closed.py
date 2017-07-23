with open("text5.txt", 'w') as my_file:
    my_file.write('Writing using with ... as')

if not my_file.closed:
    my_file.close()

print my_file.closed
