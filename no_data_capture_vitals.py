from playwright.sync_api import sync_playwright

def no_data_capture_vitals():
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

            # Pilih Menu Capture Vitals
            print("5. Memilih Menu Capture Vitals")
            page.click("text='Capture Vitals'")
            page.wait_for_selector("#patient-search", state="visible")
            
            # Input Nama Pasien
            print("6. Input Data Pasien Yang Tidak Terdaftar")
            search_field = page.locator("#patient-search")
            search_field.fill("Frisca Ajalah")
            search_field.press("Enter")
            page.wait_for_selector("#patient-search-results-table", state="visible", timeout=5000)

            message_locator = page.locator(".dataTables_empty")
            expected_text = "No matching records found"
            actual_text = message_locator.inner_text().strip()
            assert actual_text == expected_text, \
                f"Teks tidak sesuai. Dapat: '{actual_text}', Expectednya: '{expected_text}'"
            print ("✅ Text Pesan kesalahan sudah sesuai, yaitu", actual_text)
           
        finally:
            # Tutup browser
            browser.close()
            print("7. Browser ditutup")

if __name__ == "__main__":
    no_data_capture_vitals()