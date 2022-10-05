package com.example.databasebackend.Entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class ChoseMenu {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)//自动生成，依次递增
    private Integer id;

    private Integer s_id;
    private Integer d_id;

    private Integer score;
    private static Integer id_ = 0;

    public ChoseMenu(Integer s_id, Integer d_id) {
        this.id = id_++;
        this.s_id = s_id;
        this.d_id = d_id;
        this.score = 0;
    }

    public ChoseMenu() {
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getS_id() {
        return s_id;
    }

    public void setS_id(Integer s_id) {
        this.s_id = s_id;
    }

    public Integer getD_id() {
        return d_id;
    }

    public void setD_id(Integer d_id) {
        this.d_id = d_id;
    }

    public Integer getScore() {
        return score;
    }

    public void setScore(Integer score) {
        this.score = score;
    }
}
