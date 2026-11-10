---
title: 加法定理
---

# 加法定理

- $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$
- $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$（符号与左边相反）
- $\tan(\alpha \pm \beta) = \dfrac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$

## 加法定理の応用

- 2倍角：$\sin 2\alpha = 2\sin\alpha\cos\alpha$；$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha$
- 半角：$\sin^2\dfrac{\alpha}{2} = \dfrac{1 - \cos\alpha}{2}$、$\cos^2\dfrac{\alpha}{2} = \dfrac{1 + \cos\alpha}{2}$
- 积与和的互化（積和・和積の公式）は加法定理两边相加减即得，可现场推导。

## 三角関数の合成

$$a\sin\theta + b\cos\theta = \sqrt{a^2 + b^2}\sin(\theta + \varphi)$$

其中 $\cos\varphi = \dfrac{a}{\sqrt{a^2 + b^2}}$、$\sin\varphi = \dfrac{b}{\sqrt{a^2 + b^2}}$。合成后求最值、解方程/不等式都变简单。

??? example "演習：加法定理"
    **问题**

    $\sin 75^\circ$ の値を求めよ。

    **答案**

    $\dfrac{\sqrt{6} + \sqrt{2}}{4}$

    **思路**

    $75^\circ = 45^\circ + 30^\circ$，套加法定理。

    **解答**

    $$\sin 75^\circ = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6} + \sqrt{2}}{4}$$

??? example "演習：2倍角"
    **问题**

    $\sin\theta = \dfrac{1}{3}$（$\theta$ は鋭角）のとき、$\sin 2\theta$ の値を求めよ。

    **答案**

    $\dfrac{4\sqrt{2}}{9}$

    **思路**

    先由 $\cos\theta = \sqrt{1 - \sin^2\theta} = \dfrac{2\sqrt{2}}{3}$（锐角取正），再套 2 倍角公式。

    **解答**

    $$\sin 2\theta = 2 \cdot \frac{1}{3} \cdot \frac{2\sqrt{2}}{3} = \frac{4\sqrt{2}}{9}$$

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

- [ ] $\cos(\alpha + \beta)$ のマイナス符号（$\cos$ 加法定理的符号与左边相反）
- [ ] 合成の角度 $\varphi$ を $\sin$、$\cos$ 両方で確認しない（合成角要用 sin、cos 两式共同确定象限）
- [ ] 半角公式の符号は角の範囲で決める（半角的符号由角所在范围决定）
