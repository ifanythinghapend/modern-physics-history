# 推导札记：为什么“光是电磁波”是一项可计算的统一？

这里使用现代SI记号重构论证。设区域内没有电荷、电流，介质是真空。Maxwell方程给出

$$
\nabla\cdot\mathbf E=0,\qquad
\nabla\times\mathbf E=-\partial_t\mathbf B,\qquad
\nabla\times\mathbf B=\mu_0\varepsilon_0\partial_t\mathbf E.
$$

对第二式再取旋度，并交换空间、时间微分：

$$
\nabla\times(\nabla\times\mathbf E)
=-\partial_t(\nabla\times\mathbf B)
=-\mu_0\varepsilon_0\partial_t^2\mathbf E.
$$

向量恒等式
$\nabla\times(\nabla\times\mathbf E)=\nabla(\nabla\cdot\mathbf E)-\nabla^2\mathbf E$
把左边化为 $-\nabla^2\mathbf E$，因而

$$
\partial_t^2\mathbf E=c^2\nabla^2\mathbf E,\qquad
c=\frac1{\sqrt{\mu_0\varepsilon_0}}.
$$

磁场满足同样的波动方程。对平面波，散度条件还要求波矢与电场垂直，旋度方程固定电场、磁场和传播方向的关系。由电学、磁学量得到的传播速度和横波结构，可以直接与光学实验比较。现代演算参见[《费曼物理学讲义》II，第20章](https://www.feynmanlectures.caltech.edu/II_20.html)；历史论证参见本节Maxwell原文。
