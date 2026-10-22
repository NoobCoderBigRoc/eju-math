---
title: 向量
---

# 向量

## 考纲要求

向量的和差、实数倍、分量表示、内积、位置向量与分点公式、用向量处理图形（垂直/平行/夹角/长度）。

## 运算与分量

$\vec{a} = (a_1, a_2)$，$\vec{b} = (b_1, b_2)$：

$$
\vec{a} + \vec{b} = (a_1 + b_1,\ a_2 + b_2), \qquad k\vec{a} = (ka_1, ka_2)
$$

平行：$\vec{a} \parallel \vec{b} \iff a_1 b_2 - a_2 b_1 = 0$。

## 内积

$$
\vec{a} \cdot \vec{b} = |\vec{a}|\,|\vec{b}|\cos\theta = a_1 b_1 + a_2 b_2
$$

- 垂直：$\vec{a} \cdot \vec{b} = 0$；
- 夹角：$\cos\theta = \dfrac{\vec a \cdot \vec b}{|\vec a|\,|\vec b|}$；
- $|\vec{a}| = \sqrt{\vec a \cdot \vec a}$。

**分配律**成立；但向量**没有除法**。

## 位置向量与分点

以点 $O$ 为原点，$\vec{OP} = \vec{p}$ 等：

$$
\vec{p} = \frac{\vec{a} + \vec{b}}{2}\ \text{(中点)}, \qquad \vec{p} = \frac{n\vec{a} + m\vec{b}}{m+n}\ \text{(内分 } m:n\text{)}
$$

三点 $A, B, C$ 共线 $\iff \vec{OC} = t\vec{OB} + (1-t)\vec{OA}$（系数和为 1）。

## 典型例题

??? example "例题：内积求夹角"
    $\vec{a} = (1, 2)$，$\vec{b} = (3, -1)$，求夹角 $\theta$。

    **解答**：

    $$
    \cos\theta = \frac{1\cdot3 + 2\cdot(-1)}{\sqrt5\,\sqrt{10}} = \frac{1}{5\sqrt2} = \frac{\sqrt2}{10}
    $$

??? example "例题：垂线条件"
    $\vec{a} + t\vec{b}$ 与 $\vec{a}$ 垂直（$\vec{a}\cdot\vec{b} \ne 0$），求 $t$。

    **解答**：$(\vec a + t\vec b)\cdot\vec a = |\vec a|^2 + t\,\vec a \cdot \vec b = 0$，故 $t = -\dfrac{|\vec a|^2}{\vec a \cdot \vec b}$。

## 易错点

- [x] 内积不满足结合律 $(\vec a \cdot \vec b)\cdot\vec c$ 无意义；
- [x] 垂直用 $\cos\theta = 0$，平行用行列式为 0，两者公式别混用。
