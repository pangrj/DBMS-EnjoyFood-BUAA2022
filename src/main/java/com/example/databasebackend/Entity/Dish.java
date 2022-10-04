package com.example.databasebackend.Entity;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Dish {
    @Id
    private Integer d_id;
    private String d_name;
    private String d_category;
    private String d_cuisine;
    private Integer d_calories;
    private Integer d_price;

    public Dish(Integer d_id,
                String d_name,
                String d_category,
                String d_cuisine,
                Integer d_calories,
                Integer d_price) {
        this.d_id = d_id;
        this.d_name = d_name;
        this.d_category = d_category;
        this.d_cuisine = d_cuisine;
        this.d_calories = d_calories;
        this.d_price = d_price;
    }

    public Dish() {
    }

    public Integer getD_id() {
        return d_id;
    }

    public void setD_id(Integer d_id) {
        this.d_id = d_id;
    }

    public String getD_name() {
        return d_name;
    }

    public void setD_name(String d_name) {
        this.d_name = d_name;
    }

    public String getD_category() {
        return d_category;
    }

    public void setD_category(String d_category) {
        this.d_category = d_category;
    }

    public String getD_cuisine() {
        return d_cuisine;
    }

    public void setD_cuisine(String d_cuisine) {
        this.d_cuisine = d_cuisine;
    }

    public Integer getD_calories() {
        return d_calories;
    }

    public void setD_calories(Integer d_calories) {
        this.d_calories = d_calories;
    }

    public Integer getD_price() {
        return d_price;
    }

    public void setD_price(Integer d_price) {
        this.d_price = d_price;
    }
}
