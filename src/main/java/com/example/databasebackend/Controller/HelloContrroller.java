package com.example.databasebackend.Controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloContrroller {

    @ResponseBody
    @GetMapping("/Hello")
    public String Hello() {
        return "Hello!";
    }
}
