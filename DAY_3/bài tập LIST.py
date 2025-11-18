
#Tạo một movies list chứa tên các bộ phim đã xem
#Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
#Thêm bộ phim vừa nhập vào cuối của danh sách movies
#In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
#Tính tổng bộ phim có trong movies
#Xóa bộ phim đầu và cuối trong movies
#Lấy ra và xóa bộ phim cuối cùng trong movies
#Chèn một bộ phim bất kỳ vào đầu danh sách movies
#Đếm số bộ phim có tiêu đề là "One Piece"
#Tìm vị trí của bộ phim có tên là "gió"
#Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
#Xóa tất cả các bộ phim có trong danh sách

# list_movies = ["Gió", "One Piece", "Avatar", "Harry Potter", "Inception"]
# print("Danh sách phim đã xem: ", list_movies)

# film_not_list = input("Nhập tên bộ phim bạn muốn thêm vào danh sách: ")
# print(f"Bạn đã thêm bộ phim: {film_not_list} vào danh sách.")

# film_add_last = list_movies.append(film_not_list)
# print(f"Phim đã thêm vào cuối danh sách: {list_movies}")

# print(f"phim dau: {list_movies[0]}, phim cuoi: {list_movies[-1]}, phim o giua: {list_movies[len(list_movies) // 2]}")
# print(f"tong: {len(list_movies)}")

# list_remove = list_movies.pop()
# list_remove2 =list_movies.pop(0)
# print(f"Phim còn lại sau khi đã xóa đầu và cuối: {list_movies}")

# get_and_remove = list_movies.pop()
# print(f"phim lay ra và xoa phim cuoi cung la: {get_and_remove}",  f"\nphim con lai: {list_movies}")

# list_movies.insert(0, "Gió")
# print(f"phim da chen vao dau la: {list_movies}")
# count_one_piece = list_movies.count("One Piece")
# print(f"Số lượng phim có tiêu đề 'One Piece': {count_one_piece}")
# index_gio = list_movies.index("Gió")
# print(f"Vị trí của phim 'Gió' trong danh sách: {index_gio}")

# list_movies2 = ["111", "222", "333"]
# list_movies.extend(list_movies2)
# print(f"phim da them vao cuoi la: {list_movies}") 

"""
+ list 0n list
+ coppy list
+ list slising (lấy ra một phần của list ban đầu) => new list | slicing = [start:end:step]

"""
#               0            1               2
# friends = [["Bob",23], ["Alice", 22], ["Charlie", 25]]

# print(friends[0][1])

#
# lst_1 = [1, 2, 3]
# lst_2 = lst_1.copy()             
# print(lst_1 is lst_2)        # is để kiểm tra xem lst_1 và lst_2 có phải là cùng một đối tượng trong bộ nhớ hay không
# print(id(lst_1), id(lst_2))  # in ra địa chỉ bộ nhớ của lst_1 và lst_2

#        0  1  2  3  4  5  6  7  8  9
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
lst_2 = lst_1[0:7:1]  # lấy ra phần tử từ vị trí 0 đến 2 (không bao gồm 3)
print (lst_2)  # in ra [1, 2, 3]
lst_3 = lst_1[:7:3]
print(lst_3)  # in ra [1, 4, 7]
lst_4 = lst_1[::9]  # lấy ra tất cả các phần tử với bước nhảy là 9
print(lst_4) 
