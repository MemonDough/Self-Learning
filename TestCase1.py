from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap = {
    "deviceName": "1318a8ab0505",
    "platformName": "Android",
    "appPackage": "com.july.cricinfo",
    "appWaitActivity": "com.cricinfo.app.android.activities.CiMainActivity",
    "app": "C:\\Users\\Admin\\Downloads\\com.july.cricinfo.apk"

}


driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
print("Work Successfully |Test Successfully|")

time.sleep(15)

selectscore = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View")
selectscore.click()


time.sleep(10)

selectlast = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[5]/android.widget.TextView")
selectlast.click()

time.sleep(25)

driver.quit()

