from playwright.sync_api import sync_playwright

def search_patient():
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

            # Pilih Menu Find Patient Record
            print("5. Memilih Menu Find Patient Record")
            page.click("text='Find Patient Record'")
            page.wait_for_selector("#patient-search", state="visible")
            
            # Input Nama Pasien
            print("6. Input Data Pasien Terdaftar")
            search_field = page.locator("#patient-search")
            search_field.fill("Harry Potter")
            search_field.press("Enter")
            page.wait_for_selector("#patient-search-results-table", state="visible", timeout=5000)

            patient_row = page.locator("tr.odd:has-text('Harry Potter')")
            assert patient_row.is_visible(), "Pasien Harry Potter tidak ditemukan"
            assert "M" in patient_row.inner_text(), "Gender tidak sesuai"
            assert "75" in patient_row.inner_text(), "Usia tidak sesuai"
            assert "31 Jan 1950" in patient_row.inner_text(), "Tanggal lahir tidak sesuai"
            print("✅ Data Pasien ditemukan dan sesuai")
           
        finally:
            # Tutup browser
            browser.close()
            print("7. Browser ditutup")

if __name__ == "__main__":
    search_patient()