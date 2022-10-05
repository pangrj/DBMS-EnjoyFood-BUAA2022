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

import java.util.HashMap;
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
                    ChoseMenu choseMenu = new ChoseMenu(s_id, d_id);
                    choseDishService.addChose(choseMenu);
                    ret.put("success", true);
                    ret.put("message", "Chose Success!");
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
                    choseDishService.deleteChose(s_id, d_id);
                    ret.put("success", true);
                    ret.put("message", "Delete Success!");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
            ret.put("success", false);
            ret.put("message", "Chose Error!");
        }
        return ret;
    }

}
