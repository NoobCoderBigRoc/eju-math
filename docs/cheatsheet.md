---
title: 公式速查
---

# 公式チェックシート

試験直前の確認用に、項目ごとに要の公式を集めた。各見出しから詳しいページへ移動できる。

## 数と式 · [详解](course1/numbers.md)

$$
(a\pm b)^2 = a^2 \pm 2ab + b^2, \qquad a^3 \pm b^3 = (a\pm b)(a^2 \mp ab + b^2)
$$

## 集合と命題 · [详解](course1/sets.md)

$$
n(A \cup B) = n(A) + n(B) - n(A \cap B)
$$

## 2次関数 · [详解](course1/quadratic.md)

$$
y = a\left(x + \frac{b}{2a}\right)^2 + \frac{4ac - b^2}{4a}, \qquad D = b^2 - 4ac
$$

| $D$ | 実数解 |
| --- | --- |
| $>0$ | 異なる 2 つ |
| $=0$ | 重解 |
| $<0$ | なし |

## 図形と計量 · [详解](course1/measure.md)

$$
\frac{a}{\sin A} = 2R, \qquad a^2 = b^2 + c^2 - 2bc\cos A, \qquad S = \frac12 ab\sin C
$$

## 図形の性質 · [详解](course1/geometry.md)

$$
PA \cdot PB = PT^2, \qquad \frac{S_1}{S_2} = \left(\frac{a_1}{a_2}\right)^2
$$

## 場合の数と確率 · [详解](course1/probability.md)

$$
{}_nC_r = \frac{n!}{r!(n-r)!}, \qquad P(A \cup B) = P(A)+P(B)-P(A\cap B), \qquad {}_nC_r p^r (1-p)^{n-r} \ \text{（反復試行）}
$$

## 整数の性質 · [详解](course1/integer.md)

$$
n = \prod p_i^{a_i} \implies \text{約数の個数} = \prod (a_i + 1), \qquad \mathrm{gcd}(a,b)\cdot\mathrm{lcm}(a,b) = ab
$$

## いろいろな式 · [详解](course2/polynomials.md)

$$
(a+b)^n = \sum_{k=0}^{n} {}_nC_k a^{n-k} b^k, \qquad \alpha + \beta + \gamma = -p, \quad \alpha\beta\gamma = -r
$$

## 図形と方程式 · [详解](course2/geometry-equation.md)

$$
d = \frac{|ax_1 + by_1 + c|}{\sqrt{a^2 + b^2}} \ \text{（点と直線の距離）}
$$

## 指数関数・対数関数 · [详解](course2/explog.md)

$$
\log_a xy = \log_a x + \log_a y, \qquad \log_a b = \frac{\log_c b}{\log_c a}
$$

## 三角関数 · [详解](course2/trig.md)

$$
\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta, \qquad a\sin\theta + b\cos\theta = \sqrt{a^2+b^2}\sin(\theta + \varphi)
$$

## 数列 · [详解](course2/sequence.md)

$$
S_n = \frac{n(a_1 + a_n)}{2}, \qquad S_n = \frac{a(r^n - 1)}{r-1}, \qquad \sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

## 確率分布 · [详解](course2/probability-distribution.md)

$$
E(X) = \sum x_k p_k, \qquad V(X) = E(X^2) - \{E(X)\}^2, \qquad E(aX + b) = aE(X) + b
$$

## ベクトル · [详解](course2/vector.md)

$$
\vec a \cdot \vec b = a_1b_1 + a_2b_2 = |\vec a||\vec b|\cos\theta
$$

## 複素数平面 · [详解](course2/complex.md)

$$
z = r(\cos\theta + i\sin\theta), \qquad (\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta
$$

## 式と曲線 · [详解](course2/curves.md)

$$
y^2 = 4px, \qquad \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, \qquad \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
$$

## 極限 · [详解](course2/limits.md)

$$
S = \frac{a}{1 - r} \ (|r| < 1), \qquad \lim_{x \to 0} \frac{\sin x}{x} = 1
$$

## 微分法 · [详解](course2/differentiation.md)

$$
(x^n)' = nx^{n-1}, \qquad \{f(g(x))\}' = f'(g(x))g'(x), \qquad y - f(a) = f'(a)(x - a) \ \text{（接線）}
$$

## 積分法 · [详解](course2/integration.md)

$$
\int_a^b f(x)\,dx = F(b) - F(a), \qquad S = \int_a^b \{f(x) - g(x)\}\,dx, \qquad V = \pi\int_a^b \{f(x)\}^2\,dx
$$
