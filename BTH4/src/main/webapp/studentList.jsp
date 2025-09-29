<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Danh sách Sinh viên</title>
</head>
<body>
<h1>Danh sách Sinh viên</h1>
<table border="1">
    <thead>
    <tr>
        <th>ID</th>
        <th>Tên</th>
        <th>Email</th>
        <th>Điện thoại</th>
        <th>Ngày sinh</th>
        <th>Hành động</th>
    </tr>
    </thead>
    <tbody>
    <c:forEach var="student" items="${students}">
        <tr>
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.email}</td>
            <td>${student.phone}</td>
            <td>${student.dob}</td>
            <td>
                <a href="student?action=edit&id=${student.id}">Chỉnh sửa</a> |
                <a href="student?action=delete&id=${student.id}">Xóa</a>
            </td>
        </tr>
    </c:forEach>
    </tbody>
</table>
<a href="index.jsp">Quay lại trang chủ</a>
</body>
</html>
