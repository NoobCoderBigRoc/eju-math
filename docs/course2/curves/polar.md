---
title: 極座標と極方程式
---

# 極座標と極方程式

点用 $(r, \theta)$ 表示：$x = r\cos\theta$、$y = r\sin\theta$、$r = \sqrt{x^2 + y^2}$。

- 直线 $x = a$：$r\cos\theta = a$；圆 $x^2 + y^2 = ax$：$r = a\cos\theta$
- 心脏线（カージオイド）$r = a(1 + \cos\theta)$、螺旋 $r = a\theta$ 是典型极方程曲线
- 面积：$S = \dfrac{1}{2}\int r^2\, d\theta$（极坐标扇形面积，与 [積分法](../integration/integral-basics.md) 衔接）

??? example "演習：極方程式"
    **问题**

    極方程式 $r = 2\cos\theta$ の表す曲線を直交座標の方程式で表せ。

    **答案**

    $(x - 1)^2 + y^2 = 1$

    **思路**

    两边乘 $r$：$r^2 = 2r\cos\theta$，换成直交坐标 $x^2 + y^2 = 2x$ 后平方完成。

    **解答**

    $$x^2 + y^2 = 2x \quad\Longrightarrow\quad (x - 1)^2 + y^2 = 1$$

    （中心 $(1, 0)$、半径 1 的圆。）

## 易错点

- [ ] $r$ が負の場合の点の取り方（$r$ 为负时点的画法约定）
