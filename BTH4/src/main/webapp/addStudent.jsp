<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thêm Sinh viên</title>
</head>
<body>
<h1>Thêm Sinh viên Mới</h1>
<form action="student" method="post">
    <input type="hidden" name="action" value="add">
    <label for="name">Tên: </label>
    <input type="text" id="name" name="name" required><br><br>

    <label for="email">Email: </label>
    <input type="email" id="email" name="email" required><br><br>

    <label for="phone">Số điện thoại: </label>
    <input type="text" id="phone" name="phone" required><br><br>

    <label for="dob">Ngày sinh: </label>
    <input type="date" id="dob" name="dob" required><br><br>

    <input type="submit" value="Thêm Sinh viên">
</form>
<a href="index.jsp">Quay lại trang chủ</a>
</body>
</html>
