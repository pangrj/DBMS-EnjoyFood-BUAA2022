
<script lang="ts">
export default {
    data(){
        return {
        }
    },
    methods: {
    }
}

import { ref } from 'vue'

const isCollapse = ref(true)
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<template>
    <div class="wholePage">
    <el-container>
      <el-header>
        Edit Your Infomation
        </el-header>
      <el-container>
        <!--el-aside width="200px">
            Aside
            </el-aside-->
        <el-main>
            <el-radio-group v-model="isCollapse" style="margin-bottom: 20px" align="left">
                <el-radio-button :label="false">expand</el-radio-button>
                <el-radio-button :label="true">collapse</el-radio-button>
            </el-radio-group>
            <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                :collapse="isCollapse"
                @open="handleOpen"
                @close="handleClose"
            >
            <el-sub-menu index="1">
            <template #title>
            <el-icon><location /></el-icon>
            <span>Edit Avater</span>
            </template>
            <el-menu-item-group>
            <template #title><span>Group One</span></template>
                <el-menu-item index="1-1">item one</el-menu-item>
                <el-menu-item index="1-2">item two</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="Group Two">
                <el-menu-item index="1-3">item three</el-menu-item>
            </el-menu-item-group>
            <el-sub-menu index="1-4">
                <template #title><span>item four</span></template>
                <el-menu-item index="1-4-1">item one</el-menu-item>
            </el-sub-menu>
            </el-sub-menu>
            <el-menu-item index="2">
                <el-icon><icon-menu /></el-icon>
                <template #title>Navigator Two</template>
                </el-menu-item>
                <el-menu-item index="3" disabled>
                <el-icon><document /></el-icon>
                <template #title>Navigator Three</template>
                </el-menu-item>
                <el-menu-item index="4">
                <el-icon><setting /></el-icon>
                <template #title>Navigator Four</template>
                </el-menu-item>
            </el-menu>
            </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.wholePage{
  padding-top: 3%;
}
</style>