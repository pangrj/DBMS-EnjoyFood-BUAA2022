package com.example.databasebackend.Service;

import com.example.databasebackend.Entity.Dish;

import java.util.List;

public interface DishService {
    List<Dish> searchByName(String d_name);
}
