package com.example.serverlet;

import com.example.dao.StudentDAO;
import com.example.model.Student;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
import java.sql.*;
import java.util.*;


public class StudentServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if (action == null) action = "list";

        try {
            switch (action) {
                case "add":
                    request.getRequestDispatcher("addStudent.jsp").forward(request, response);
                    break;
                case "edit":
                    int id = Integer.parseInt(request.getParameter("id"));
                    Student student = StudentDAO.getStudentById(id);
                    request.setAttribute("student", student);
                    request.getRequestDispatcher("editStudent.jsp").forward(request, response);
                    break;
                case "delete":
                    id = Integer.parseInt(request.getParameter("id"));
                    StudentDAO.deleteStudent(id);
                    response.sendRedirect("student?action=list");
                    break;
                default:
                    List<Student> students = StudentDAO.getAllStudents();
                    request.setAttribute("students", students);
                    request.getRequestDispatcher("studentList.jsp").forward(request, response);
                    break;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");

        try {
            if ("add".equals(action)) {
                String name = request.getParameter("name");
                String email = request.getParameter("email");
                String phone = request.getParameter("phone");
                String dob = request.getParameter("dob");

                Student student = new Student(0, name, email, phone, dob);
                StudentDAO.addStudent(student);
                response.sendRedirect("student?action=list");
            } else if ("update".equals(action)) {
                int id = Integer.parseInt(request.getParameter("id"));
                String name = request.getParameter("name");
                String email = request.getParameter("email");
                String phone = request.getParameter("phone");
                String dob = request.getParameter("dob");

                Student student = new Student(id, name, email, phone, dob);
                StudentDAO.updateStudent(student);
                response.sendRedirect("student?action=list");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
