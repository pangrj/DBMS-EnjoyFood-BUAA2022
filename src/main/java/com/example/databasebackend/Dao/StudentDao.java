package com.example.databasebackend.Dao;

import com.example.databasebackend.Entity.Student;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface StudentDao {

    public Student selectById(Integer s_id);

    public void registerNewStudent(Student studentNew);

    void modifyStudentMessage(Student student);
}
