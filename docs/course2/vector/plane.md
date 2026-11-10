---
title: 平面上のベクトル
---

# 平面上のベクトル

## 1. ベクトルとその演算・成分

$\vec{a} = (a_1, a_2)$；加法/数乘按成分运算；大小 $|\vec{a}| = \sqrt{a_1^2 + a_2^2}$。平行条件：$\vec{b} = k\vec{a}$（成分成比例）。

## 2. ベクトルの内積

$$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1 b_1 + a_2 b_2$$

垂直条件 $\vec{a} \cdot \vec{b} = 0$；夹角 $\cos\theta = \dfrac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}$。内积为 0 是判定垂直最快的工具。

??? example "演習：内積と垂直条件"
    **问题**

    $\vec{a} = (2, 1)$、$\vec{b} = (1, k)$ が垂直であるような $k$ の値を求めよ。

    **答案**

    $k = -2$

    **思路**

    垂直 ⇔ 内积为 0。

    **解答**

    $$\vec{a} \cdot \vec{b} = 2 \cdot 1 + 1 \cdot k = 0 \quad\Longrightarrow\quad k = -2$$

??? example "演習：内積と角度"
    **问题**

    $\vec{a} = (1, 0)$、$\vec{b} = (1, \sqrt{3})$ のなす角を求めよ。

    **答案**

    $60^\circ$

    **思路**

    内积 $= 1$，模长 $|\vec{a}| = 1$、$|\vec{b}| = 2$，$\cos\theta = \dfrac{1}{2}$。

    **解答**

    $$\cos\theta = \frac{1}{1 \cdot 2} = \frac{1}{2} \quad\Longrightarrow\quad \theta = 60^\circ$$

## 易错点

- [ ] 内積が0＝垂直だが、$\vec{0}$ の扱い（零向量）には注意
