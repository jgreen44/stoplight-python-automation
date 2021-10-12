from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


def main():
    js = """
    const newDiv = document.createElement('div');
    newDiv.setAttribute('id', 'timer');
    newDiv.setAttribute('style', 'font-size: 16px; text-align: center; color: red; font-weight: 600;');

    const buttonDiv = document.getElementsByClassName('bp3-button')[0];
    buttonDiv.parentNode.insertBefore(newDiv, buttonDiv.nextSibling);

    
    function timer(){
    var sec = 3600;
    var timer = setInterval(function(){
        document.getElementById('timer').innerHTML='You have '+ sec + ' seconds left to enter the code!';
        sec--;
        if (sec < 0) {
            clearInterval(timer);
        }
    }, 1000);
}
timer();

"""
    driver = webdriver.Chrome('./chromedriver')
    wait = WebDriverWait(driver, 3600)
    driver.get("http://stoplight-local.com:8080")

    email = driver.find_element_by_id('email')
    email.send_keys('test@test.com')

    continue_button = driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/form/button')
    continue_button.click()

    wait.until(presence_of_element_located((By.XPATH, '//*[@id="companyName"]')))

    company_name = driver.find_element_by_xpath('//*[@id="companyName"]')
    company_name.send_keys('test')

    workspace_focus = driver.find_element_by_xpath('//*[@id="workspace"]')
    workspace_focus.click()

    next_button = driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/form/button')
    next_button.click()

    wait.until(presence_of_element_located((By.XPATH, '//*[@id="code"]')))
    driver.execute_script(js)

    wait.until(presence_of_element_located((By.XPATH, '//*[@id="firstName"]')))

    first_name = driver.find_element_by_xpath('//*[@id="firstName"]')
    first_name.send_keys('test')

    second_name = driver.find_element_by_xpath('//*[@id="lastName"]')
    second_name.send_keys('user')

    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('asdf1234')

    select_role = Select(driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/form/div[3]/div[2]/div/div/select'))
    select_role.select_by_value('fullstack_developer')

    select_company = Select(driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/form/div[3]/div[3]/div/div/select'))
    select_company.select_by_value('1')

    select_me = Select(driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/form/div[3]/div[4]/div[2]/div/select'))
    select_me.select_by_value('with_git')

    continue_button = driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/form/button')
    continue_button.click()

    wait.until(presence_of_element_located(
        (By.XPATH, '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/div[2]/div[2]/div[2]')))

    choose_use_case = driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/div[2]/div[2]/div[2]')
    choose_use_case.click()

    go_to_workspace = driver.find_element_by_xpath(
        '//*[@id="mosaic-provider-react-aria-1-1"]/div/div/div[2]/main/div/div[2]/div[3]/button/span')
    go_to_workspace.click()

    while True:
        pass


if __name__ == '__main__':
    main()
