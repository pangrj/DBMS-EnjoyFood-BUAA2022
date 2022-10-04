package com.example.databasebackend.Entity;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Student {
    @Id
    private Integer s_id;
    private String s_password;
    private String s_name;
    private String s_dorm;
    private String s_gender;

    public Student(Integer s_id, String s_password) {
        this.s_id = s_id;
        this.s_password = s_password;
        this.s_name = null;
        this.s_dorm = null;
        this.s_gender = null;
    }


    public Student() {

    }



    public Integer getS_id() {
        return s_id;
    }

    public void setS_id(Integer s_id) {
        this.s_id = s_id;
    }

    public String getS_password() {
        return s_password;
    }

    public void setS_password(String s_password) {
        this.s_password = s_password;
    }

    public String getS_name() {
        return s_name;
    }

    public void setS_name(String s_name) {
        this.s_name = s_name;
    }

    public String getS_dorm() {
        return s_dorm;
    }

    public void setS_dorm(String s_dorm) {
        this.s_dorm = s_dorm;
    }

    public String getS_gender() {
        return s_gender;
    }

    public void setS_gender(String s_gender) {
        this.s_gender = s_gender;
    }


}
