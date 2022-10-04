package com.example.databasebackend.Service.Imp;

import com.example.databasebackend.Entity.Dish;
import com.example.databasebackend.Service.DishService;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DishServiceImp implements DishService {
    @Override
    public List<Dish> searchByName(String d_name) {
        return null;
    }
}
