from appium import webdriver

desired_cap = {

    "appium:deviceName": "emulator-5554",
    "appium:platformName": "Android",
    "appium:appPackage": "com.july.cricinfo",
    "appium:appWaitActivity": "com.cricinfo.app.android.activities.CiMainActivity",
    "appium:app": "C:\\Users\\Admin\\Downloads\\com.july.cricinfo.apk"
}

driver = webdriver.Remote("https://localhost:4723/wd/hub", desired_cap)