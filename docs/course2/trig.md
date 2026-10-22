---
title: 三角函数
---

# 三角函数

## 考纲要求

任意角与弧度制、一般角的三角函数、加法定理及其推论（倍角、和差化积）、三角函数图像与周期、三角方程与不等式。

## 弧度制

$$
\theta\ (\text{rad}) \times r = \text{弧长}, \qquad 180° = \pi\ \text{rad}
$$

## 加法定理（全站最重要的公式组）

$$
\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta
$$

$$
\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta
$$

$$
\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}
$$

## 倍角·半角

$$
\sin 2\alpha = 2\sin\alpha\cos\alpha
$$

$$
\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1
$$

半角：$\displaystyle\sin^2\frac{\alpha}{2} = \frac{1-\cos\alpha}{2},\quad \cos^2\frac{\alpha}{2} = \frac{1+\cos\alpha}{2}$

## 积化和差·和差化积

$$
\sin\alpha\cos\beta = \tfrac12\{\sin(\alpha+\beta) + \sin(\alpha-\beta)\}
$$

$$
\sin\alpha + \sin\beta = 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}
$$

## 合成（辅助角形式）

$$
a\sin\theta + b\cos\theta = \sqrt{a^2+b^2}\,\sin(\theta + \varphi), \quad \tan\varphi = \frac{b}{a}\ (a>0)
$$

## 图像与周期

$y = \sin\theta$ 周期 $2\pi$；$y = \tan\theta$ 周期 $\pi$。$y = a\sin(b\theta + c) + d$：振幅 $|a|$，周期 $\dfrac{2\pi}{b}$。

## 典型例题

??? example "例题：合成求最值"
    求 $f(\theta) = \sin\theta + \sqrt3\cos\theta$ 的最大值。

    **解答**：

    $$
    f(\theta) = 2\sin\left(\theta + \frac{\pi}{3}\right) \le 2
    $$

    最大值 2，此时 $\theta = \dfrac{\pi}{6} + 2k\pi$。

## 易错点

- [x] 加法定理正余弦的中间符号方向（sin 同号、cos 反号）；
- [x] 解三角方程时**周期性导致解不唯一**，必须写成通解；
- [x] 角度范围限制（$0 \le \theta < 2\pi$）下漏解或多解。
