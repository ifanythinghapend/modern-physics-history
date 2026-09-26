# 推导札记：Cole—Hopf变换与白噪声极限

先把噪声平滑化，让下列微分按普通微积分合法。取一维

$$
\partial_t h=\nu h_{xx}+\frac{\lambda}{2}h_x^2+\eta,
\qquad
Z=e^{ah},\quad a=\frac{\lambda}{2\nu},\quad \nu>0,\ \lambda\ne0.
$$

链式法则逐项给出

$$
Z_t=aZh_t,\qquad
Z_{xx}=aZh_{xx}+a^2Zh_x^2.
$$

另一方面，

$$
Z_t=a\nu Zh_{xx}+\frac{a\lambda}{2}Zh_x^2+aZ\eta.
$$

由于 $\nu a^2=a\lambda/2$，非线性梯度项恰好合并进扩散项：

$$
\partial_tZ=\nu Z_{xx}+a\eta Z.
$$

这个方程对 $Z$ 是线性的，随机性以乘性项出现。于是增长高度与随机热方程发生联系：对数可以把乘性涨落变为梯度非线性。

但是空间—时间白噪声不是光滑函数，不能把刚才的链式法则原封不动照抄。一个具体检查是：对空间平滑、时间仍为白噪声的Itô方程

$$
dZ=\nu Z_{xx}\,dt+aZ\,dW_\varepsilon,\qquad
d[W_\varepsilon(x)]_t=C_\varepsilon(0)\,dt,
$$

取严格正的初值，并在 $Z>0$ 的情形令 $h=a^{-1}\log Z$，Itô二阶项产生

$$
dh=\left(\nu h_{xx}+\frac{\lambda}{2}h_x^2
-\frac{\lambda}{4\nu}C_\varepsilon(0)\right)dt+dW_\varepsilon.
$$

随着平滑尺度趋于零，$C_\varepsilon(0)$ 发散，提示必须给非线性乘积与减去的常数共同规定意义。具体常数还依赖正则化与归一化；这段算式展示其来源，不替代收敛证明。原始模型见[KPZ，1986](https://link.aps.org/doi/10.1103/PhysRevLett.56.889)，严格构造见[Hairer，2013](https://annals.math.princeton.edu/2013/178-2/p04)。

这些方法也用于链、膜、细胞和群体运动。在那里，随机性还要与形状变化及持续耗能一同考虑。
