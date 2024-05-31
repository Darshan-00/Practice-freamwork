class BasePageLocators:
    useremail = "xpath-->//input[@id='login_email']"
    password = "xpath-->//input[@id='login_password']"
    signin_button = "xpath-->//button[@type='submit']"
    title = "xpath-->//h3[@class='ant-typography css-1ihz8o1']"
    header = "xpath-->//span[text()='<<report_type>>']"
    brand_dropdown = "xpath-->(//span[@class='ant-select-selection-item'])[1]"
    brand_filter = "xpath-->//div[@title='<<brand_name>>']"
    year_filter = "xpath-->(//span[@class='ant-select-selection-item'])[2]"
