from uzhealth_app import UzHealthApp

def main():
    return UzHealthApp("UzHealth AI", "org.beeware.uzhealthai")

if __name__ == "__main__":
    app = main()
    app.main_loop()