---
title: 微分与积分
---

# 微分与积分

## 考纲要求

平均变化率与导数、导函数与切线、和差积商的微分、不定积分与定积分、面积与体积应用。Course 2 **分值最高**的单元（约 30%）。

## 导数定义

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

## 常用导数公式

$$
(x^n)' = n x^{n-1}, \qquad (\sin x)' = \cos x, \qquad (\cos x)' = -\sin x, \qquad (e^x)' = e^x
$$

$$
(\log_a x)' = \frac{1}{x \ln a}, \qquad \{(f(x) + g(x))\}' = f'(x) + g'(x)
$$

$$
\{f(x)g(x)\}' = f'(x)g(x) + f(x)g'(x)
$$

## 切线

曲线 $y = f(x)$ 上点 $(a, f(a))$ 处的切线：

$$
y - f(a) = f'(a)(x - a)
$$

**单调性与极值**：$f'(x) > 0$ 递增，$< 0$ 递减；$f'(x) = 0$ 且导数**变号**处取极值。

## 积分

**不定积分**（$F'(x) = f(x)$）：

$$
\int f(x)\, dx = F(x) + C
$$

**定积分**：

$$
\int_a^b f(x)\, dx = F(b) - F(a)
$$

常用积分公式：

$$
\int x^n\, dx = \frac{x^{n+1}}{n+1} + C \ (n \ne -1), \qquad \int e^x dx = e^x + C, \qquad \int \cos x\, dx = \sin x + C
$$

## 面积与体积

- 两曲线间面积：$S = \displaystyle\int_a^b |f(x) - g(x)|\, dx$；
- 绕 $x$ 轴旋转体体积：$V = \pi \displaystyle\int_a^b \{f(x)\}^2\, dx$。

## 典型例题

??? example "例题 1：切线方程"
    求 $y = x^3 - 3x$ 在 $x = 2$ 处的切线。

    **解答**：$y' = 3x^2 - 3$，$y'(2) = 9$；$f(2) = 2$。

    $$
    y - 2 = 9(x - 2) \implies y = 9x - 16
    $$

??? example "例题 2：面积"
    求抛物线 $y = x^2$ 与直线 $y = x + 2$ 围成的面积。

    **解答**：交点 $x^2 = x + 2 \Rightarrow x = -1, 2$。直线在上方：

    $$
    S = \int_{-1}^{2} (x + 2 - x^2)\, dx = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2} = \frac{9}{2}
    $$

## 易错点

- [x] 极值点要求**导数两侧变号**（$f'(x)=0$ 不一定是极值，如 $y = x^3$ 在 0 处）；
- [x] 定积分结果可能为负，"面积"要取绝对值或分段处理；
- [x] 旋转体体积公式别丢 $\pi$。
