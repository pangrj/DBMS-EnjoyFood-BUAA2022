<script>
export default {
    setup(){
        
    },
    methods: {
        clickToMain(){

        },
        clickToInfor(){

        },
    }
}
</script>

<template>
    <div>
        <ul class="left">
            <li>
                <el-icon><KnifeFork /></el-icon>
                <span>MainPage</span>
            </li>
            <li>
                <span>MakePlan</span>
            </li>
            <li>
                <span>Enjoy Food !</span>
            </li>
            <li>

            </li>
        </ul>
    </div>
</template>

<style scoped>
.left{
    display: flex;
    align-items: center;
    flex-shrink: 0;
    margin-right: 30px;
}
.li{
    border: 0;
    font-family: inherit;
    font-size: 100%;
    font-weight: 400;
    font-style: normal;
    line-height: 1.25;
    display: list-item;
    text-align: -webkit-match-parent;
}
</style>