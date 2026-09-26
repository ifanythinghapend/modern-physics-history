# 推导札记：先从静态例子理解“涨落能告诉我们响应”

考虑经典正则系综，外场 $f$ 通过 $H_f=H_0-fB$ 耦合。设观测量 $A$ 本身不显含 $f$，则

$$
\langle A\rangle_f
=\frac{\int A(z)e^{-\beta[H_0(z)-fB(z)]}\,dz}
{\int e^{-\beta[H_0(z)-fB(z)]}\,dz}.
$$

对商求导，分子和分母都不能漏：

$$
\frac{\partial\langle A\rangle_f}{\partial f}
=\beta\langle AB\rangle_f
-\beta\langle A\rangle_f\langle B\rangle_f
=\beta\,{\rm Cov}_f(A,B).
$$

令 $A=B=M$ 为与磁场共轭的总磁矩，就得到

$$
\left.\frac{\partial\langle M\rangle_f}{\partial f}\right|_{f=0}
=\beta\,{\rm Var}_0(M).
$$

如果定义每单位体积的磁化率，还需再除以体积。这个结果解释了：平衡时总磁矩涨落越大，弱场越容易重新分配状态的权重，因而响应越大。

这是静态的经典结果。输运问题还涉及时间相关、因果响应和取极限顺序；一般量子情形还涉及非对易算符，不能把这个普通乘积公式无条件套上去。它是理解[Kubo，1957](https://journals.jps.jp/doi/10.1143/JPSJ.12.570)所研究问题的入口；正则系综本身见[Gibbs，1902](https://www.gutenberg.org/ebooks/50992)。
