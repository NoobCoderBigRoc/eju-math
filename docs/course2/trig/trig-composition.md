---
title: 三角関数の合成
---

# 三角関数の合成

$$a\sin\theta + b\cos\theta = \sqrt{a^2 + b^2}\sin(\theta + \varphi)$$

其中 $\cos\varphi = \dfrac{a}{\sqrt{a^2 + b^2}}$、$\sin\varphi = \dfrac{b}{\sqrt{a^2 + b^2}}$。合成后求最值、解方程/不等式都变简单。

??? example "演習：合成と最大値"
    **问题**

    $\sin\theta + \sqrt{3}\cos\theta$ の最大値を求めよ。

    **答案**

    $2$

    **思路**

    合成：振幅 $\sqrt{1 + 3} = 2$，即 $2\sin\left(\theta + \dfrac{\pi}{3}\right)$，最大值就是振幅。

    **解答**

    $$\sin\theta + \sqrt{3}\cos\theta = 2\sin\left(\theta + \frac{\pi}{3}\right) \le 2$$

## 易错点

- [ ] 合成の角度 $\varphi$ を $\sin$、$\cos$ 両方で確認しない（合成角要用 sin、cos 两式共同确定象限）
