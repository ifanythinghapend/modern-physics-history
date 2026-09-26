# 推导札记：不用追踪分子，也能算出扩散与阻力的关系

设稀薄悬浮颗粒在温度恒定的流体中运动，迁移率为 $\mu$：小外力 $F$ 产生平均漂移速度 $v=\mu F$。设外势 $U(x)$，粒子浓度为 $n(x)$，扩散系数 $D$ 在考虑的区域内为常数。漂移和扩散的总粒子流是

$$
j(x)=\mu F(x)n(x)-D\partial_xn(x),\qquad F=-U'.
$$

热平衡既要求没有净流，也要求稀薄粒子服从Boltzmann分布：

$$
n_{\rm eq}(x)\propto e^{-U(x)/(k_BT)},\qquad
\partial_xn_{\rm eq}=-\frac{U'}{k_BT}n_{\rm eq}.
$$

代回流量式：

$$
0=j_{\rm eq}
=\left(-\mu+\frac{D}{k_BT}\right)U'n_{\rm eq}.
$$

对可施加的非零势梯度都要成立，所以

$$
D=\mu k_BT.
$$

球形颗粒满足低雷诺数、连续流体与无滑移边界等Stokes阻力条件时，$\mu=(6\pi\eta a)^{-1}$，得到本节的Einstein关系。撤去外力后，在均匀介质中再由自由扩散方程 $\partial_t n=D\partial_x^2n$，在边界项消失且分布归一化的条件下两次分部积分：

$$
\frac{d}{dt}\langle x^2\rangle
=D\int x^2\partial_x^2n\,dx
=2D\int n\,dx=2D.
$$

以起点为原点，便得到 $\langle[x(t)-x(0)]^2\rangle=2Dt$。平衡分布和零净流条件，把扩散强度与机械响应联系起来。当系统持续主动耗能、存在记忆效应或已经进入短时弹道运动时，要重新检查假设。现代推导背景参见[《费曼物理学讲义》I，第43章“扩散”](https://www.feynmanlectures.caltech.edu/I_43.html)；历史归属及实验检验见本节所引Einstein—Perrin研究。

热、统计和电磁理论在热辐射问题上汇合，却遇到了困难：若按经典方式给电磁模式分配能量，为什么得不到正确的光谱？
