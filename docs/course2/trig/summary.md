---
title: 三角関数要点总结
---

# 三角関数要点总结

考前确认本页：弧度法与単位円的定义，以加法定理为起点的一整套公式派生关系（2倍角・半角・合成）。

## 公式・定理清单

### 三角関数

- 単位円による定義：对动径与単位円的交点 $P(x, y)$，$\sin\theta = y$、$\cos\theta = x$、$\tan\theta = \dfrac{y}{x}$（$x \ne 0$）—— $\tan\theta$ 无定义的角是 $\theta = \dfrac{\pi}{2} + n\pi$
- 弧度法：$\pi\ \mathrm{rad} = 180^\circ$、$\theta = \dfrac{\text{弧の長さ}}{\text{半径}}$ —— 从度换成弧度要乘 $\dfrac{\pi}{180}$
- 扇形：弧長 $l = r\theta$、面積 $S = \dfrac{1}{2}r^2\theta = \dfrac{1}{2}lr$ —— 只在 $\theta$ 用弧度法时成立
- 相互関係：$\sin^2\theta + \cos^2\theta = 1$、$\tan\theta = \dfrac{\sin\theta}{\cos\theta}$、$1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$
- 周期と奇偶性：$\sin$、$\cos$ 的周期是 $2\pi$，$\tan$ 的周期是 $\pi$；$\sin$、$\tan$ 是奇関数，$\cos$ 是偶関数
- 誘導公式の整理：含 $\pi$ 的变换中 $\sin$ 与 $\cos$ 不互换，含 $\dfrac{\pi}{2}$ 的变换中互换
- グラフ $y = a\sin(bx + c) + d$：振幅 $|a|$、周期 $\dfrac{2\pi}{b}$、平移量 $-\dfrac{c}{b}$ —— $y = \tan x$ 的漸近線是 $x = \dfrac{\pi}{2} + n\pi$

### 加法定理

- $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$ —— 符号与左式同向
- $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$ —— 符号与左式相反
- $\tan(\alpha \pm \beta) = \dfrac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$
- 2 倍角：$\sin 2\alpha = 2\sin\alpha\cos\alpha$、$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha$ —— $\cos 2\alpha$ 按题目需要在三种形式中选用
- 半角：$\sin^2\dfrac{\alpha}{2} = \dfrac{1 - \cos\alpha}{2}$、$\cos^2\dfrac{\alpha}{2} = \dfrac{1 + \cos\alpha}{2}$ —— 值的符号由角的范围决定
- 積和・和積の公式：由加法定理两边相加减得到 —— 考场上可以现推
- 合成：$a\sin\theta + b\cos\theta = \sqrt{a^2 + b^2}\sin(\theta + \varphi)$（$\cos\varphi = \dfrac{a}{\sqrt{a^2 + b^2}}$、$\sin\varphi = \dfrac{b}{\sqrt{a^2 + b^2}}$）—— 振幅直接就是最大值

## 解法パターン

- **非特殊角的值**：$75^\circ$ 这样的角 → 分解为 $45^\circ + 30^\circ$ 等特殊角的和、差，再用加法定理
- **由一个值求其他值**：只给出 $\sin\theta$ 的值时 → 先用相互関係求绝对值，再按象限定符号
- **最大・最小**：$a\sin\theta + b\cos\theta$ 的形式 → 合成为一个 $\sin$，读振幅与相位
- **方程式・不等式**：种类与次数混杂时 → 用 2 倍角或合成统一成 $\sin$ 或 $\cos$ 一种再解，不要漏掉范围内的解
- **读图**：$y = a\sin(bx + c) + d$ → 变形为 $bx + c = b\left(x + \dfrac{c}{b}\right)$，读周期 $\dfrac{2\pi}{b}$ 与平移 $-\dfrac{c}{b}$

## 考前注意

- [ ] $\tan$ 的周期是 $\pi$ 而不是 $2\pi$；无定义的角 $\theta = \dfrac{\pi}{2} + n\pi$ 也不要漏看
- [ ] $\cos(\alpha + \beta)$ 的加法定理符号与左式相反
- [ ] 合成的角 $\varphi$ 要由 $\sin\varphi$、$\cos\varphi$ 两者共同确定象限
- [ ] 半角公式的符号由角的范围决定
- [ ] 不要把度数法的角度直接代入扇形的公式

详细讲解见本项目各细目页（从[三角関数简介](index.md)进入）。
