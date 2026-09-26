# 推导札记：为什么四维对 $\phi^4$ 理论特别？

下面只做高斯固定点附近的尺度计数。把自由能除以 $k_BT$，写成无量纲泛函

$$
\mathcal S[\phi]=\int d^dx
\left[\frac12|\nabla\phi|^2+\frac r2\phi^2+\frac u{4!}\phi^4\right].
$$

放大观察尺度：$x=bx'$，$b>1$。为了让梯度项系数保持不变，选择

$$
\phi(x)=b^{-(d-2)/2}\phi'(x').
$$

因为 $d^dx=b^dd^dx'$，且 $\nabla=b^{-1}\nabla'$，梯度项总因子是
$b^d b^{-2}b^{-(d-2)}=1$。另外两项分别变为

$$
r'=b^{d-(d-2)}r=b^2r,\qquad
u'=b^{d-2(d-2)}u=b^{4-d}u.
$$

所以二次项是相关方向；四次相互作用在 $d<4$ 时随粗尺度放大，在 $d>4$ 时按这一线性尺度判断衰减，在 $d=4$ 时为边缘项，需要继续计算。

尺度计数表明，四维以下的相互作用项会在粗粒化下增长，高斯固定点因而可能不稳定。它尚未积分掉短波模式，也没有算出相互作用固定点和真实临界指数；完整RG还会生成耦合的非线性流动。即使在四维以上，也须注意危险无关变量等细节。原始路线见[Kadanoff，1966](https://link.aps.org/doi/10.1103/PhysicsPhysiqueFizika.2.263)、[Wilson，1971](https://link.aps.org/doi/10.1103/PhysRevB.4.3174)；现代固定点与扰动分类也可对照[Shankar的RG综述](https://arxiv.org/abs/cond-mat/9307009)。
