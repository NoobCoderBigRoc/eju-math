---
title: 数与式
---

# 数与式

## 考纲要求

实数的四则运算与有理化、多项式的展开与因式分解、绝对值方程与不等式。在 EJU 中通常作为**前 2–3 题**出现，属于"必须全对"的基础分。

## 核心公式

### 乘法公式

$$
(a \pm b)^2 = a^2 \pm 2ab + b^2, \qquad (a+b)(a-b) = a^2 - b^2
$$

$$
(a+b)(c+d) = ac + ad + bc + bd, \qquad (a\pm b)^3 = a^3 \pm 3a^2 b + 3ab^2 \pm b^3
$$

$$
a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)
$$

### 因式分解常用型

$$
x^2 + (a+b)x + ab = (x+a)(x+b)
$$

$$
acx^2 + (ad+bc)x + bd = (ax+b)(cx+d)
$$

### 有理化

$$
\frac{1}{\sqrt{a} \pm \sqrt{b}} = \frac{\sqrt{a} \mp \sqrt{b}}{a - b}
$$

## 绝对值

对 $a > 0$：

$$
|x| < a \iff -a < x < a, \qquad |x| > a \iff x < -a \ \text{或}\ x > a
$$

## 集合与命题

EJU 把「集合と論理」并入数与式，几乎每年 1 题。

**集合运算**：$A \cup B$（并集）、$A \cap B$（交集）、$\overline{A}$（补集，全集 $U$ 下）。

**元素个数**（容斥原理）：

$$
n(A \cup B) = n(A) + n(B) - n(A \cap B)
$$

$$
n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A\cap B) - n(B \cap C) - n(C \cap A) + n(A \cap B \cap C)
$$

**命题与条件**：

- $p \Rightarrow q$ 的**逆否**是 $\overline{q} \Rightarrow \overline{p}$，两者等价；
- 「$p$ 是 $q$ 的充分条件」$\iff p \Rightarrow q$；「必要条件」$\iff q \Rightarrow p$；
- 「$\iff$」表示充分必要（必要十分条件）。

**量词否定**：$\forall x\, P(x)$ 的否定是 $\exists x\, \overline{P(x)}$。

## 典型例题

??? example "例题 1：因式分解"
    分解 $x^2 + 3x - 10$。

    **解答**：找两个数 $p, q$ 使 $pq = -10$，$p+q = 3$，得 $5, -2$。

    $$
    x^2 + 3x - 10 = (x+5)(x-2)
    $$

??? example "例题 2：有理化求值"
    求 $\dfrac{\sqrt{5} + \sqrt{3}}{\sqrt{5} - \sqrt{3}}$ 的值，并化为 $a + b\sqrt{15}$ 的形式。

    **解答**：分子分母同乘 $(\sqrt{5} + \sqrt{3})$：

    $$
    \frac{(\sqrt{5}+\sqrt{3})^2}{5-3} = \frac{8 + 2\sqrt{15}}{2} = 4 + \sqrt{15}
    $$

## 易错点

- [x] 展开含负号的多项式时漏乘（$-(a-b)^2 \ne -a^2 - b^2$）；
- [x] 绝对值方程要**分情况讨论**后验证是否有增根；
- [x] EJU 题干常写「いずれ」「すべて」等限定词，注意答案形式要求（如「最简形式」）。
