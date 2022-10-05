package com.example.databasebackend.Service.Imp;

import com.example.databasebackend.Dao.ChoseDishDao;
import com.example.databasebackend.Entity.ChoseMenu;
import com.example.databasebackend.Service.ChoseDishService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ChoseDishServiceImp implements ChoseDishService {

    @Autowired
    private ChoseDishDao choseDishDao;

    @Override
    public void addChose(ChoseMenu choseMenu) {
        choseDishDao.addChose(choseMenu);
    }

    @Override
    public void deleteChose(Integer s_id, Integer d_id) {
        choseDishDao.deleteChose(s_id, d_id);
    }
}
