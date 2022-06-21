import sentry_sdk
sentry_sdk.init(
    dsn="https://45f39db1385648c49f05b49ea04b3df0@o1289354.ingest.sentry.io/6507728",
    traces_sample_rate=1.0
)


if __name__ == '__main__':
    print(5 / 0)
