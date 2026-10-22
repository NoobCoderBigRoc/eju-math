---
title: 复数平面
---

# 复数平面

## 考纲要求

复数的几何表示、共轭复数、极形式与模、棣莫弗定理、复数与旋转、圆与线段的复数表示。

## 极形式

复数 $z = a + bi$ 的极形式：

$$
z = r(\cos\theta + i\sin\theta) = re^{i\theta}
$$

其中 $r = |z| = \sqrt{a^2 + b^2}$，$\tan\theta = \dfrac{b}{a}$。

## 乘除法的几何意义

$$
z_1 z_2 = r_1 r_2 \left(\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)\right)
$$

**乘以 $re^{i\theta}$ = 放大 $r$ 倍 + 逆时针旋转 $\theta$**。这是旋转问题秒杀技巧：

- 乘 $i$：逆时针转 $90°$；
- 乘 $-\dfrac12 \pm \dfrac{\sqrt3}{2}i$：转 $\pm 120°$；
- 乘 $\dfrac{\sqrt2}{2}(1+i)$：转 $45°$。

## 棣莫弗定理

$$
(re^{i\theta})^n = r^n e^{in\theta}, \qquad (\cos\theta + i\sin\theta)^n = \cos n\theta + i \sin n\theta
$$

## 共轭与模

$$
\overline{z} = a - bi, \qquad z\overline{z} = |z|^2, \qquad |z_1 z_2| = |z_1||z_2|
$$

## 轨迹的复数表示

- $|z - z_0| = r$：以 $z_0$ 为圆心、半径 $r$ 的圆；
- $|z - z_1| = |z - z_2|$：$z_1, z_2$ 连线段的垂直平分线。

## 典型例题

??? example "例题：旋转求点"
    点 $P$ 对应 $z = 1 + i$，将 $P$ 绕原点逆时针旋转 $90°$，求新点对应的复数。

    **解答**：$z' = iz = i(1+i) = -1 + i$。

## 易错点

- [x] 辐角是多值的，主值范围通常为 $0 \le \theta < 2\pi$ 或 $-\pi < \theta \le \pi$（看清题意）；
- [x] $|z_1 + z_2| \le |z_1| + |z_2|$（三角不等式）取等条件是同向。
