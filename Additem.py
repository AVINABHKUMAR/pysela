from selenium import webdriver
path="C:/Users/JAI Krishna/Documents/GitHub/pysela/resource/chromedriver.exe"


driver=webdriver.Chrome(path)
driver.implicitly_wait(20)
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("honor")
driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Honor 20 (Sapphire Blue, 6GB, 128GB Storage): Amazon.in: Electronics":
        driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
        driver.find_element_by_xpath("//*[@id='nav-cart']/span[2]")

    driver.close()
driver.quit()









