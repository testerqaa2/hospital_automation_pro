from playwright.sync_api import sync_playwright

def search_active_visits():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)  # slow_mo untuk simulasi 
        page = browser.new_page()
        
        try:
            # Navigasi ke halaman login
            print("1. Membuka halaman login OpenMRS")
            page.goto("https://o2.openmrs.org/openmrs/login.htm")

            # Isi username dan password
            print("2. Mengisi username dan password")
            page.fill("#username", "admin")
            page.fill("#password", "Admin123")
            page.click("#togglePassword")

            # Pilih Location: Registration Desk
            print("3. Memilih 'Registration Desk'")
            page.locator("#sessionLocation li#Registration\\ Desk").click()

            # Klik tombol login
            print("4. Mengklik tombol login")
            page.click("#loginButton")
            page.wait_for_timeout(2000)
            print("✅ Login berhasil dengan valid Username & Password")

            # Pilih Menu Active Visits
            print("5. Memilih Menu Active Visits")
            page.click("text='Active Visits'")
            page.wait_for_selector("#active-visits", state="visible")

            search_box = page.locator("input[type='search']")
            search_box.fill("Jack John")
            search_box.press("Enter")
            page.wait_for_selector("table tbody tr", state="visible")

            target_row = page.locator("tr.odd:has-text('Jack John')")
            assert "Jack John" in target_row.inner_text(), "Nama Pasien Tidak ditemukan"
            print("✅ Data Pasien ditemukan dan sesuai")
           
        finally:
            # Tutup browser
            browser.close()
            print("7. Browser ditutup")

if __name__ == "__main__":
    search_active_visits()