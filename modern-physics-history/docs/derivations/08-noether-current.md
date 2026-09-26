# 推导札记：一个连续对称性怎样变成守恒量？

给定 $L(q,\dot q,t)$，先只考虑不改变时间坐标的无穷小变换
$\delta q_i=\epsilon X_i(q,t)$。
若作用量在此变换下至多改变端点项，则
$\delta L=\epsilon\,dB/dt$。
另一方面，令 $p_i=\partial L/\partial\dot q_i$，有

$$
\frac{\delta L}{\epsilon}
=\sum_i\left(\frac{\partial L}{\partial q_i}X_i
+p_i\frac{dX_i}{dt}\right).
$$

沿满足Euler—Lagrange方程的运动，
$\partial L/\partial q_i=\dot p_i$，所以

$$
\frac{dB}{dt}
=\sum_i(\dot p_iX_i+p_i\dot X_i)
=\frac d{dt}\sum_ip_iX_i.
$$

因此

$$
Q=\sum_ip_iX_i-B,\qquad \dot Q=0.
$$

例如，沿固定方向 $\mathbf a$ 平移，$\delta\mathbf q=\epsilon\mathbf a$ 且 $B=0$，得到 $\mathbf p\cdot\mathbf a$ 守恒；旋转取 $\delta\mathbf q=\epsilon\,\mathbf a\times\mathbf q$，得到 $\mathbf a\cdot(\mathbf q\times\mathbf p)$ 守恒。

守恒量的得到同时用到了作用量的连续对称性、运动方程与端点条件。局部规范变换牵涉Noether第二定理、约束及边界，不能直接把这里每一个参数照搬成独立物理守恒荷。原始来源：[Noether，1918，Tavel英译](https://arxiv.org/abs/physics/0503066)；本段只展示第一定理的一个有限维版本。
