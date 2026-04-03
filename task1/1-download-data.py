import yfinance as yf

ticker = "IBM"

train_start = "2015-01-01"
train_end   = "2025-01-01"

test_start  = "2025-01-01"
test_end    = "2026-01-01"


train_data = yf.download(
    ticker,
    start=train_start,
    end=train_end,
    progress=False,
    auto_adjust=True
)


train_data.to_csv('ibm_train.csv', header=True)
print(f"✅ ibm_train.csv сохранён ({len(train_data)} дней)")


test_data = yf.download(
    ticker,
    start=test_start,
    end=test_end,
    progress=False,
    auto_adjust=True
)

test_data.to_csv('ibm_test.csv', header=True)
print(f"✅ ibm_test.csv сохранён ({len(test_data)} дней)")
