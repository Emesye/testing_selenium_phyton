from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi driver Edge
driver = webdriver.Edge(executable_path=r'C:\edgedriver\edgedriver.exe')

# Catat waktu mulai
start_time = time.time()

# Buka halaman web dan lakukan tindakan
driver.get('http://127.0.0.1:8000/')
driver.fullscreen_window()
username = driver.find_element(By.XPATH, '//*[@id="email"]')
username.send_keys('admin@gmail.com')

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('admin123')

form = driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div/div[2]/form/center/button')
form.click()
driver.fullscreen_window()

# Tunggu beberapa saat agar halaman selesai dimuat
time.sleep(3)

# Cek apakah login gagal dengan mencari teks "login failed"
login_failed = False
try:
    # Ganti '//*[contains(text(), "login failed")]' dengan XPath atau CSS Selector yang sesuai
    error_message = driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div/div[2]/div')
    login_failed = True
except:
    login_failed = False

# Kondisi if untuk menampilkan hasil login
if login_failed:
    print("Gagal Login")
else:
    print("Berhasil Login")

    # Tindakan setelah login berhasil
    try:
        # Menunggu elemen halaman berikutnya muncul (misalnya, tautan atau tombol untuk melanjutkan)
        next_page_element = driver.find_element(By.XPATH, '//*[@id="accordionSidenav"]/a[16]')
        next_page_element.click()
        
        # Tunggu beberapa saat agar halaman selesai dimuat
        time.sleep(3)
        
        # Verifikasi bahwa kita telah berada di halaman berikutnya
        page_title = driver.title
        print(f"Berhasil masuk ke halaman Data Pengguna: {page_title}")
        
    except Exception as e:
        print(f"Gagal masuk ke halaman berikutnya: {e}")

# Catat waktu selesai
end_time = time.time()

# Hitung durasi eksekusi
duration = end_time - start_time

# Tampilkan durasi eksekusi
print(f"Durasi eksekusi test case: {duration:.2f} detik")

# Tutup driver
#driver.quit()
