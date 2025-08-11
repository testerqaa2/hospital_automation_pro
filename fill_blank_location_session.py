from playwright.sync_api import sync_playwright

def fill_blank_location_session():
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

            # Kosongkan Location Session
            print("3. Tidak Memilih Location Session")

            # Klik tombol login
            print("4. Mengklik tombol login")
            page.click("#loginButton")

            # Verifikasi Error Message Location Session Kosong
            print("5. Location Session Tidak Dipilih")
            actual_text = page.locator("#sessionLocationError").inner_text().strip()
            expected_text = "You must choose a location!"
            assert actual_text == expected_text, \
                f"Teks tidak sesuai. Dapat: '{actual_text}', Expectednya: '{expected_text}'"
            print ("✅ Text Pesan kesalahan sudah sesuai") 

        finally:
            # Tutup browser
            browser.close()
            print("6. Browser ditutup")

if __name__ == "__main__":
    fill_blank_location_session()