---
title: 導関数
---

# 導関数

## 1. 微分係数と導関数

微分係数 $f'(a) = \lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h}$；导関数 $f'(x) = \lim_{h \to 0} \dfrac{f(x + h) - f(x)}{h}$。

基本公式：

- $(x^n)' = n x^{n-1}$；$(\sin x)' = \cos x$；$(\cos x)' = -\sin x$；$(\tan x)' = \dfrac{1}{\cos^2 x}$
- $(e^x)' = e^x$；$(a^x)' = a^x \log a$；$(\log x)' = \dfrac{1}{x}$；$(\log_a x)' = \dfrac{1}{x \log a}$

## 2. 演算の公式

- 積の微分：$(fg)' = f'g + fg'$
- 商の微分：$\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$
- 合成関数：$\{f(g(x))\}' = f'(g(x))\, g'(x)$（外微分 × 内微分）；逆関数の微分：$\dfrac{dy}{dx} = \dfrac{1}{dx/dy}$

## 3. 第 $n$ 次導関数

反复求导找规律：$(e^x)^{(n)} = e^x$；$(\sin x)^{(n)} = \sin\left(x + \dfrac{n\pi}{2}\right)$；$\left(\dfrac{1}{x}\right)^{(n)} = \dfrac{(-1)^n n!}{x^{n + 1}}$。

??? example "演習：積の微分"
    **问题**

    $y = x e^x$ を微分せよ。

    **答案**

    $y' = (x + 1)e^x$

    **思路**

    乘积法则：(前导×后) + (前×后导)。

    **解答**

    $$y' = 1 \cdot e^x + x \cdot e^x = (x + 1)e^x$$

## 易错点

- [ ] 合成関数の内側の微分（$g'(x)$）を掛け忘れる（链式法则漏乘内层导数）
- [ ] $\log|x|$ の微分の絶対値、$(a^x)'$ の $\log a$（$|\cdot|$ 与 $\log a$ 因子的处理）
- [ ] 商の微分の分子の順序（$f'g - fg'$ の順序，商法则分子的顺序）
