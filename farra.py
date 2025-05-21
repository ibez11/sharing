from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup headless options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Aktifkan ini jika tidak ingin menampilkan GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inisialisasi driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Akses URL
url = "https://upoy-ton.bio-matrix.com/#tgWebAppData=user%3D%257B%2522id%2522%253A7680719943%252C%2522first_name%2522%253A%2522%25F0%259F%258C%2595%2524iPoY%2522%252C%2522last_name%2522%253A%2522Syafiq%2522%252C%2522username%2522%253A%2522SyafiqJafar%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252Fg7aE1sbSKgFG3RR9lOm97Fpfbo0IRya0mgE8cEwGgeyy0JiAHAl8LGHWgmFPohgo.svg%2522%257D%26chat_instance%3D8202730045201078548%26chat_type%3Dsender%26auth_date%3D1747215544%26signature%3D0UXD4syxu7X-DdShkt-Z0LtrXAQDwtn-4w4nB98YaZfENMM3EMmgvoQP2TPV5AAOogjO2hAlmiwNgP_YOHU3DA%26hash%3D5ae724f1224dd5c5a612d205ffc75fced69d03e56463265a5b62b745992d4b81&tgWebAppVersion=8.0&tgWebAppPlatform=web&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22button_color%22%3A%22%233390ec%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23707579%22%2C%22link_color%22%3A%22%2300488f%22%2C%22secondary_bg_color%22%3A%22%23f4f4f5%22%2C%22text_color%22%3A%22%23000000%22%2C%22header_bg_color%22%3A%22%23ffffff%22%2C%22accent_text_color%22%3A%22%233390ec%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22section_header_text_color%22%3A%22%233390ec%22%2C%22subtitle_text_color%22%3A%22%23707579%22%2C%22destructive_text_color%22%3A%22%23df3f40%22%7D"
driver.get(url)

# Tunggu loading halaman
time.sleep(0.05)
print("Auto-click mulai berjalan setiap 5 detik... Tekan CTRL+C untuk berhenti.")

wait = WebDriverWait(driver, 10)

try:
    while True:
        try:
            print("Mencari tombol...")

            # Tunggu sampai tombol muncul dan bisa diklik
            button = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[contains(@class, 'flex') and contains(@class, 'select-none') and contains(@class, 'relative') and contains(@class, 'justify-center') and contains(@class, 'overflow-visible') and contains(@class, 'w-full') and contains(@class, 'h-full') and contains(@class, 'border')]"
            )))
            
            print("Button ditemukan!")

            # Scroll ke posisi tombol
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(1)

            # Klik tombol
            button.click()
            
            print("Button diklik!")
            time.sleep(0.05)  # delay 5 detik tiap klik

        except Exception as e:
            # Jika terjadi error, abaikan dan lanjutkan
            print("⚠️ Tombol tidak ditemukan atau gagal diklik, lanjutkan loop...")

        # Tunggu 5 detik sebelum next click
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Auto-click dihentikan.")
finally:
    driver.quit()
