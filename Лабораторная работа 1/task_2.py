def books_on_disk(disk_capacity, num_pages, num_lines, num_chars):
    bytes_book = num_pages * num_lines * num_chars * 4
    books_on_disk = disk_capacity / bytes_book
    
    return int(books_on_disk)

disk_capacity = 1.44 * 2 ** 20 
num_pages = 100
num_lines = 50
num_chars = 25

result = books_on_disk(disk_capacity, num_pages, num_lines, num_chars)
print(result)
