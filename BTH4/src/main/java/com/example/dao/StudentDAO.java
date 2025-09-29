package com.example.dao;

import com.example.model.Student;

import java.sql.*;
import java.util.*;

public class StudentDAO {
    private static final String URL = "jdbc:mysql://localhost:3306/student_management";
    private static final String USER = "root";  // Thay bằng username của bạn
    private static final String PASSWORD = "root";  // Thay bằng password của bạn

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public static Student getStudentById(int id) throws SQLException {
        String query = "SELECT * FROM students WHERE id = ?";
        try (Connection conn = getConnection();
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, id);
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return new Student(rs.getInt("id"), rs.getString("name"), rs.getString("email"), rs.getString("phone"), rs.getString("dob"));
                } else {
                    // Nếu không tìm thấy sinh viên, trả về null hoặc có thể ném exception
                    return null;  // Hoặc throw new SQLException("Student not found with ID: " + id);
                }
            }
        }
    }


    public static List<Student> getAllStudents() throws SQLException {
        List<Student> students = new ArrayList<>();
        String query = "SELECT * FROM students";
        try (Connection conn = getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            while (rs.next()) {
                students.add(new Student(rs.getInt("id"), rs.getString("name"), rs.getString("email"), rs.getString("phone"), rs.getString("dob")));
            }
        }
        return students;
    }

    public static int addStudent(Student student) throws SQLException {
        String query = "INSERT INTO students (name, email, phone, dob) VALUES (?, ?, ?, ?)";
        try (Connection conn = getConnection();
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, student.getName());
            stmt.setString(2, student.getEmail());
            stmt.setString(3, student.getPhone());
            stmt.setString(4, student.getDob());
            return stmt.executeUpdate();
        }
    }

    public static int updateStudent(Student student) throws SQLException {
        String query = "UPDATE students SET name = ?, email = ?, phone = ?, dob = ? WHERE id = ?";
        try (Connection conn = getConnection();
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, student.getName());
            stmt.setString(2, student.getEmail());
            stmt.setString(3, student.getPhone());
            stmt.setString(4, student.getDob());
            stmt.setInt(5, student.getId());
            return stmt.executeUpdate();
        }
    }

    public static int deleteStudent(int id) throws SQLException {
        String query = "DELETE FROM students WHERE id = ?";
        try (Connection conn = getConnection();
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, id);
            return stmt.executeUpdate();
        }
    }
}
