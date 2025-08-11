from playwright.sync_api import sync_playwright

def success_login():
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

            # Verifikasi login berhasil & selected Location
            print("5. Redirect ke dashboard")
            actual_text = page.locator("#selected-location").inner_text().strip()
            expected_text = "Registration Desk"
            assert actual_text == expected_text, \
                f"Teks tidak sesuai. Dapat: '{actual_text}', Expectednya: '{expected_text}'"
            print ("✅ Anda memilih location = ", actual_text) 

        finally:
            # Tutup browser
            browser.close()
            print("6. Browser ditutup")

if __name__ == "__main__":
    success_login()