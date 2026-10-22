---
title: 指数函数·对数函数
---

# 指数函数·对数函数

## 考纲要求

指数法则、指数函数图像、对数定义与运算法则、换底公式、指数对数方程与不等式。

## 指数法则

$$
a^m \cdot a^n = a^{m+n}, \quad (a^m)^n = a^{mn}, \quad (ab)^n = a^n b^n, \quad a^0 = 1\ (a \ne 0)
$$

分数指数：$a^{\frac{m}{n}} = \sqrt[n]{a^m}$；负指数：$a^{-n} = \dfrac{1}{a^n}$。

## 对数定义与法则

$$
a^x = b \iff x = \log_a b \quad (a > 0, a \ne 1, b > 0)
$$

$$
\log_a xy = \log_a x + \log_a y, \qquad \log_a \frac{x}{y} = \log_a x - \log_a y
$$

$$
\log_a x^n = n \log_a x, \qquad \log_a b = \frac{\log_c b}{\log_c a}\ \text{(换底)}
$$

## 图像

- $y = a^x$：恒过 $(0, 1)$，$a > 1$ 单调递增，$0 < a < 1$ 递减；
- $y = \log_a x$：恒过 $(1, 0)$，与 $y = a^x$ 关于 $y = x$ 对称。

## 典型例题

??? example "例题：对数方程"
    解 $\log_2(x-1) + \log_2(x+1) = 3$。

    **解答**：真数条件 $x > 1$。合并：

    $$
    \log_2(x^2 - 1) = 3 \implies x^2 - 1 = 8 \implies x = \pm 3
    $$

    验证真数条件后**只保留 $x = 3$**。

!!! warning "真数条件"
    对数方程/不等式**最后必须验根**——EJU 选项里常放一个不满足真数条件的"陷阱值"。

## 易错点

- [x] $(\log_a x)^2 \ne \log_a x^2$（前者是 $2\log_a|x|$ 相关的错误记法）；
- [x] 底数 $0 < a < 1$ 时对数不等式**不等号方向反转**；
- [x] 忘记真数 $> 0$ 的定义域限制。
