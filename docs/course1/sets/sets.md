---
title: 集合
---

# 集合

- $a \in A$（属于）、$A \subset B$（子集）、$A \cap B$（交集）、$A \cup B$（并集）、$\overline{A}$（补集）、$\varnothing$（空集）
- 德摩根律：$\overline{A \cup B} = \overline{A} \cap \overline{B}$、$\overline{A \cap B} = \overline{A} \cup \overline{B}$

## 集合の要素の個数

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

3 个集合时再加 $n(A \cap B \cap C)$、减去两两交集。用文氏图（ベン図）整理最稳妥。

??? example "演習：要素の個数"
    **问题**

    40人のクラスで、数学が好きな生徒は24人、英語が好きな生徒は19人、両方好きな生徒は11人である。どちらも好きでない生徒は何人か。

    **答案**

    8 人

    **思路**

    先求「至少喜欢一科」的人数，再用全班人数减。

    **解答**

    $$n(A \cup B) = 24 + 19 - 11 = 32, \qquad 40 - 32 = 8 \text{（人）}$$

## 易错点

- [ ] $n(A \cup B)$ 忘记减去重复计数的 $n(A \cap B)$
- [ ] 「A または B」（或）是并集、「A かつ B」（且）是交集，别读反
