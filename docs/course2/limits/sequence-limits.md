---
title: 数列の極限
---

# 数列の極限

等比数列 $r^n$：$|r| < 1$ 时收敛于 0、$r = 1$ 时为 1、$r \le -1$ 或 $r > 1$ 时发散（$r = -1$ 是振動）。分数式数列的极限：分子分母同除以最高次项。有理化处理根号差：$\sqrt{n + 1} - \sqrt{n} = \dfrac{1}{\sqrt{n + 1} + \sqrt{n}} \to 0$。

**演習：数列の極限**

$\displaystyle \lim_{n \to \infty} (\sqrt{n + 1} - \sqrt{n})$ を求めよ。

??? example "思路・解答"
    **答案**

    $0$

    **思路**

    $\infty - \infty$ 型，先乘共轭有理化再估。

    **解答**

    $$\sqrt{n + 1} - \sqrt{n} = \frac{1}{\sqrt{n + 1} + \sqrt{n}} \to \frac{1}{\infty} = 0$$

## 易错点

- [ ] $(\sqrt{n + a} - \sqrt{n + b})$ は有理化してから（根号差的极限先有理化）
