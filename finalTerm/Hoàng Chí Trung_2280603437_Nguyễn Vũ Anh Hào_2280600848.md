

| Test Case ID | Test Description | Author | Marks |
| :---: | :---: | :---: | :---: |
| 00 | Verify Account Register | Nguyễn Vũ Anh Hào |  |
| 01 | Verify Login Functionality | Nguyễn Vũ Anh Hào |  |
| 02 | Verify Logout Functionality | Nguyễn Vũ Anh Hào |  |
| 03 | Verify Search Functionality  | Hoàng Chí Trung |  |
| 04 | Verify Shopping Cart Total Calculation  | Hoàng Chí Trung |  |
| 05 | Verify Product Removal from Cart | Hoàng Chí Trung |  |
| 06 | Verify Product Sorting (Price: High to Low) | Hoàng Chí Trung |  |
| 07 | Verify Product Quantity Added to Shopping Cart | Nguyễn Vũ Anh Hào |  |
| 08 | Verify Product Comparison Functionality | Nguyễn Vũ Anh Hào |  |
| 09 | Verify Warranty Lookup  | Hoàng Chí Trung |  |
| 10 | Verify video  | Nguyễn Vũ Anh Hào |  |

**Details Test Scenarios**

| TC ID | Test Steps | Expected Result |
| :---- | ----- | :---- |
|  | **Verify Account Registration Functionality** 1.Navigate to: anphatpc.com.vn 2\. Click ‘Đăng ký’ 3\. Enter account information as follows: Field Value Địa chỉ email haokun5500@gmail.com Mật khẩu hao123456 Nhập lại mật khẩu hao123456 Họ và tên Vũ Anh Hào Giới tính Nam Tỉnh/Tp TP HCM Địa chỉ nhận hàng TP HCM Điện thoại di động 012345678 4\. Click ‘Đăng kí’ 5\. Verify the registration success message.  | The system displays the message: ‘Đăng kí thành công’ |
|  | **Verify Login Functionality** 1\. Navigate to: anphatpc.com.vn 2\. Click ‘Đăng nhập’. 3\. Enter login credentials: Field Value Email đăng nhập haokun5500@gmail.com Mật khẩu hao123456  4\. Click ‘Đăng nhập’ button. 5\. Verify successful login status. | The ‘Đăng Nhập’ button is disappear (indicating successful login).  |
|  | **Verify Logout Functionality** 1\. Navigate to: anphatpc.com.vn 2\. Click the user account 3.click the log out 3\. Verify the logout status.  | The Log out button is no longer displayed.  |
|  | **Verify Search Functionality** Navigate to: [anphatpc.com.vn](http://anphatpc.com.vn) Enter 'RTX 4060' into the search bar. Click the Search icon or press Enter. Click product to open product details Verify that all products must contain the keyword. | In the product details must contain the keyword ‘RTX 4060’ |
|  | **Verify Shopping Cart Total Calculation** Navigate to: anphatpc.com.vn Add products to the Cart. Navigate to the Cart page. Capture unit prices and calculate sum via executeScript. Compare sum with 'Total Amount' displayed. | The total payment amount displayed must match 100% with the accumulated sum of individual item prices. |
|  | **Verify Product Removal from Cart** Navigate to: anphatpc.com.vn Add product to cart. Navigate to the cart page. Click “XÓA GIỎ HÀNG” button. | The product is removed from the cart; the system displays "Có 0 sản phẩm trong giỏ hàng" |
|  | **Verify Product Sorting (Price: High to Low)** Navigate to: anphatpc.com.vn Navigate to “Laptop Gaming \- Đồ Họa” category. Select “Còn hàng” and “Giá giảm dần”. Compare the price of 1st and 2nd products | The price of the 1st product must be greater than or equal to the 2nd product. |
|  | **Verify Product Quantity Added to Shopping Cart** Navigate to: [anphatpc.com.vn](http://anphatpc.com.vn) Select menu **Apple.** Add available products to the shopping cart. Verify quantity displayed on the homepage. | The cart quantity displayed matches the number of products added. |
|  | **Verify Product Comparison Functionality** Navigate to: [anphatpc.com.vn](http://anphatpc.com.vn) Navigate to "Apple". Select 2 different products for comparison. Click the "SO SÁNH NGAY" button. Verify that the comparison display all the product information | The Comparison Page displays a detailed spec table. Data Consistency: The product names in the table match exactly with the selected items. |
|  | **Verify Warranty Lookup**  Navigate to: [anphatpc.com.vn](http://anphatpc.com.vn) Click “Tra cứu bảo hành” Select “Tra theo số điện thoại” Enter your phone number Verify the warranty information return | Website must announce that they don’t recognize or the information is invalid |
|  | **Verify video**  Navigate to: [anphatpc.com.vn](http://anphatpc.com.vn) Click “Video” button Verify that the button will redirect youtube page of anphatpc. | Redirect or popup a youtube page of anphatpc |
|  | **Verify Quick View Functionality** Navigate to: [anphatpc.com.vn](http://anphatpc.com.vn) Navigate to a product category (e.g., "Laptop"). Hover the mouse over a specific product item. Verify that the quick info popup (tooltip/summary box) becomes visible. Check if the technical specifications (CPU, RAM, SSD, etc.) are displayed inside the popup. | The quick info box must appear smoothly and contain non-empty technical details matching the product. |
|  | **Verify Custom PC Build Total Price Calculation** Navigate to: [anphatpc.com.vn](http://anphatpc.com.vn) Click “Xây dựng cấu hình PC” Select PC components. Verify that the sum of the components fit with the web calculated. | The total payment amount displayed must match 100% with the accumulated sum of individual item prices. |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

