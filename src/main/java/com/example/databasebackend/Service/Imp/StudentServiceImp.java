package com.example.databasebackend.Service.Imp;

import com.example.databasebackend.Dao.StudentDao;
import com.example.databasebackend.Entity.Student;
import com.example.databasebackend.Service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StudentServiceImp implements StudentService {
    @Autowired
    private StudentDao studentDao;

    @Override
    public Student selectById(Integer s_id) {
        return studentDao.selectById(s_id);
    }

    @Override
    public void registerNewStudent(Student studentNew) {
        studentDao.registerNewStudent(studentNew);
    }

    @Override
    public void modifyStudentMessage(Student student) {
        studentDao.modifyStudentMessage(student);
    }
}
