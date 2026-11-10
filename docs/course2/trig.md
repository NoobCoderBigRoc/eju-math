---
title: 三角関数
---

# 11. 三角関数

## シラバスとの対応

| 項目 | 内容 |
| --- | --- |
| 出題項目 | 11. 三角関数（数学II） |
| 細目 | (1) 三角関数：①一般角と弧度法 ②三角関数とその基本的な性質 ③三角関数とそのグラフ　(2) 加法定理：①三角関数の加法定理 ②加法定理の応用 ③三角関数の合成 |
| コース | コース2 のみ。[図形と計量](../course1/measure.md) の拡張 |

## 1. 一般角と弧度法

弧度法では $\theta\ [\mathrm{rad}]$、$180^\circ = \pi$。半径 $r$、中心角 $\theta$ の扇形について、弧の長さ $l = r\theta$、面積 $S = \dfrac{1}{2}r^2\theta$。

$y = \sin x$ の周期は $2\pi$、$y = \tan x$ の周期は $\pi$。$y = a \sin(bx + c) + d$ の振幅は $|a|$、周期は $\dfrac{2\pi}{|b|}$。

![三角関数のグラフ](../images/trig-graphs.svg)

図：$y = \sin x$、$y = \cos x$、$y = \tan x$ のグラフ。$\tan x$ は $x = \dfrac{\pi}{2} + n\pi$ に漸近線をもつ。

## 2. 加法定理とその応用

$$
\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta, \qquad \cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta
$$

$$
\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}
$$

**2倍角**：$\sin 2\alpha = 2\sin\alpha\cos\alpha$、$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1$。

**半角**：$\sin^2 \dfrac{\alpha}{2} = \dfrac{1 - \cos\alpha}{2}$、$\cos^2 \dfrac{\alpha}{2} = \dfrac{1 + \cos\alpha}{2}$。

**積和・和積**（要点のみ）：$\sin\alpha\cos\beta = \dfrac{1}{2}\{\sin(\alpha + \beta) + \sin(\alpha - \beta)\}$、$\sin\alpha + \sin\beta = 2\sin\dfrac{\alpha + \beta}{2}\cos\dfrac{\alpha - \beta}{2}$。

## 3. 三角関数の合成

$$
a\sin\theta + b\cos\theta = \sqrt{a^2 + b^2}\, \sin(\theta + \varphi), \qquad \cos\varphi = \frac{a}{\sqrt{a^2 + b^2}},\ \sin\varphi = \frac{b}{\sqrt{a^2 + b^2}}
$$

最大値・最小値を求める問題は合成して 1 つの $\sin$ にまとめるのが原則。

## 例題（演習）

??? example "例題 1：加法定理で値を求める"
    $\sin 75^\circ$ の値を求めよ。

    **考え方**：$75^\circ = 45^\circ + 30^\circ$ として加法定理を使う。

    **解答**：$\sin 75^\circ = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ = \dfrac{\sqrt{2}}{2} \cdot \dfrac{\sqrt{3}}{2} + \dfrac{\sqrt{2}}{2} \cdot \dfrac{1}{2} = \dfrac{\sqrt{6} + \sqrt{2}}{4}$。

    **答え**：$\dfrac{\sqrt{6} + \sqrt{2}}{4}$

??? example "例題 2：合成と最大値"
    $f(\theta) = \sin\theta + \sqrt{3}\cos\theta$ の最大値と、そのときの $\theta$（$0 \leqq \theta < 2\pi$）を求めよ。

    **考え方**：合成すると $f(\theta) = 2\sin\left(\theta + \dfrac{\pi}{3}\right)$。

    **解答**：最大値は $2$。$\theta + \dfrac{\pi}{3} = \dfrac{\pi}{2}$ のとき、すなわち $\theta = \dfrac{\pi}{6}$。

    **答え**：最大値 $2$（$\theta = \dfrac{\pi}{6}$）

??? example "例題 3：三角方程式"
    $0 \leqq x < 2\pi$ の範囲で $\sin 2x = \sin x$ を解け。

    **考え方**：2 倍角の公式で左辺を変形し、共通因数でくくる。

    **解答**：$2\sin x \cos x - \sin x = \sin x (2\cos x - 1) = 0$。$\sin x = 0$ より $x = 0, \pi$。$\cos x = \dfrac{1}{2}$ より $x = \dfrac{\pi}{3}, \dfrac{5\pi}{3}$。

    **答え**：$x = 0, \dfrac{\pi}{3}, \pi, \dfrac{5\pi}{3}$

## よくあるミス

- [ ] 加法定理の符号（$\sin$ は同符号、$\cos$ は逆符号）を取り違える
- [ ] 方程式の解を範囲内で列挙し忘れる（周期性のため範囲外・範囲内の判定が必須）
- [ ] 合成の角度 $\varphi$ を当てずっぽうに決める（$\cos\varphi$、$\sin\varphi$ の両方から決める）
- [ ] 弧度法と度数法を混在させる

## 関連項目

- 基礎：[図形と計量](../course1/measure.md)
- 微分での姿は [微分法](differentiation.md)
