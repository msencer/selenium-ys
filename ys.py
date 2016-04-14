#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )

class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded)


USER_NAME = ''
PASSWORD = ''

browser = webdriver.PhantomJS()
browser.get('http://yemeksepeti.com/ankara')

username = browser.find_element_by_name("UserName")
username.send_keys(USER_NAME)

password = browser.find_element_by_name("Password")
password.send_keys(PASSWORD)

button = browser.find_element_by_id('ys-fastlogin-button')

#with wait_for_page_load(browser):
button.click()

print "Logged in"

#html = browser.page_source
#f = open('afterlogin.html','w+')
#f.write(html.encode('utf8'))
#f.close()

script = """
var options = {
        type: "POST",
        url: '',
        data: '',
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        failure: function(errMsg) {
            alert(errMsg);
        }
};

function checkout(payload){
    options.url = 'https://service.yemeksepeti.com/YS.WebServices/OrderService.svc/Checkout';
    options.data = JSON.stringify(payload);
    options.success = function(data){alert(data);};

    console.log(options);

    setTimeout(function(){$.ajax(options);}, 3000);
}

$(document).ready(function () {
var token = window.Globals.CurrentState.LoginToken;
var basket = window.Globals.CurrentState.BasketId;
var addressId = '62cfe1da-359d-4f6a-92e8-404048cba489'
var paymentMethod = 'b93e2cf9-5d58-494e-b69a-3a7882f4e747'

var ysRequest = {"Token":token,"CatalogName":"TR_ANKARA","Culture":"tr-TR","LanguageId":"tr-TR"};
var checkoutPayload = {'checkoutParameters' : {'IsCheckoutStep' : 'true', 'IsTakeAway' : 'true','BasketId' : basket,'AddressId' : addressId,'IsCampus' : 'true','IsFutureOrder' : 'false','PaymentMethodId' : paymentMethod,'SaveGreen' : 'true'},'ysRequest' : ysRequest};
var addPayload = {"quantity":"1","categoryName":"b228f939-65e8-48d1-8600-8d421a414d33","productId":"fa44b71e-2027-46e6-8e15-5a59d2b4feac","isFavourite":false,"RestaurantInfo":{"RestaurantCuisines":"Cafe","RestaurantPoints":"H-7,94|S-7,26|L-6,8|T-22|Av-7,3","RestaurantId":"b228f939-65e8-48d1-8600-8d421a414d33","RestaurantName":"Ender Cafe & Restaurant|ODTÜ Teknokent","PrimaryRestaurantName":"","RestaurantIsYsDelivery":"False","RestaurantArea":"ODTÜ Teknokent","RestaurantIsOpen":"True"},"selectedItems":[],"__type":"ProductDetail:#YS.WebServices.Service.DTO.ProductDetail","BasketIsActive":true,"DefaultPrice":"5,00 TL","Description":"","ExtendedPrice":"5,00 TL","FacebookLikeUrl":"http://social.yemeksepeti.com/430241/lp.ys","FacebookShareUrl":"http://social.yemeksepeti.com/430241/lp.ys","FoodReadyInTimeMessage":null,"Id":"fa44b71e-2027-46e6-8e15-5a59d2b4feac","ImagePath":"App_Themes/Default_tr-TR/images/ResimYok.jpg","Name":"Sucuklu Tost","Options":[],"Price":0,"PrimaryRestaurantName":null,"ProductIsOpen":true,"ProductOpenMessage":null,"Quantity":1,"Render":false,"basketId":basket,"catalogName":"TR_ANKARA","ysRequest":ysRequest};

options.url = 'https://service.yemeksepeti.com/YS.WebServices/OrderService.svc/AddProduct';
options.data = JSON.stringify(addPayload);
options.success = function(data){checkout(checkoutPayload);},
setTimeout(function(){$.ajax(options);}, 3000);

});
"""
browser.execute_script(script)
print "Script yerlestirildi"
time.sleep(20)