---
title: ド・モアブルの定理
---

# ド・モアブルの定理

$$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$$

推论：$n$ 次方根有恰好 $n$ 个，均匀分布在圆周上：指数方程 $z^n = w$ 的解是把 $\arg w$ 做 $n$ 等分再加 $\dfrac{2\pi}{n}$ 的周期偏移。

??? example "演習：ド・モアブルの定理"
    **问题**

    $(1 + i)^8$ の値を求めよ。

    **答案**

    $16$

    **思路**

    $1 + i = \sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$，8 次幂：模 $(\sqrt{2})^8 = 16$、角 $8 \times \dfrac{\pi}{4} = 2\pi$，回到正实轴。

    **解答**

    $$(1 + i)^8 = 16\left(\cos 2\pi + i\sin 2\pi\right) = 16$$

## 易错点

- [ ] 方根の個数（$n$ 個）を数え落とす（$n$ 次方根恰有 $n$ 个，别漏）
