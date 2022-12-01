# InfomationPage 设计文档
## 页面架构
InfomationPage 通过在 ChoosePage 调用跳转得到。它本身会调用两个页面，分别是 EditInfoPage、SettingsPage。
## 数据流动
InfomationPage 通过 {username, password} 与 ChoosePage 和 LoginPage 沟通。此外，本身维护两个数据结构：用户信息、页面设置信息。
#### 用户信息：
| Name     |   信息   | 类型    |
| -------- | :------: | :----- |
| username |  用户名  | String(8)|
| id       |   学号   | int(8)  |
| password |   密码   | int(8)  |
| email    | 邮箱地址 | String  |
| profilePhoto | 头像 | .jpg    |
