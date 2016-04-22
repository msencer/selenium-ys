#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
from config import configs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Order():
    def __init__(self):
        self.USER_NAME = configs().user['email']
        self.PASSWORD = configs().user['password']
        self.ADDRESSID = configs().ys['address']
        self.PAYMENTMETHOD = configs().ys['payment']

    def give(self):
        browser = webdriver.PhantomJS()
        browser.get('http://yemeksepeti.com/ankara')


        username = browser.find_element_by_name("UserName")
        username.send_keys(self.USER_NAME)
        password = browser.find_element_by_name("Password")
        password.send_keys(self.PASSWORD)
        button = browser.find_element_by_id('ys-fastlogin-button')
        button.click()

        wait = WebDriverWait(browser, 10)
        try:
            element = wait.until(EC.presence_of_element_located((By.ID, "user-info")))
        except:
            print "Time out"
            return

        print "Logged in"

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
        var addressId = '%s'
        var paymentMethod = '%s'

        var ysRequest = {"Token":token,"CatalogName":"TR_ANKARA","Culture":"tr-TR","LanguageId":"tr-TR"};
        var checkoutPayload = {'checkoutParameters' : {'IsCheckoutStep' : 'true', 'IsTakeAway' : 'true','BasketId' : basket,'AddressId' : addressId,'IsCampus' : 'true','IsFutureOrder' : 'false','PaymentMethodId' : paymentMethod,'SaveGreen' : 'true'},'ysRequest' : ysRequest};
        var addPayload = {"quantity":"1","categoryName":"b228f939-65e8-48d1-8600-8d421a414d33","productId":"fa44b71e-2027-46e6-8e15-5a59d2b4feac","isFavourite":false,"RestaurantInfo":{"RestaurantCuisines":"Cafe","RestaurantPoints":"H-7,94|S-7,26|L-6,8|T-22|Av-7,3","RestaurantId":"b228f939-65e8-48d1-8600-8d421a414d33","RestaurantName":"Ender Cafe & Restaurant|ODTÜ Teknokent","PrimaryRestaurantName":"","RestaurantIsYsDelivery":"False","RestaurantArea":"ODTÜ Teknokent","RestaurantIsOpen":"True"},"selectedItems":[],"__type":"ProductDetail:#YS.WebServices.Service.DTO.ProductDetail","BasketIsActive":true,"DefaultPrice":"5,00 TL","Description":"","ExtendedPrice":"5,00 TL","FacebookLikeUrl":"http://social.yemeksepeti.com/430241/lp.ys","FacebookShareUrl":"http://social.yemeksepeti.com/430241/lp.ys","FoodReadyInTimeMessage":null,"Id":"fa44b71e-2027-46e6-8e15-5a59d2b4feac","ImagePath":"App_Themes/Default_tr-TR/images/ResimYok.jpg","Name":"Sucuklu Tost","Options":[],"Price":0,"PrimaryRestaurantName":null,"ProductIsOpen":true,"ProductOpenMessage":null,"Quantity":1,"Render":false,"basketId":basket,"catalogName":"TR_ANKARA","ysRequest":ysRequest};

        options.url = 'https://service.yemeksepeti.com/YS.WebServices/OrderService.svc/AddProduct';
        options.data = JSON.stringify(addPayload);
        options.success = function(){};
        //options.success = function(data){checkout(checkoutPayload);},
        setTimeout(function(){$.ajax(options);}, 3000);

        });
        """ % (self.ADDRESSID,self.PAYMENTMETHOD)

        jsres = browser.execute_script("return window.Globals.CurrentState.LoginToken;")
        print 'Login Token : ',jsres
        browser.execute_script(script)
        time.sleep(10)
        browser.refresh()
        browser.save_screenshot('screen.png') 