package com.example.databasebackend.Controller;

import com.example.databasebackend.Entity.Dish;
import com.example.databasebackend.Service.DishService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class DishController {
    @Autowired
    private DishService dishService;

    @PostMapping("/searchByName")
    public Map<String, Object> searchByName(@RequestBody Map<String, String> request) {
        String d_name = request.get("d_name");
        Map<String, Object> ret = new HashMap<>();
        List<Dish> dishes = new ArrayList<>();

        try {
            dishes = dishService.searchByName(d_name);
            if (dishes.size() == 0) {
                ret.put("success", false);
                ret.put("message", "No Such Dishes!");
            } else {
                ret.put("success", true);
                ret.put("message", "Find Dishes!");
                ret.put("dishes", dishes);
            }
        } catch (Exception e) {
            e.printStackTrace();
            ret.put("success", false);
            ret.put("message", "Search Error!");
        }
        return ret;
    }

    @ResponseBody
    @GetMapping("/menu")
    public Map<String, Object> menu() {
        Map<String, Object> ret = new HashMap<>();
        List<Dish> dishes = new ArrayList<>();
        try {
            dishes = dishService.showAllDishes();
            ret.put("success", "true!");
            ret.put("message", "初始化菜单界面请求成功!");
            ret.put("dishes", dishes);
        } catch (Exception e) {
            e.printStackTrace();
            ret.put("success", "false");
            ret.put("message", "初始化菜单界面请求错误!");
        }

        return ret;
    }
}
