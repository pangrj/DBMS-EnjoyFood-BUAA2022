<script>

import {ref} from 'vue'

export default({
    props: {
        information:{
                u_name: String,
                u_id: String,
                u_password: String,
                u_position: String,
                u_gender: String,
                u_email : String,
                u_photo: File,
                u_age: 0,
                u_height: 0,
                u_weight: 0,
            }
    },
    setup(props) {
        const gender = ref("")
        if(props.information.u_gender=="True"){
            gender.value = "male";
        }else{
            gender.value = "female";
        }
        return {gender}
    },
})


</script>

<template>
<div class="Body">
     <el-descriptions
        class="margin-top"
        title="Information"
        :column="3"
        size="Large"
        border
    >
    <template #extra>
      <el-button type="primary">Operation</el-button>
    </template>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <user />
          </el-icon>
          Username
        </div>
      </template>
      <span>{{information.u_name}}</span>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <Message />
          </el-icon>
            Emial
        </div>
      </template>
      <span>{{information.u_email}}</span>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <Male />
          </el-icon>
            Gender
        </div>
      </template>
      <span>{{gender}}</span>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <location />
          </el-icon>
          Position
        </div>
      </template>
      <span>{{information.u_position}}</span>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <tickets />
          </el-icon>
          Remarks
        </div>
      </template>
      <el-tag size="small">School</el-tag>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <office-building />
          </el-icon>
          Id
        </div>
      </template>
      <span>{{information.u_id}}</span>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <office-building />
          </el-icon>
          Age
        </div>
      </template>
      <span>{{information.u_age}}</span>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <office-building />
          </el-icon>
          Height
        </div>
      </template>
      <span>{{information.u_height}}</span>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <div class="cell-item">
          <el-icon :style="iconStyle">
            <office-building />
          </el-icon>
          Weight
        </div>
      </template>
      <span>{{information.u_weight}}</span>
    </el-descriptions-item>
  </el-descriptions>
  </div>
</template>

<style scoped>
.body{
  padding-bottom: 5%;
}
.el-descriptions {
  margin-top: 20px;
}
.cell-item {
  display: flex;
  align-items: center;
}
.margin-top {
  margin-top: 20px;
}
</style>