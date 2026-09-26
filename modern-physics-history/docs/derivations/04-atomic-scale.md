# 推导札记：原子为什么具有一个有限的量子尺度？

原子稳定性可以进一步表述为基态能量的下界。取非相对论氢原子的相对坐标，忽略精细结构和辐射修正：

$$
H=-\frac{\hbar^2}{2\mu}\nabla^2-\frac{\kappa}{r},
\qquad
\kappa=\frac{e^2}{4\pi\varepsilon_0},
\qquad
a_0=\frac{\hbar^2}{\mu\kappa},
$$

其中 $\mu$ 是电子与质子的约化质量。先对归一化、足够光滑且边界项消失的 $\psi$ 计算，再以二次型的稠密逼近延伸到相应有限能量态。利用 $\nabla\cdot\widehat{\mathbf r}=2/r$，

$$
\begin{aligned}
\int\left|\nabla\psi+\frac{\widehat{\mathbf r}}{a_0}\psi\right|^2d^3x
&=\int|\nabla\psi|^2d^3x+\frac1{a_0^2}
 +\frac1{a_0}\int\widehat{\mathbf r}\cdot\nabla|\psi|^2\,d^3x\\
&=\int|\nabla\psi|^2d^3x+\frac1{a_0^2}
 -\frac2{a_0}\int\frac{|\psi|^2}{r}\,d^3x.
\end{aligned}
$$

所以能量期望恰好是

$$
\langle H\rangle
=\frac{\hbar^2}{2\mu}
\int\left|\nabla\psi+\frac{\widehat{\mathbf r}}{a_0}\psi\right|^2d^3x
-\frac{\hbar^2}{2\mu a_0^2}
\ge-\frac{\mu\kappa^2}{2\hbar^2}.
$$

等号由 $\nabla\psi=-\widehat{\mathbf r}\psi/a_0$ 达到：

$$
\psi_0(r)=\frac{e^{-r/a_0}}{\sqrt{\pi a_0^3}}.
$$

这既找到有限大小的基态，也排除了在这个模型中把电子无限压向原点便能无限降低能量的可能。它体现的是微分算符的动能与奇异势能之间的竞争，没有使用经典电子轨道。这个单原子论证不自动证明任意大块物质的稳定性，后者还需要多体结构与费米统计。模型及基态可对照[《费曼物理学讲义》III，第19章](https://www.feynmanlectures.caltech.edu/III_19.html)；稳定性层次参见[Lieb，2004年综述](https://arxiv.org/abs/math-ph/0401004)。上述配方演算为本文的教学重构。
