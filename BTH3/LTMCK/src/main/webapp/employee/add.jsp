<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thêm Nhân Viên</title>
</head>
<body>
    <h1>Thêm Nhân Viên</h1>
    <form action="insert" method="post">
        <label>Tên:</label><br>
        <input type="text" name="name" required><br>
        <label>Email:</label><br>
        <input type="email" name="email"><br>
        <label>ID Phòng Ban:</label><br>
        <input type="number" name="departmentId" required><br><br>
        <input type="submit" value="Thêm">
    </form>
    <br>
    <a href="list">Quay lại danh sách</a>
</body>
</html>
