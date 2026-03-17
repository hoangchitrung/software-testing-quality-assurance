# Quy Tắc khi viết testcases:

- Không được trùng testcases (Ví dụ: Chức năng tìm kiếm sản phẩm dựa theo tên nếu như đã có rồi mà tiếp theo nếu như có chức năng tìm sản phẩm dựa theo hãng thì không được). Các testcase phải là một flow chứ không phải là một chức năng riêng nhỏ lẻ. Tổng số lượng testcases là 30
- Các lệnh như execute script nên ngắn gọn và không được dài. Nếu như dài quá thì phải tách ra thành từng dòng không được gộp lại thành 1.

# Các loại testcase theo điểm:
- 0.1: Đây là dạng các testcase thực hiện thao tác input, click cơ bản không thực hiện nâng cao. Giới hạn tối đa chỉ 10 testcases. (Ví dụ: Login, Register, Logout)
- 0.15: Đây là các testcase nâng cao hơn thực hiện các thao tác click hay tìm kiếm bằng vòng lặp và có xử lí một số scrip cơ bản. (Ví dụ: Thêm sản phẩm vào giỏ hàng và sau đó kiểm tra giá tiền)
- 0.2: Đây là dạng khó nhất thực hiện logic bao gồm click, input cơ bản để sử dụng vòng lặp và áp dụng logic vào như if/else, while loop, execute script, thuật toán vòng lặp,... (Ví dụ: Kiểm tra tất cả giá của sản phẩm có đang tăng dần hay không và xác nhận)