# 推导札记：场方程中的 $8\pi G/c^4$ 从哪里来？

这段计算是在已经选定Einstein张量以后，用牛顿极限固定耦合常数；它不是从几个类比就唯一推导整个引力理论。取度规号差 $(-,+,+,+)$、$x^0=ct$，暂设 $\Lambda=0$，写

$$
G_{\mu\nu}=\kappa T_{\mu\nu}.
$$

四维缩并给出 $-R=\kappa T$，故

$$
R_{\mu\nu}=\kappa\left(T_{\mu\nu}-\frac12g_{\mu\nu}T\right).
$$

对弱、静态引力场中的非相对论物质，压强相对于静质量能量密度可忽略：

$$
g_{00}\simeq-\left(1+\frac{2\Phi}{c^2}\right),\qquad
T_{00}\simeq\rho c^2,\qquad T\simeq-\rho c^2.
$$

在相应的曲率符号约定下，线性化的 $00$ 分量是 $R_{00}\simeq\nabla^2\Phi/c^2$。于是

$$
\frac{\nabla^2\Phi}{c^2}
=\frac{\kappa}{2}\rho c^2.
$$

与 $\nabla^2\Phi=4\pi G\rho$ 比较，得到 $\kappa=8\pi G/c^4$。这里的因子2来自迹反演后的物质项，不能把 $T_{00}$ 单独塞进 $R_{00}=\kappa T_{00}$。这一系数使场方程在牛顿极限下与已知的引力测量相符。现代技术来源：[Carroll《Lecture Notes on General Relativity》，第4节“Gravitation”](https://arxiv.org/abs/gr-qc/9712019)。
