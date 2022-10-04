package com.example.databasebackend.Dao;

import com.example.databasebackend.Entity.Dish;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface DishDao {
    List<Dish> searchByName(String d_name);
}
