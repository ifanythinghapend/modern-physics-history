# 推导札记：一个恒星质量上限，为什么会含有 $\hbar$？

用量级估算先抓机制，不在几行里伪造精确的Chandrasekhar模型。设白矮星质量为 $M$、半径为 $R$，每个电子对应的平均物质质量为 $\mu_e m_u$。冷、完全简并电子气有

$$
N_e\simeq\frac{M}{\mu_e m_u},\qquad
n_e\sim\frac{N_e}{R^3},\qquad
p_F=\hbar(3\pi^2n_e)^{1/3}.
$$

非相对论时，简并动能量级
$U_e\sim N_ep_F^2/m_e\propto M^{5/3}/R^2$，
而引力能 $U_g\sim-GM^2/R$。在这个区间，缩小半径会使动能代价比引力吸引增长得更快。

当电子达到超相对论区间，单粒子能量转为 $pc$ 的尺度：

$$
U_e\sim N_ecp_F
\sim\frac{\hbar c}{R}
\left(\frac{M}{\mu_e m_u}\right)^{4/3}.
$$

此时两项都按 $R^{-1}$ 变化，能否支撑由它们的系数竞争决定：

$$
GM^2\sim\hbar c\left(\frac{M}{\mu_e m_u}\right)^{4/3}
\quad\Rightarrow\quad
M_{\rm scale}\sim
\frac{(\hbar c/G)^{3/2}}{(\mu_e m_u)^2}.
$$

量子统计提供压力，相对论改变其随密度增长的方式，引力决定是否能平衡。数值系数和约 $1.4M_\odot$ 的典型理想化结果，需要结合状态方程求解恒星结构，不能从这里的 $\sim$ 号直接得到。旋转、温度、组分、广义相对论与核过程还会修正适用范围。历史与理论入口：[Chandrasekhar，1983年诺贝尔讲演](https://www.nobelprize.org/prizes/physics/1983/chandrasekhar/lecture/)。
