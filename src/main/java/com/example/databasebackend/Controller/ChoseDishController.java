package com.example.databasebackend.Controller;

import com.example.databasebackend.Entity.ChoseMenu;
import com.example.databasebackend.Entity.Dish;
import com.example.databasebackend.Entity.Student;
import com.example.databasebackend.Service.ChoseDishService;
import com.example.databasebackend.Service.DishService;
import com.example.databasebackend.Service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class ChoseDishController {

    @Autowired
    private ChoseDishService choseDishService;
    @Autowired
    private StudentService studentService;
    @Autowired
    private DishService dishService;

    @PostMapping("/choseDish")
    public Map<String, Object> choseDish(@RequestBody Map<String, Integer> request) {
        Integer s_id = request.get("s_id");
        Integer d_id = request.get("d_id");
        List<Dish> dishes = new ArrayList<>();
        Map<String, Object> ret = new HashMap<>();

        try {
            Student student = studentService.selectById(s_id);
            if (student == null) {
                ret.put("success", false);
                ret.put("message", "No Such Student!");
            } else {
                Dish dish = dishService.searchById(d_id);
                if (dish == null) {
                    ret.put("success", false);
                    ret.put("message", "No Such Dish!");
                } else {
                    ChoseMenu existMenu = choseDishService.search(s_id, d_id);
                    if (existMenu != null) {
                        ret.put("success", false);
                        ret.put("message", "Already chose this dish!");
                    }else {
                        ChoseMenu choseMenu = new ChoseMenu(s_id, d_id);

                        choseDishService.addChose(choseMenu);
                        dishes = dishService.showNotSelectDishes(s_id);
                        ret.put("success", true);
                        ret.put("message", "Chose Success!");
                        ret.put("dishes", dishes);
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
            ret.put("success", false);
            ret.put("message", "Chose Error!");
        }
        return ret;
    }

    @PostMapping("/deleteDish")
    public Map<String, Object> deleteDish(@RequestBody Map<String, Integer> request) {
        Integer s_id = request.get("s_id");
        Integer d_id = request.get("d_id");
        List<Dish> dishes = new ArrayList<>();
        Map<String, Object> ret = new HashMap<>();
        try {
            ChoseMenu choseMenu = choseDishService.search(s_id, d_id);
            Student student = studentService.selectById(s_id);
            if (choseMenu == null) {
                ret.put("success", false);
                ret.put("message", "No Such Order!");
            } else {
                choseDishService.deleteChose(s_id, d_id);
                dishes = dishService.showNotSelectDishes(s_id);
                ret.put("success", true);
                ret.put("message", "Delete Success!");
                ret.put("dishes", dishes);
            }
        } catch (Exception e) {
            e.printStackTrace();
            ret.put("success", false);
            ret.put("message", "Chose Error!");
        }
        return ret;
    }

}
