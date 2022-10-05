package com.example.databasebackend.Dao;

import com.example.databasebackend.Entity.ChoseMenu;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface ChoseDishDao {
    void addChose(ChoseMenu choseMenu);

    void deleteChose(Integer s_id, Integer d_id);
}
