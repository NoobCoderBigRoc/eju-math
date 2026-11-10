---
title: 図形と計量
---

# 4. 図形と計量

## 与考纲的对应

| 项目 | 内容 |
| --- | --- |
| 考纲项目 | 4. 図形と計量（数学I） |
| 细目 | (1) 三角比：①正弦、余弦、正接 ②三角比の相互関係　(2) 三角比と図形：①正弦定理、余弦定理 ②図形の計量（空間図形への応用を含む） |
| 适用课程 | Course 1 与 Course 2 共同，是 [三角関数](../course2/trig.md) 的基础 |

## 1. 三角比と相互関係

直角三角形（$\theta$ 为锐角）中的定义：

$$
\sin\theta = \frac{\text{対辺}}{\text{斜辺}}, \qquad \cos\theta = \frac{\text{隣辺}}{\text{斜辺}}, \qquad \tan\theta = \frac{\text{対辺}}{\text{隣辺}}
$$

$0^\circ \leqq \theta \leqq 180^\circ$ 时，用原点为圆心、半径 $r$ 的半圆与动径的交点 $(x, y)$ 推广：$\sin\theta = \dfrac{y}{r}$、$\cos\theta = \dfrac{x}{r}$、$\tan\theta = \dfrac{y}{x}$。**相互関係**（互相关系式）如下：

$$
\sin^2\theta + \cos^2\theta = 1, \qquad \tan\theta = \frac{\sin\theta}{\cos\theta}, \qquad 1 + \tan^2\theta = \frac{1}{\cos^2\theta}
$$

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\sin\theta$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{1}{2}$ | $0$ |
| $\cos\theta$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{1}{2}$ | $0$ | $-\frac{1}{2}$ | $-\frac{\sqrt2}{2}$ | $-\frac{\sqrt3}{2}$ | $-1$ |
| $\tan\theta$ | $0$ | $\frac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | — | $-\sqrt3$ | $-1$ | $-\frac{1}{\sqrt3}$ | $0$ |

钝角的值不用死背：用 $180^\circ - \theta$ 的锐角值加符号（sin 为正、cos 与 tan 为负）即可还原。

## 2. 正弦定理・余弦定理

$\triangle ABC$ 的外接圆半径记为 $R$：

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R \qquad \text{（正弦定理）}
$$

$$
a^2 = b^2 + c^2 - 2bc\cos A \qquad \text{（余弦定理）}, \qquad \cos A = \frac{b^2 + c^2 - a^2}{2bc}
$$

选用原则：**两边及其夹角**（或三边）已知用余弦定理，**一边和两角**已知用正弦定理。拿不准时先想「我想求的量出现在哪个公式里」。

## 3. 図形の計量

$$
S = \frac{1}{2}bc\sin A = \frac{1}{2}ca\sin B = \frac{1}{2}ab\sin C, \qquad S = \frac{abc}{4R} = 2R^2 \sin A \sin B \sin C
$$

ヘロンの公式：$s = \dfrac{a + b + c}{2}$ 时 $S = \sqrt{s(s - a)(s - b)(s - c)}$。

空间图形的基本方针是把问题切到一个**截面（平面图形）**里解决（正四面体的体积公式是 $V = \dfrac{\sqrt{2}}{12}a^3$，其推导就是切截面求高）。

## 例题（演习）

??? example "例题 1：余弦定理"
    $\triangle ABC$ において、$b = 3$、$c = 5$、$A = 120^\circ$ のとき、$a$ を求めよ。

    **思路**：两边及夹角已知，用余弦定理。注意 $\cos 120^\circ = -\dfrac{1}{2}$。

    **解答**：

    $$
    a^2 = 3^2 + 5^2 - 2 \cdot 3 \cdot 5 \cos 120^\circ = 34 - 30 \cdot \left(-\frac{1}{2}\right) = 49
    $$

    **答案**：$a = 7$

??? example "例题 2：正弦定理"
    $\triangle ABC$ において、$A = 45^\circ$、$B = 60^\circ$、$a = 2$ のとき、$b$ を求めよ。

    **思路**：一边和两角已知，用正弦定理。

    **解答**：

    $$
    \frac{2}{\sin 45^\circ} = \frac{b}{\sin 60^\circ} \implies b = 2 \cdot \frac{\sqrt{3}/2}{\sqrt{2}/2} = \sqrt{6}
    $$

    **答案**：$b = \sqrt{6}$

??? example "例题 3：空間図形への応用"
    1 辺の長さが $2$ の正四面体の体積を求めよ。

    **思路**：顶点向底面作垂线，垂足落在底面正三角形的重心上。先求高，再用 $V = \dfrac{1}{3} \times \text{底面积} \times \text{高}$。

    **解答**：底面是边长 $2$ 的正三角形，面积 $\sqrt{3}$。高为 $\sqrt{2^2 - \left(\dfrac{2}{\sqrt{3}}\right)^2} = \sqrt{\dfrac{8}{3}}$。于是 $V = \dfrac{1}{3} \cdot \sqrt{3} \cdot \sqrt{\dfrac{8}{3}} = \dfrac{2\sqrt{2}}{3}$。

    **答案**：$\dfrac{2\sqrt{2}}{3}$

## 易错点

- [ ] 忘了钝角的 $\cos$ 是负数（$120^\circ$、$135^\circ$、$150^\circ$ 高频出现）
- [ ] 正弦定理与余弦定理选错（原则：「两边夹角→余弦」「一边两角→正弦」）
- [ ] 面积公式漏乘 $\dfrac{1}{2}$
- [ ] 由 $\sin$ 值反求角时漏掉钝角的那一种可能

## 相关条目

- 应用：[図形の性質](geometry.md)；空间问题在 [ベクトル](../course2/vector.md) 中还会遇到
- 把角推广到任意角就是 [三角関数](../course2/trig.md)
