package com.example.databasebackend.Service;

import com.example.databasebackend.Entity.ChoseMenu;

public interface ChoseDishService {

    void addChose(ChoseMenu choseMenu);

    void deleteChose(Integer s_id, Integer d_id);
}
