---
title: 图形与计量
---

# 图形与计量（三角比）

## 考纲要求

锐角三角比、钝角三角比（坐标定义）、正弦定理、余弦定理、三角形面积与图形综合。Course 1 必考板块，也直接衔接 Course 2 的三角函数。

## 三角比定义

在直角三角形中：

$$
\sin\theta = \frac{\text{对边}}{\text{斜边}}, \quad \cos\theta = \frac{\text{邻边}}{\text{斜边}}, \quad \tan\theta = \frac{\text{对边}}{\text{邻边}}
$$

推广到任意角（终边与单位圆交点 $(x, y)$，半径 $r$）：

$$
\sin\theta = \frac{y}{r}, \quad \cos\theta = \frac{x}{r}, \quad \tan\theta = \frac{y}{x}
$$

## 基本关系

$$
\sin^2\theta + \cos^2\theta = 1, \qquad \tan\theta = \frac{\sin\theta}{\cos\theta}
$$

## 特殊角数值

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ |
| --- | --- | --- | --- | --- | --- |
| $\sin\theta$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$ |
| $\cos\theta$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{1}{2}$ | $0$ |
| $\tan\theta$ | $0$ | $\frac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | — |

## 正弦定理与余弦定理

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R \quad (R\ \text{为外接圆半径})
$$

$$
a^2 = b^2 + c^2 - 2bc\cos A
$$

$$
S = \frac{1}{2}ab\sin C = \frac{1}{2}bc\sin A = \frac{1}{2}ca\sin B
$$

## 典型例题

??? example "例题：余弦定理求边"
    在 $\triangle ABC$ 中，$b = 3$，$c = 5$，$A = 120°$，求 $a$。

    **解答**：

    $$
    a^2 = 9 + 25 - 2 \cdot 3 \cdot 5 \cdot \cos 120° = 34 - 30 \cdot \left(-\frac12\right) = 49
    $$

    故 $a = 7$。

!!! tip "口诀"
    余弦定理结构：**平方和减两倍积乘夹角余弦**。$\cos 120° = -\dfrac12$ 是真题最爱。

## 易错点

- [x] 钝角情形下 $\cos\theta < 0$，符号处理错误；
- [x] 混淆"求角"与"求边"时正弦/余弦定理的选择（知两边夹角用余弦，知两角一边用正弦）；
- [x] 面积公式漏乘 $\frac12$。
