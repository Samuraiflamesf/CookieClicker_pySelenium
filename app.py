from selenium import webdriver
import time

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "cookies": {
                    "xpath": "/html/body/div[2]/div[2]/div[15]/div[8]/div[1]"
                },
                
                "upgrade":{
                    "xpath": "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                }
            }
        }

        self.driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe")
        #self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def clicar_no_cookie(self):
        self.driver.find_element_by_xpath(self.SITE_MAP ["buttons"]["cookies"]["xpath"]).click()
        
    def pegar_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2

        while not encontrei:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(elemento_atual))
            classes_objeto = self.driver.find_element_by_xpath(objeto).get_attribute("class")

            if not "enabled" in classes_objeto:
                encontrei = True
            else:
                elemento_atual +=1

        return elemento_atual - 1

    def comprar_upgrade(self):
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.pegar_melhor_upgrade()))
        self.driver.find_element_by_xpath(objeto).click()

biscoito = CookieClicker()
biscoito.abrir_site()

i = 0
x = 0

while True:        
    if i % 100 ==  0 and i !=0:
        time.sleep(1)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookie()
    i += 1

    
    
    
    

        
    
    