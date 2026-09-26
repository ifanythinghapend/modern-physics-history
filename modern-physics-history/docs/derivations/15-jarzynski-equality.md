# 推导札记：一个非平衡过程，怎样精确给出平衡自由能差？

展示Jarzynski等式的一个简单适用情形：经典系统先按逆温度 $\beta$ 的正则分布准备，此后与热浴隔离，以给定协议改变哈密顿量参数 $\lambda_t$，并服从Hamilton动力学。设初末相点为 $z_0,z_\tau$：

$$
\rho_0(z_0)=\frac{e^{-\beta H(z_0,\lambda_0)}}{Z_0},\qquad
W=H(z_\tau,\lambda_\tau)-H(z_0,\lambda_0).
$$

后一式成立，因为这段过程只有外界做功，没有热交换。代入指数平均：

$$
\begin{aligned}
\langle e^{-\beta W}\rangle
&=\frac1{Z_0}\int dz_0\,e^{-\beta H(z_0,\lambda_0)}
e^{-\beta[H(z_\tau,\lambda_\tau)-H(z_0,\lambda_0)]}\\
&=\frac1{Z_0}\int dz_0\,e^{-\beta H(z_\tau,\lambda_\tau)}.
\end{aligned}
$$

对具有适当光滑性、固定相空间且全程良定义的Hamilton演化，Liouville定理给出相空间体积保持，$dz_\tau=dz_0$。因而

$$
\langle e^{-\beta W}\rangle
=\frac1{Z_0}\int dz_\tau\,e^{-\beta H(z_\tau,\lambda_\tau)}
=\frac{Z_\tau}{Z_0}=e^{-\beta\Delta F}.
$$

$Z_\tau$ 是末参数在同一 $\beta$ 下的平衡配分函数；实际末态并不要求已经达到这个平衡。再用凸性：

$$
e^{-\beta\langle W\rangle}
\le\langle e^{-\beta W}\rangle=e^{-\beta\Delta F},
\qquad
\langle W\rangle\ge\Delta F.
$$

这一等式不要求驱动缓慢，但依赖所设定的初始分布与动力学。与热浴持续接触的随机动力学也有相应结论，但需要其自己的动力学和功定义条件，不能用上面的相空间换元当作一切情形的证明。来源：[Jarzynski，1997](https://link.aps.org/doi/10.1103/PhysRevLett.78.2690)、[Seifert，2012](https://arxiv.org/abs/1205.4176)。
