# coding=utf-8
from behave import *
import pageObject.BingHomePage as HomePage
from pageObject import searchPage
from pageObject import signPage

@Step (u'我在bing的首页')
def step_impl(context):
    HomePage.Open(context)

@Step (u'我搜索"{keyword}"')
def step_impl(context,keyword):
    HomePage.Search_TextBox(context).send_keys(keyword)
    HomePage.Submit_Button(context).click()


@Step (u'我应该看见包含"{keyword}"的搜索结果')
def step_impl(context,keyword):
    assert searchPage.page_title(context).__contains__(keyword)

@Step(u'用"{user},{password}"登录bing')
def step_impl(context,user,password):
    HomePage.Signin_Link(context).click()

    signPage.wait_name(context)
    signPage.name_TextBox(context).send_keys(user)
    signPage.next_button(context).click()

    signPage.wait_password(context)
    signPage.password_TextBox(context).send_keys(password)
    signPage.login_button(context).click()

@Step(u'首页显示我的登录名是"{username}"')
def step_impl(context,username):
    assert HomePage.name_link(context).text.__contains__(username)