<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="model.Employee" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Cập Nhật Nhân Viên</title>
</head>
<body>
    <h1>Cập Nhật Nhân Viên</h1>
    <form action="update" method="post">
        <input type="hidden" name="id" value="<%= request.getParameter("id") %>">
        <label>Tên:</label><br>
        <input type="text" name="name" required><br>
        <label>Email:</label><br>
        <input type="email" name="email"><br>
        <label>ID Phòng Ban:</label><br>
        <input type="number" name="departmentId" required><br><br>
        <input type="submit" value="Cập nhật">
    </form>
    <br>
    <a href="list">Quay lại danh sách</a>
</body>
</html>
