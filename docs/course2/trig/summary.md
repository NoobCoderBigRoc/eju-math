---
title: 三角関数要点总结
---

# 三角関数要点总结

考前确认本页：弧度法と単位円の定義、加法定理を起点とする公式の派生関係（2倍角・半角・合成）。

## 公式・定理清单

### 三角関数

- 単位円による定義：動径と単位円の交点 $P(x, y)$ に対して $\sin\theta = y$、$\cos\theta = x$、$\tan\theta = \dfrac{y}{x}$（$x \ne 0$）—— $\tan\theta$ が定義されないのは $\theta = \dfrac{\pi}{2} + n\pi$
- 弧度法：$\pi\ \mathrm{rad} = 180^\circ$、$\theta = \dfrac{\text{弧の長さ}}{\text{半径}}$ —— 度から弧度へは $\dfrac{\pi}{180}$ を掛ける
- 扇形：弧長 $l = r\theta$、面積 $S = \dfrac{1}{2}r^2\theta = \dfrac{1}{2}lr$ —— $\theta$ が弧度法のときにだけ使える
- 相互関係：$\sin^2\theta + \cos^2\theta = 1$、$\tan\theta = \dfrac{\sin\theta}{\cos\theta}$、$1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$
- 周期と奇偶性：$\sin$、$\cos$ の周期は $2\pi$、$\tan$ の周期は $\pi$；$\sin$、$\tan$ は奇関数、$\cos$ は偶関数
- 誘導公式の整理：$\pi$ を含む変換では $\sin$ と $\cos$ は入れ替わらず、$\dfrac{\pi}{2}$ を含む変換では入れ替わる
- グラフ $y = a\sin(bx + c) + d$：振幅 $|a|$、周期 $\dfrac{2\pi}{b}$、平行移動は $-\dfrac{c}{b}$ —— $y = \tan x$ の漸近線は $x = \dfrac{\pi}{2} + n\pi$

### 加法定理

- $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$ —— 符号は左辺と同方向
- $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$ —— 符号は左辺と逆になる
- $\tan(\alpha \pm \beta) = \dfrac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$
- 2 倍角：$\sin 2\alpha = 2\sin\alpha\cos\alpha$、$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha$ —— $\cos 2\alpha$ は問題に合わせて 3 形から選ぶ
- 半角：$\sin^2\dfrac{\alpha}{2} = \dfrac{1 - \cos\alpha}{2}$、$\cos^2\dfrac{\alpha}{2} = \dfrac{1 + \cos\alpha}{2}$ —— 値の符号は角の範囲で決める
- 積和・和積の公式：加法定理の両辺を加減すれば得られる —— 現場で導出できる
- 合成：$a\sin\theta + b\cos\theta = \sqrt{a^2 + b^2}\sin(\theta + \varphi)$（$\cos\varphi = \dfrac{a}{\sqrt{a^2 + b^2}}$、$\sin\varphi = \dfrac{b}{\sqrt{a^2 + b^2}}$）—— 振幅がそのまま最大値になる

## 解法パターン

- **有名でない角の値**：$75^\circ$ のような角は → $45^\circ + 30^\circ$ のように有名角の和・差に分解して加法定理を使う
- **1 つの値から他を求める**：$\sin\theta$ の値だけ与えられたら → 相互関係で絶対値を出し、象限で符号を決める
- **最大・最小**：$a\sin\theta + b\cos\theta$ の形は → 合成して 1 つの $\sin$ にまとめ、振幅と位相を読む
- **方程式・不等式**：種類や次数が混ざっていたら → 2 倍角や合成で $\sin$ か $\cos$ の 1 種類に統一してから解き、範囲内の解を取りこぼさない
- **グラフの読み取り**：$y = a\sin(bx + c) + d$ は → $bx + c = b\left(x + \dfrac{c}{b}\right)$ と変形し、周期 $\dfrac{2\pi}{b}$ と平行移動 $-\dfrac{c}{b}$ を読む

## 考前注意

- [ ] $\tan$ の周期は $2\pi$ ではなく $\pi$、定義されない角 $\theta = \dfrac{\pi}{2} + n\pi$ も見落とさない
- [ ] $\cos(\alpha + \beta)$ の加法定理は符号が左辺と逆になる
- [ ] 合成の角 $\varphi$ は $\sin\varphi$、$\cos\varphi$ の両方から象限を確定する
- [ ] 半角公式の符号は角の範囲で決める
- [ ] 扇形の公式に度数法の角度をそのまま代入しない

详细讲解见本项目各细目页（从[三角関数简介](index.md)进入）。
