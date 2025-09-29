<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.List" %>
<%@ page import="model.Employee" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Danh sách nhân viên</title>
</head>
<body>
    <h1>Danh sách nhân viên</h1>
    <a href="add.jsp">Thêm nhân viên mới</a>
    <table border="1">
        <tr>
            <th>ID</th><th>Tên</th><th>Email</th><th>Phòng ban</th><th>Hành động</th>
        </tr>
        <%
            List<Employee> list = (List<Employee>) request.getAttribute("listEmployee");
            for (Employee emp : list) {
        %>
        <tr>
            <td><%= emp.getId() %></td>
            <td><%= emp.getName() %></td>
            <td><%= emp.getEmail() %></td>
            <td><%= emp.getDepartmentId() %></td>
            <td>
                <a href="update.jsp?id=<%= emp.getId() %>">Sửa</a> |
                <a href="delete?id=<%= emp.getId() %>">Xóa</a>
            </td>
        </tr>
        <% } %>
    </table>
</body>
</html>
