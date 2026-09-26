# 推导札记：缓慢绕一圈，量子态为什么可能没有“原样回来”？

设 $H(R)|n(R)\rangle=E_n(R)|n(R)\rangle$，沿参数路径始终有隔离的非简并本征态，并满足所需绝热条件。在绝热近似下写

$$
|\psi(t)\rangle=
\exp\left[-\frac{i}{\hbar}\int_0^tE_n(R(s))\,ds\right]
e^{i\gamma(t)}|n(R(t))\rangle.
$$

代入Schrödinger方程，动力学相位部分抵消，再左乘 $\langle n|$：

$$
-\hbar\dot\gamma+i\hbar\langle n|\partial_t n\rangle=0,
\qquad
\dot\gamma=i\langle n|\partial_t n\rangle.
$$

于是对闭合路径 $C$，

$$
\gamma(C)=\oint_C\mathcal A(R)\cdot dR,\qquad
\mathcal A=i\langle n|\nabla_Rn\rangle.
$$

改选本征态相位 $|n\rangle\mapsto e^{i\chi(R)}|n\rangle$ 时，
$\mathcal A\mapsto\mathcal A-\nabla_R\chi$；
在单值允许的规范变换下，闭路可测相位保持不变，模 $2\pi$ 理解。

因此动力学结束时，能量和参数都回到原值，态仍可能带有路径留下的相位。沿闭路得到的相位关系可以通过干涉检验。简并情形要改用更一般的矩阵结构，发生能级交叉时也不能盲用本式。[Berry，1984](https://royalsocietypublishing.org/rspa/article/392/1802/45/15579/Quantal-phase-factors-accompanying-adiabatic)。后面的量子霍尔效应将进一步用到量子态随参数变化的几何。
