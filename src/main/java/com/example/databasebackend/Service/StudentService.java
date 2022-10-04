package com.example.databasebackend.Service;

import com.example.databasebackend.Entity.Student;

public interface StudentService {
    public Student selectById(Integer s_id);

    public void registerNewStudent(Student studentNew);
}
