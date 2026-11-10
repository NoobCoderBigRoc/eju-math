---
title: 微分係数と導関数
---

# 微分係数と導関数

微分係数 $f'(a) = \lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h}$；导関数 $f'(x) = \lim_{h \to 0} \dfrac{f(x + h) - f(x)}{h}$。

基本公式：

- $(x^n)' = n x^{n-1}$

??? example "演習：微分係数の定義"
    **问题**

    定義に従って、$f(x) = x^2$ の $x = 1$ における微分係数を求めよ。

    **答案**

    $2$

    **思路**

    直接用差商定义求极限（不要用公式，要按定义的步骤写）。

    **解答**

    $$f'(1) = \lim_{h \to 0} \frac{(1 + h)^2 - 1}{h} = \lim_{h \to 0} \frac{2h + h^2}{h} = \lim_{h \to 0} (2 + h) = 2$$

## 関連項目

- 前置：[極限](../limits/sequence-limits.md)（导数即极限）
- 并行：[積分法](../integration/integral-basics.md)（微积分基本定理连接两者）
