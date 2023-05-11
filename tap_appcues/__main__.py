from tap_appcues.tap import TapAppcues

def main():
    tap = TapAppcues("ACCOUNT_ID", "ACCESS_TOKEN")
    tap.sync()

if __name__ == '__main__':
    main()
