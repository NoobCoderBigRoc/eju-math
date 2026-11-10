---
title: 三角比の相互関係
---

# 三角比の相互関係

## 3 つの基本公式

- $\sin^2\theta + \cos^2\theta = 1$
- $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$
- $1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$

## 公式の出どころ

単位円（半径 1）上の点 $(\cos\theta, \sin\theta)$ が円の方程式 $x^2 + y^2 = 1$ を満たすことから第 1 式が出る（三平方の定理そのもの）。第 3 式は第 1 式の両辺を $\cos^2\theta$ で割ったもので、新しい公式として暗記するより「割れば出る」と理解するのが確実。

変形して使う形も多い：$\sin^2\theta = 1 - \cos^2\theta$、$\cos^2\theta = 1 - \sin^2\theta$。

## 使い方：1 つ分かれば残りが決まる

$\sin\theta$、$\cos\theta$、$\tan\theta$ のうち 1 つが分かれば、相互関係から残り 2 つが決まる。手順は：

1. $\sin^2\theta + \cos^2\theta = 1$ で $\sin$ と $\cos$ の**絶対値**を求める。
2. $\theta$ の範囲（鋭角か鈍角か）で**符号**を決定する。鈍角（$90^\circ < \theta < 180^\circ$）では $\sin$ は正、$\cos$ と $\tan$ は負。
3. $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$ で割り算する。

順序が逆（符号を考えずに平方根だけ取る）だと、鈍角の場合に符号を落とす。

## 補角の関係も相互関係の一種

[正弦・余弦・正接](trig-definitions.md) の $\sin(180^\circ - \theta) = \sin\theta$、$\cos(180^\circ - \theta) = -\cos\theta$、$\tan(180^\circ - \theta) = -\tan\theta$ は、三角形の内角（$\sin$ が鈍角でも正など）を扱うときの橋渡しになる。特に $\sin$ は補角で値が変わらないため、正弦定理で角を求めると解が 2 つに割れる原因になる（[正弦定理・余弦定理](sine-cosine-laws.md)）。

## 易错点

- [ ] 钝角的 $\cos$、$\tan$ 是负数（$90^\circ$ 的 $\tan$ 不存在）
- [ ] 单位是度（°），与数学II的弧度制（三角関数）不要混用
- [ ] $\sin^2\theta$ の読み違い（$(\sin\theta)^2$ の意味で、$\sin(\theta^2)$ ではない）
