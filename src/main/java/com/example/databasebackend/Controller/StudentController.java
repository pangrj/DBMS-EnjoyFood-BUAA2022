package com.example.databasebackend.Controller;

import com.example.databasebackend.Entity.Student;
import com.example.databasebackend.Service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class StudentController {
    @Autowired
    private StudentService studentService;

    @PostMapping("/login")
    public Map<String, Object> login(@RequestBody Map<String, Object> id2password) {
        Integer s_id = (Integer) (id2password.get("s_id"));
        String s_password = (String) id2password.get("s_password");
        Map<String, Object> ret = new HashMap<>();

        try {
            Student student = studentService.selectById(s_id);

            if (student != null) {
                if (student.getS_password().equals(s_password)) {
                    ret.put("success", true);
                    ret.put("message", "login success!");
                } else {
                    ret.put("success", false);
                    ret.put("message", "账号或密码错误！");
                }
            } else {
                Student studentNew = new Student(s_id, s_password);

                studentService.registerNewStudent(studentNew);
                ret.put("success", true);
                ret.put("message", "login success!");
            }
        } catch (Exception e) {
            e.printStackTrace();
            ret.put("success", false);
            ret.put("message", "登录或注册失败！");
        }

        return ret;
    }
}
