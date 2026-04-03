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

def count_violations(close_test: np.ndarray, VaR: float) -> tuple:
    """Считает количество нарушений на тестовой выборке"""
    r5_test = np.log(close_test[4:] / close_test[:-4])
    
    violations = r5_test < -VaR
    
    N = int(np.sum(violations))
    T = len(violations)
    return N, T


def kupiec_pof_test(N: int, T: int, p: float = 0.05) -> tuple:
    """Тест Купиека (POF) — полностью на numpy, без scipy"""
    L_null = np.log((1 - p) ** (T - N)) + np.log(p ** N)
    
    pi = N / T
    L_obs = np.log((1 - pi) ** (T - N)) + np.log(pi ** N)
    
    LR = -2 * (L_null - L_obs)
    critical_value = 3.841459
    
    reject = LR > critical_value
    result = "Отвергаем H0 (VaR неадекватен)" if reject else "Не отвергаем H0 (VaR приемлем)"
    
    return LR, critical_value, result


if __name__ == "__main__":
    close_test = load_close_prices("data/ibm_test.csv")
    
    VaR1 = 0.047523
    VaR2 = 0.047326
    VaR3 = 0.053854
    
    for i, VaR in enumerate([VaR1, VaR2, VaR3], 1):
        N, T = count_violations(close_test, VaR)
        LR, crit, result = kupiec_pof_test(N, T)
        
        print(f"\nVaR №{i} = {VaR:.5f}")
        print(f"Нарушений: {N} из {T} периодов ({N/T*100:.2f}%)")
        print(f"Вывод: {result}")

"""
VaR №1 = 0.04752
Нарушений: 17 из 246 периодов (6.91%)
Вывод: Не отвергаем H0 (VaR приемлем)

VaR №2 = 0.04733
Нарушений: 17 из 246 периодов (6.91%)
Вывод: Не отвергаем H0 (VaR приемлем)

VaR №3 = 0.05385
Нарушений: 13 из 246 периодов (5.28%)
Вывод: Не отвергаем H0 (VaR приемлем)
"""