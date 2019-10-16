# language: zh-CN

功能: 测试bing首页的登录与搜索功能
  1、用户在bing首页登录后，首页相应位置会显示用户昵称
  2、用户在搜索关键字的时候，在搜索页面title中会包含关键字本身

  场景大纲: 登录bing首页
    当我在bing的首页
    假如用"<email>,<password>"登录bing
    那么首页显示我的登录名是"<username>"
    例子:
    | email| password| username|

    #| 邮箱或手机号| 密码| 登录时显示的用户名 |

  场景大纲: 搜索多个关键字
    当我在bing的首页
    假如我搜索"<keyword>"
    那么我应该看见包含"<result>"的搜索结果
    例子:
    | keyword | result |
    | game    | game    |
