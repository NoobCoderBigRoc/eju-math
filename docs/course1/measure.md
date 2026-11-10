---
title: 図形と計量
---

# 4. 図形と計量

## シラバスとの対応

| 項目 | 内容 |
| --- | --- |
| 出題項目 | 4. 図形と計量（数学I） |
| 細目 | (1) 三角比：①正弦、余弦、正接 ②三角比の相互関係　(2) 三角比と図形：①正弦定理、余弦定理 ②図形の計量（空間図形への応用を含む） |
| コース | コース1・コース2 共通。[三角関数](../course2/trig.md) の基礎 |

## 1. 三角比と相互関係

直角三角形（$\theta$ は鋭角）では

$$
\sin\theta = \frac{\text{対辺}}{\text{斜辺}}, \qquad \cos\theta = \frac{\text{隣辺}}{\text{斜辺}}, \qquad \tan\theta = \frac{\text{対辺}}{\text{隣辺}}
$$

$0^\circ \leqq \theta \leqq 180^\circ$ では、原点を中心とする半径 $r$ の半円と動径の交点 $(x, y)$ を使って $\sin\theta = \dfrac{y}{r}$、$\cos\theta = \dfrac{x}{r}$、$\tan\theta = \dfrac{y}{x}$ と拡張する。**相互関係**：

$$
\sin^2\theta + \cos^2\theta = 1, \qquad \tan\theta = \frac{\sin\theta}{\cos\theta}, \qquad 1 + \tan^2\theta = \frac{1}{\cos^2\theta}
$$

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\sin\theta$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{1}{2}$ | $0$ |
| $\cos\theta$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{1}{2}$ | $0$ | $-\frac{1}{2}$ | $-\frac{\sqrt2}{2}$ | $-\frac{\sqrt3}{2}$ | $-1$ |
| $\tan\theta$ | $0$ | $\frac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | — | $-\sqrt3$ | $-1$ | $-\frac{1}{\sqrt3}$ | $0$ |

## 2. 正弦定理・余弦定理

$\triangle ABC$ の外接円の半径を $R$ とする。

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R \qquad \text{（正弦定理）}
$$

$$
a^2 = b^2 + c^2 - 2bc\cos A \qquad \text{（余弦定理）}, \qquad \cos A = \frac{b^2 + c^2 - a^2}{2bc}
$$

使い分け：**2 辺とその間の角**（または 3 辺）が分かれば余弦定理、**1 辺と 2 角**が分かれば正弦定理。

## 3. 図形の計量

$$
S = \frac{1}{2}bc\sin A = \frac{1}{2}ca\sin B = \frac{1}{2}ab\sin C, \qquad S = \frac{abc}{4R} = 2R^2 \sin A \sin B \sin C
$$

ヘロンの公式：$s = \dfrac{a + b + c}{2}$ として $S = \sqrt{s(s - a)(s - b)(s - c)}$。

空間図形では、問題の局面を切り取る**断面（平面図形）**に帰着させるのが基本方針である（正四面体の体積は $V = \dfrac{\sqrt{2}}{12}a^3$）。

## 例題（演習）

??? example "例題 1：余弦定理"
    $\triangle ABC$ において、$b = 3$、$c = 5$、$A = 120^\circ$ のとき、$a$ を求めよ。

    **考え方**：2 辺とその間の角が分かっているので余弦定理。$\cos 120^\circ = -\dfrac{1}{2}$ に注意。

    **解答**：

    $$
    a^2 = 3^2 + 5^2 - 2 \cdot 3 \cdot 5 \cos 120^\circ = 34 - 30 \cdot \left(-\frac{1}{2}\right) = 49
    $$

    **答え**：$a = 7$

??? example "例題 2：正弦定理"
    $\triangle ABC$ において、$A = 45^\circ$、$B = 60^\circ$、$a = 2$ のとき、$b$ を求めよ。

    **考え方**：1 辺と 2 角が分かっているので正弦定理。

    **解答**：

    $$
    \frac{2}{\sin 45^\circ} = \frac{b}{\sin 60^\circ} \implies b = 2 \cdot \frac{\sqrt{3}/2}{\sqrt{2}/2} = \sqrt{6}
    $$

    **答え**：$b = \sqrt{6}$

??? example "例題 3：空間図形への応用"
    1 辺の長さが $2$ の正四面体の体積を求めよ。

    **考え方**：頂点から底面におろした垂線の足は底面の正三角形の重心に一致する。高さを求めてから $V = \dfrac{1}{3} \times \text{底面積} \times \text{高さ}$。

    **解答**：底面は 1 辺 $2$ の正三角形で面積 $\sqrt{3}$。高さは $\sqrt{2^2 - \left(\dfrac{2}{\sqrt{3}}\right)^2} = \sqrt{\dfrac{8}{3}}$。よって $V = \dfrac{1}{3} \cdot \sqrt{3} \cdot \sqrt{\dfrac{8}{3}} = \dfrac{2\sqrt{2}}{3}$。

    **答え**：$\dfrac{2\sqrt{2}}{3}$

## よくあるミス

- [ ] 鈍角の $\cos$ が負であることを忘れる（$120^\circ$、$135^\circ$、$150^\circ$ は頻出）
- [ ] 正弦定理と余弦定理の選択ミス（「2 辺と間の角→余弦」「1 辺と 2 角→正弦」が原則）
- [ ] 面積公式の $\dfrac{1}{2}$ を落とす
- [ ] $\sin$ の値から角を求めるとき、鈍角の可能性がある場合に 2 通りの答えを見落とす

## 関連項目

- 応用：[図形の性質](geometry.md)、空間は [ベクトル](../course2/vector.md) でも扱う
- 角を一般化すると [三角関数](../course2/trig.md) になる
