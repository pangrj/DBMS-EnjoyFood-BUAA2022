# InfomationPage 设计文档
## 页面架构
InfomationPage 通过在 ChoosePage 调用跳转得到。它本身会调用的组件有RecommendCard。
## 数据流动
InfomationPage 通过 {username, password} 与 ChoosePage 和 LoginPage 沟通。此外，本身维护两个数据结构：用户信息、页面设置信息。
#### 用户信息：
| Name         |   信息   |   类型    | 后端        |
| ------------ | :------: | :-------: | :---       |
| username     |  用户名  |  String   | s_name     |
| id           |   学号   |  int(8)   | s_id       |
| password     |   密码   |  String   | s_password |
| email        | 邮箱地址  |  String  |  s_email   |
| profilePhoto |   头像   |   url ??  | s_photo    |
| gender       |   性别   |   String  | s_gender   |
| position     |   住处   |   String  | s_dorm     |