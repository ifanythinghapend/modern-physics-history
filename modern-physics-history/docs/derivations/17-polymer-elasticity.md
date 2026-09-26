# 推导札记：没有拉长化学键，回复力也能出现

考虑三维理想自由连接链：$N\gg1$ 个独立、各向同性的链段，每段长度 $\ell$。端到端向量是
$\mathbf R=\sum_{i=1}^N\mathbf r_i$。
各链段均值为零，且不同链段的交叉平均为零，所以

$$
\langle R^2\rangle
=\sum_i\langle r_i^2\rangle
+2\sum_{i<j}\langle\mathbf r_i\cdot\mathbf r_j\rangle
=N\ell^2.
$$

在高斯近似有效的伸长范围内，端到端向量的概率密度为

$$
P(\mathbf R)\propto
\exp\left[-\frac{3R^2}{2N\ell^2}\right].
$$

固定 $\mathbf R$ 时，构型自由能的变化因此是

$$
F(\mathbf R)-F(0)
=-k_BT\log\frac{P(\mathbf R)}{P(0)}
=\frac{3k_BT}{2N\ell^2}R^2.
$$

回复力为

$$
\mathbf f_{\rm restore}=-\nabla_{\mathbf R}F
=-\frac{3k_BT}{N\ell^2}\mathbf R.
$$

它呈Hooke形式，却主要来自构型数减少，而非每根化学键的弹性能。这里固定的是向量，不能误用包含 $4\pi R^2$ 因子的径向分布而不改变约束的解释。排除体积、链刚性、溶剂和接近完全拉直的有限伸长都会改变结果。回复力由给定端到端向量时的构型数得到。尺度方法的历史入口：[de Gennes，1991年科学说明](https://www.nobelprize.org/prizes/physics/1991/press-release/)；上述独立链模型的计算为教学重构。
