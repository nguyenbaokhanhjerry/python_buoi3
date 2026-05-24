order_list = ["GE001", "GE002", "GE003"]
while True:
    print(" --- HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS --- ")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ").strip()
    if choice == "1":
        if order_list == []:
            print("Danh sách đơn hàng đang trống")
        else:
            print("Danh sách đơn hàng:")
            stt = 1
            for order in order_list:
                print(stt, ".", order)
                stt = stt + 1
    elif choice == "2":
        new_order = input("Nhập mã đơn hàng mới: ")
        new_order = new_order.strip().upper()
        if new_order == "":
            print("Mã đơn hàng không được để trống")
        else:
            order_list.append(new_order)
            print("Thêm đơn hàng thành công!")
            print("Danh sách hiện tại:", order_list)
    elif choice == "3":
        delete_order = input("Nhập mã đơn hàng cần xóa: ")
        delete_order = delete_order.strip().upper()
        if delete_order in order_list:
            order_list.remove(delete_order)
            print("Xóa đơn hàng thành công!")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")
    elif choice == "4":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
