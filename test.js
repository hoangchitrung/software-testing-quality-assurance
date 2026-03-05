// Mô phỏng các biến lấy từ Selenium IDE
let accmulatedTotal = 1; // Tương đương dòng khởi tạo return 0
let currentPrice = "$799.00"; // Giá trị lấy từ storeText

// Logic tính toán bạn đang dùng trong executeScript
let result = (Number(accmulatedTotal) || 0) + Number(currentPrice.replace(/[^0-9.]/g, ""));

console.log("--- KẾT QUẢ TEST ---");
console.log("Giá trị sau khi lọc số:", currentPrice.replace(/[^0-9.]/g, ""));
console.log("Tổng cộng dồn:", result, typeof result);