package com.example.databasebackend.Service.Imp;

import com.example.databasebackend.Dao.DishDao;
import com.example.databasebackend.Entity.Dish;
import com.example.databasebackend.Service.DishService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DishServiceImp implements DishService {
    @Autowired
    private DishDao dishDao;

    @Override
    public List<Dish> searchByName(String d_name) {
        return dishDao.searchByName(d_name);
    }

    @Override
    public List<Dish> showAllDishes() {
        return dishDao.showAllDishes();
    }

    @Override
    public Dish searchById(Integer d_id) {
        return dishDao.searchById(d_id);
    }
}
