import numpy as np

def load_close_prices(file_path: str) -> np.ndarray:
    close = np.loadtxt(
        file_path,
        delimiter=',',
        skiprows=3,
        usecols=1,
        dtype=float
    )
    return close


def var_by_sample(close_train: np.ndarray, alpha: float = 0.05) -> float:
    """
    1. По выборке (эмпирический)
    """
    r5 = np.log(close_train[4:] / close_train[:-4])
    VaR = -np.percentile(r5, alpha * 100)
    return VaR


def var_gauss_5day(close_train: np.ndarray, alpha: float = 0.05) -> float:
    """
    2. Гауссовость 5-дневных приростов
    """
    r5 = np.log(close_train[4:] / close_train[:-4])
    
    mu5 = np.mean(r5)
    sigma5 = np.std(r5, ddof=1)
    
    z_alpha = -1.64485
    
    VaR = -(mu5 + z_alpha * sigma5)
    return VaR


def var_gauss_daily_scaled(close_train: np.ndarray, alpha: float = 0.05) -> float:
    """
    3. Гауссовость дневных + √5
    """
    r1 = np.log(close_train[1:] / close_train[:-1])
    
    mu_d = np.mean(r1)
    sigma_d = np.std(r1, ddof=1)
    
    # Масштабируем на 5 дней
    mu5 = 5 * mu_d
    sigma5 = sigma_d * np.sqrt(5)
    
    z_alpha = -1.64485
    
    VaR = -(mu5 + z_alpha * sigma5)
    return VaR


if __name__ == "__main__":
    close_train = load_close_prices("data/ibm_train.csv")
    
    VaR1 = var_by_sample(close_train)
    VaR2 = var_gauss_5day(close_train)
    VaR3 = var_gauss_daily_scaled(close_train)
    
    print("5-дневный 5%-VaR логарифмической доходности (IBM):")
    print(f"1. По выборке (эмпирический)          : {VaR1:.6f}")
    print(f"2. Гауссовость 5-дневных приростов    : {VaR2:.6f}")
    print(f"3. Гауссовость дневных + √5           : {VaR3:.6f}")

"""
5-дневный 5%-VaR логарифмической доходности (IBM):
1. По выборке (эмпирический)          : 0.047523
2. Гауссовость 5-дневных приростов    : 0.047326
3. Гауссовость дневных + √5           : 0.053854
"""