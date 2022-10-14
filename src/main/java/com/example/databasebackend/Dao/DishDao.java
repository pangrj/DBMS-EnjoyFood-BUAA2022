package com.example.databasebackend.Dao;

import com.example.databasebackend.Entity.Dish;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface DishDao {
    List<Dish> searchByName(String d_name);

    List<Dish> showAllDishes();

    Dish searchById(Integer d_id);

    List<Dish> showNotSelectDishes(Integer s_id);

    List<Dish> showSelectDishes(Integer s_id);
}
