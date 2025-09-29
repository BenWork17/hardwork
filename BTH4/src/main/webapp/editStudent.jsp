<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chỉnh sửa Sinh viên</title>
</head>
<body>
<h1>Chỉnh sửa Sinh viên</h1>
<form action="student" method="post">
    <input type="hidden" name="action" value="update">
    <input type="hidden" name="id" value="${student.id}">

    <label for="name">Tên: </label>
    <input type="text" id="name" name="name" value="${student.name}" required><br><br>

    <label for="email">Email: </label>
    <input type="email" id="email" name="email" value="${student.email}" required><br><br>

    <label for="phone">Số điện thoại: </label>
    <input type="text" id="phone" name="phone" value="${student.phone}" required><br><br>

    <label for="dob">Ngày sinh: </label>
    <input type="date" id="dob" name="dob" value="${student.dob}" required><br><br>

    <input type="submit" value="Cập nhật Sinh viên">
</form>
<a href="index.jsp">Quay lại trang chủ</a>
</body>
</html>
