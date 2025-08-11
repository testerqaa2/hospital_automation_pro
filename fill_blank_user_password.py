from playwright.sync_api import sync_playwright

def fill_blank_user_password():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)  # slow_mo untuk simulasi 
        page = browser.new_page()

        try:
            # Navigasi ke halaman login
            print("1. Membuka halaman login OpenMRS")
            page.goto("https://o2.openmrs.org/openmrs/login.htm")

            # Kosongkan username dan password
            print("2. Kosongkan username dan password")
            page.fill("#username", "")
            page.fill("#password", "")
            page.click("#togglePassword")

            # Pilih Location: Registration Desk
            print("3. Memilih 'Registration Desk'")
            page.locator("#sessionLocation li#Registration\\ Desk").click()

            # Klik tombol login
            print("4. Mengklik tombol login")
            page.click("#loginButton")

            # Verifikasi login (data kosong)
            print("5. Login Gagal!! Data Input Kosong")
            actual_error = page.locator("div.alert-danger")

            actual_error.wait_for(state="visible", timeout=2000)
            assert actual_error.is_visible(), "Pesan error tidak tampil"
            print("✅ Pesan kesalahan berhasil ditampilkan")
            
            # Verifikasi text yang tampil
            expected_text = "Invalid username/password. Please try again."
            assert actual_error.inner_text().strip() == expected_text, \
                f"Teks error tidak sesuai. Dapat: '{actual_error.inner_text()}', Expectednya: '{expected_text}'"
            print("✅ Text Pesan kesalahan sudah sesuai")
            
            error_icon = page.locator("i.icon-exclamation-sign")
            assert error_icon.is_visible(), "Icon error tidak tampil"
            print("✅ Icon error berhasil ditampilkan")
            
        finally:
            # Tutup browser
            browser.close()
            print("6. Browser ditutup")

if __name__ == "__main__":
    fill_blank_user_password()