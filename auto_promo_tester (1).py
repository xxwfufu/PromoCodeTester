import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# === CONFIGURATION ===
NUM_CODES = 100000
WAIT_AFTER_APPLY = 2
EXPORT_FILE = "valid_codes.txt"
ALL_CODES_LOG = "all_codes.txt"

# === GÉNÉRATION DE CODES PROMO ===
def generate_code():
    def block():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{block()}-{block()}-{block()}-{block()}"

# === SE CONNECTER À TON CHROME DÉJÀ OUVERT ===
def setup_existing_browser():
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver

# === TEST DU CODE ===
def test_code(driver, code):
    try:
        input_field = driver.find_element(By.ID, "code-input")
        input_field.click()
        input_field.clear()

        for char in code:
            input_field.send_keys(char)
            time.sleep(0.1)

        input_field.send_keys(Keys.ENTER)
        time.sleep(WAIT_AFTER_APPLY)

        page_content = driver.page_source.lower()
        if "réduction" in page_content or code.lower() in page_content:
            return True

    except Exception as e:
        print(f"⚠️ Erreur avec le code {code} : {type(e).__name__} - {e}")
    return False

# === MAIN ===
def main():
    print(f"🧩 Connexion au navigateur existant...")
    driver = setup_existing_browser()
    valid_codes = []

    for i in range(NUM_CODES):
        code = generate_code()
        print(f"[{i+1}/{NUM_CODES}] Test : {code}")

        with open(ALL_CODES_LOG, "a") as log:
            log.write(code + "\n")

        if test_code(driver, code):
            print(f"✅ VALIDE : {code}")
            valid_codes.append(code)
        else:
            print("❌ Invalide")

    if valid_codes:
        with open(EXPORT_FILE, "w") as f:
            for code in valid_codes:
                f.write(code + "\n")
        print(f"\n✅ Enregistrés dans : {EXPORT_FILE}")
    else:
        print("❌ Aucun code valide")

if __name__ == "__main__":
    main()
