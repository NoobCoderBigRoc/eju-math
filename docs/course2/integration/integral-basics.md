---
title: 積分とその基本的な性質
---

# 積分とその基本的な性質

- $\int x^n dx = \dfrac{x^{n + 1}}{n + 1} + C$（$n \ne -1$）；$\int \dfrac{1}{x} dx = \log|x| + C$；$\int e^x dx = e^x + C$；$\int \sin x\, dx = -\cos x + C$；$\int \cos x\, dx = \sin x + C$
- 定积分与微积分基本定理：$\int_a^b f(x)\, dx = F(b) - F(a)$；交换限符号变，$\int_a^a = 0$。
- 偶函数/奇函数在对称区间：奇函数积分为 0，偶函数为一侧的 2 倍。

??? example "演習：定積分"
    **问题**

    $\displaystyle \int_0^1 (x^2 + 1)\, dx$ の値を求めよ。

    **答案**

    $\dfrac{4}{3}$

    **思路**

    找原函数后代上下限。

    **解答**

    $$\int_0^1 (x^2 + 1)\, dx = \left[\frac{x^3}{3} + x\right]_0^1 = \frac{1}{3} + 1 = \frac{4}{3}$$

## 易错点

- [ ] $\int \dfrac{1}{x} dx = \log|x| + C$ の絶対値（对数里的绝对值别丢）
