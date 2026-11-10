---
title: 曲線の長さ
---

# 曲線の長さ

## 1. 公式の考え方

曲線を細かく区切ると、各小区間の弧は直線（弦）で近似できる。$x$ が $\Delta x$ 増えるときの弦の長さは三平方の定理から $\sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{1 + \left(\dfrac{\Delta y}{\Delta x}\right)^2}\, \Delta x$。区間を限りなく細かくして $\dfrac{\Delta y}{\Delta x} \to f'(x)$ とすると、弧長の微小量 $ds = \sqrt{1 + \{f'(x)\}^2}\, dx$ を得て、それを足し上げたものが積分になる。

## 2. 3つの表示と公式

| 曲線の表示 | 曲線の長さ |
| --- | --- |
| $y = f(x)$（$a \le x \le b$） | $\displaystyle L = \int_a^b \sqrt{1 + \{f'(x)\}^2}\, dx$ |
| 媒介変数表示 $x = x(t)$、$y = y(t)$（$\alpha \le t \le \beta$） | $\displaystyle L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt$ |
| 極座標 $r = r(\theta)$（$\alpha \le \theta \le \beta$） | $\displaystyle L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\, d\theta$ |

$x = g(y)$ の形で与えられた曲線は、$x$ と $y$ の役割を入れ替えて $L = \int_c^d \sqrt{1 + \{g'(y)\}^2}\, dy$ とする。

## 3. 計算のコツ

被積分関数に根号があるため、そのままでは積分できない形が多い。出題される曲線はたいてい **$1 + \{f'(x)\}^2$ が完全平方式になる**よう設計されている（例：$f'(x)$ に $x - \dfrac{1}{4x}$ のような形が入ると $1 + \{f'(x)\}^2 = \left(x + \dfrac{1}{4x}\right)^2$ になる）。まず根号の中を整理し、平方の形にできないかを確認してから積分に入る。媒介変数表示でも同様に、$\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2$ が平方になることが多い。

## 易错点

- [ ] 曲線の長さの被積分関数の形（$\sqrt{1 + (f')^2}$ の形を正確に）
- [ ] 媒介変数・極座標で積分区間を $x$ の範囲のままにする（パラメータの範囲 $\alpha \le t \le \beta$ に直す）
- [ ] 根号を外すときの絶対値（$\sqrt{A^2} = |A|$；区間内での $A$ の符号を確認する）
- [ ] 極座標の公式で $r^2 + (r')^2$ の $r'$ 側を $r$ と書き違える
