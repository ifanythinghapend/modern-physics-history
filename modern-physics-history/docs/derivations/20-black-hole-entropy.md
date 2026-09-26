# 推导札记：接受Hawking温度以后，面积熵怎样接上热力学？

限定为无电荷、不旋转的Schwarzschild黑洞，并使用半经典温度
$T_H=\hbar c^3/(8\pi GMk_B)$。
第一定律在这条单参数平衡态族上简化为

$$
dE=T_H\,dS,\qquad E=Mc^2.
$$

所以

$$
dS=\frac{c^2\,dM}{T_H}
=\frac{8\pi Gk_B}{\hbar c}M\,dM.
$$

积分：

$$
S(M)=\frac{4\pi Gk_B}{\hbar c}M^2+S_0.
$$

又因为 $r_s=2GM/c^2$、$A=4\pi r_s^2=16\pi G^2M^2/c^4$，

$$
S=\frac{k_Bc^3A}{4G\hbar}+S_0.
$$

通常所写的Bekenstein—Hawking面积项即第一项；这段热力学积分自身不能确定质量无关的加性常数。温度随质量反比变化，使熵按面积而非体积增长。

这一积分从Hawking温度得到面积熵；辐射的推导与微观态计数仍是另外的问题。带电、旋转情形的第一定律还包含其他功项。来源：[Bekenstein，1973](https://link.aps.org/doi/10.1103/PhysRevD.7.2333)、[Hawking，1975](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-43/issue-3/Particle-creation-by-black-holes/cmp/1103899181.full)。
