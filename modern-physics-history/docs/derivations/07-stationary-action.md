# 推导札记：作用量为什么能把量子相位接到经典运动？

先看一维粒子，取 $S[x]=\int_{t_a}^{t_b}L(x,\dot x,t)\,dt$，扰动路径为 $x+\epsilon\eta$，固定端点，即 $\eta(t_a)=\eta(t_b)=0$。一阶变化是

$$
\delta S=\int_{t_a}^{t_b}
\left(\frac{\partial L}{\partial x}\eta+
\frac{\partial L}{\partial\dot x}\dot\eta\right)dt.
$$

对第二项分部积分，端点项消失：

$$
\delta S=\int_{t_a}^{t_b}
\left[\frac{\partial L}{\partial x}
-\frac d{dt}\frac{\partial L}{\partial\dot x}\right]\eta\,dt.
$$

若对任意这样的 $\eta$ 都有 $\delta S=0$，就得到Euler—Lagrange方程。取 $L=m\dot x^2/2-V(x)$，恢复 $m\ddot x=-V'(x)$。

现在回看量子幅中的 $e^{iS/\hbar}$。在允许驻相近似的半经典情形，作用量快速变化的邻近路径容易产生相位相消；$\delta S=0$ 的历史附近能够留下有组织的贡献。经典方程因而出现在量子幅的驻相近似中。这是驻相解释，并非对任意势、任意时间的严格经典极限定理；多个驻点、焦散和隧穿都需要额外处理。[Feynman，1948](https://link.aps.org/doi/10.1103/RevModPhys.20.367)。
