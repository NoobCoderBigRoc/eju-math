---
title: 三角関数とその基本的な性質
---

# 三角関数とその基本的な性質

## 1. 単位円による定義

座標平面で、原点 $O$ を中心とする半径 1 の円（単位円）を考え、角 $\theta$ の動径と円との交点を $P(x, y)$ とする。このとき

$$\sin\theta = y, \qquad \cos\theta = x, \qquad \tan\theta = \frac{y}{x} \quad (x \ne 0)$$

と定義する。この定義により、$\theta$ は鋭角に限らず、負の角や $2\pi$ を超える角にまで拡張される。$\tan\theta$ は動径の傾きそのものであり、$\theta = \dfrac{\pi}{2} + n\pi$（$n$ は整数）では定義されない。

## 2. 象限と符号

| 象限 | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
| --- | --- | --- | --- |
| 第1象限（$0 < \theta < \dfrac{\pi}{2}$） | + | + | + |
| 第2象限（$\dfrac{\pi}{2} < \theta < \pi$） | + | − | − |
| 第3象限（$\pi < \theta < \dfrac{3\pi}{2}$） | − | − | + |
| 第4象限（$\dfrac{3\pi}{2} < \theta < 2\pi$） | − | + | − |

符号は $P$ の座標 $(x, y)$ の符号そのものである。方程式を解いて角を求めるときは、この表で候補の象限を絞る。

## 3. 周期性と奇偶性

- 周期性：$\sin(\theta + 2\pi) = \sin\theta$、$\cos(\theta + 2\pi) = \cos\theta$（周期 $2\pi$）；$\tan(\theta + \pi) = \tan\theta$（周期 $\pi$）
- 奇偶性：$\sin(-\theta) = -\sin\theta$（奇関数）、$\cos(-\theta) = \cos\theta$（偶関数）、$\tan(-\theta) = -\tan\theta$（奇関数）

## 4. 誘導公式（代表角への帰着）

どの公式も単位円の対称性から導かれる。暗記よりも「$P$ がどの点へ移るか」で確認するのが確実である。

| 変換 | $\sin$ | $\cos$ | $\tan$ |
| --- | --- | --- | --- |
| $-\theta$ | $-\sin\theta$ | $\cos\theta$ | $-\tan\theta$ |
| $\pi - \theta$ | $\sin\theta$ | $-\cos\theta$ | $-\tan\theta$ |
| $\pi + \theta$ | $-\sin\theta$ | $-\cos\theta$ | $\tan\theta$ |
| $\dfrac{\pi}{2} - \theta$ | $\cos\theta$ | $\sin\theta$ | $\dfrac{1}{\tan\theta}$ |
| $\dfrac{\pi}{2} + \theta$ | $\cos\theta$ | $-\sin\theta$ | $-\dfrac{1}{\tan\theta}$ |

$\dfrac{\pi}{2}$ を含む変換では $\sin$ と $\cos$ が入れ替わり、$\pi$ を含む変換では入れ替わらない、という規則で整理できる。

## 5. 相互関係

- $\sin^2\theta + \cos^2\theta = 1$
- $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$
- $1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$

## 易错点

- [ ] $\tan\theta$ の定義されない角（$\theta = \dfrac{\pi}{2} + n\pi$）を見落とす
- [ ] 象限による符号の判定ミス（$\sin$ の値から $\cos$ を求めるとき $\pm$ の両方を検討する）
- [ ] $\tan$ の周期を $2\pi$ と思い込む（$\tan$ は $\pi$）
