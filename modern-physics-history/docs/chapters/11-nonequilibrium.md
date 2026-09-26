<a id="chapter-11"></a>

# 11. 非平衡统计物理：系统还在运动、输运和生长时，有什么普遍规律？

研究布朗运动、输运和生长过程时，往往关心轨迹的统计，而非某一条轨迹本身。噪声和耗散有什么联系？涨落能否给出响应？持续驱动又会形成怎样的结构？

<a id="q-11-1"></a>

## 11.1 摩擦让运动衰减，为什么微小颗粒又永远在抖动？

Langevin在1908年将布朗运动写成可辨认的两部分：摩擦与随机力。例如

$$
m\dot v=-\gamma v+\xi(t),\qquad
\langle\xi(t)\xi(t')\rangle=2\gamma k_BT\,\delta(t-t').
$$

这里 $\gamma>0$ 是阻力系数。热浴一方面耗散颗粒的有序运动，另一方面不断给它随机冲击。要使稳态与温度为 $T$ 的同一热浴相容，噪声强度必须与阻力按上式匹配。不匹配并不必然导致无限升温：在线性模型中，若噪声相关为 $2A\delta(t-t')$，仍可达到有限稳态，只是其有效温度为 $A/(\gamma k_B)$，未必等于指定的热浴温度。下面的推导会给出这个区别。

白噪声是时间尺度分离后的理想化。$\delta(t-t')$作为分布表达相关性，不能把 $t=t'$ 直接代入，得到一个普通“瞬时噪声方差”。可测的是有限时间窗中积分或平均后的量。

Fokker—Planck方法转而描述概率分布随时间演化。随机轨迹与概率密度方程是同一物理的两种组织方式，分别适合不同问题。这些方法也用于化学反应等随机过程；在物理中，它们首先用来研究涨落与输运。

<!-- include-derivation: derivations/13-fluctuation-dissipation.md -->
[阅读推导札记：噪声强度为什么不能随意指定？](../derivations/13-fluctuation-dissipation.md)
<!-- /include-derivation -->


<a id="q-11-2"></a>

## 11.2 不真的施加一个外场，能不能从平衡涨落预测系统的响应？

Onsager1931年研究不可逆过程的互易关系。在接近平衡时，电流、热流、扩散流可与驱动力线性联系；微观可逆性对交叉响应系数施加限制。有磁场或具有不同时间反演奇偶性的变量时，需要相应的Onsager—Casimir形式，不能总写成无条件的 $L_{ij}=L_{ji}$。[Onsager，1931](https://link.aps.org/doi/10.1103/PhysRev.37.405)。

Green、Kubo等人的线性响应理论，将输运系数与平衡态的时间关联联系起来。例如电流会自然涨落；这些涨落如何在时间上保持关联，携带系统受微弱电场驱动时如何导电的信息。[Kubo，1957](https://journals.jps.jp/doi/10.1143/JPSJ.12.570)。

这回答了一类常见困惑：为什么关联函数如此重要？因为在有明确假设的理论中，关联不仅表达“共同变化”，还能与可测的响应建立定量关系。不过，远离平衡时不能未经证明沿用同一个平衡涨落—耗散公式。

<!-- include-derivation: derivations/14-static-response.md -->
[阅读推导札记：先从静态例子理解“涨落能告诉我们响应”](../derivations/14-static-response.md)
<!-- /include-derivation -->


<a id="q-11-3"></a>

## 11.3 持续输入能量，为什么反而可能产生有序结构？

Rayleigh—Bénard对流、化学振荡、激光和反应扩散图样表明，系统偏离平衡时可以形成稳定的空间或时间结构。Prigogine及合作者发展耗散结构思想；Haken的协同学研究不同模式如何竞争和选择。

这类研究要回答：均匀状态什么时候失稳？哪一种模式首先长大？非线性怎样限制增长？噪声会触发转变，还是破坏有序？这些问题通常通过线性稳定性、振幅方程和分岔理论处理。

不能把它概括成“远离平衡就必然自组织”，也没有一个普遍适用于所有远离平衡系统的最小熵产生原则。一个新的非平衡理论，首先要说清楚驱动、耗散、守恒量和观测时间尺度。

这套从失稳到振幅方程的研究框架可查[Cross—Hohenberg，1993：《Pattern Formation Outside of Equilibrium》](https://link.aps.org/doi/10.1103/RevModPhys.65.851)。应查阅具体系统的控制参数与对称性，而不是仅凭“耗散结构”四个字解释一个图样。

<a id="q-11-4"></a>

## 11.4 微小系统偶尔逆着第二定律波动，热力学还成立吗？

对分子机器或单个胶体颗粒，每次实验做功不同，热交换也不同。Evans、Cohen、Morriss，Gallavotti与Cohen，以及Jarzynski、Crooks等人的工作，逐渐形成涨落关系和随机热力学的一组核心结果。

Jarzynski等式在适用条件下写成

$$
\left\langle e^{-\beta W}\right\rangle=e^{-\beta\Delta F},
\qquad \beta=(k_BT)^{-1}.
$$

这里系统从相应的热平衡分布准备出发，$W$取外界对系统做功的约定，$\Delta F$是初末控制参数所对应的平衡自由能差；实际驱动不必始终缓慢或保持平衡。由Jensen不等式可推出 $\langle W\rangle\ge\Delta F$。[Jarzynski，1997年论文](https://link.aps.org/doi/10.1103/PhysRevLett.78.2690)。

因此，单次涨落不等于宏观第二定律失效。新的理论补充的是整条概率分布和轨迹层面的热力学。Sekimoto、Seifert等人把功、热和熵产生组织到随机轨迹上，连接单分子拉伸、马达、化学网络等实验。[Seifert，2012年综述](https://arxiv.org/abs/1205.4176)。

<!-- include-derivation: derivations/15-jarzynski-equality.md -->
[阅读推导札记：一个非平衡过程，怎样精确给出平衡自由能差？](../derivations/15-jarzynski-equality.md)
<!-- /include-derivation -->


<a id="q-11-5"></a>

## 11.5 一条随机生长的边界，为什么会有可重复的粗糙规律？

想象沉积薄膜、燃烧前沿或液晶中的增长区域。每处生长有随机性，但长时间、大尺度的粗糙度可能服从简单标度。Edwards—Wilkinson型线性生长理论是重要前身；Kardar、Parisi、张翼成在1986年提出后来称为KPZ方程的模型：

$$
\partial_t h=\nu\nabla^2h
+\frac{\lambda}{2}|\nabla h|^2+\eta.
$$

第一项使表面趋于平滑，第二项表达局部倾斜如何影响生长，第三项代表随机输入。这些项的竞争最终产生什么大尺度统计？哪些微观细节会消失？[Kardar—Parisi—Zhang，1986](https://link.aps.org/doi/10.1103/PhysRevLett.56.889)。

在通常的 $1+1$ 维KPZ普适类中，进入渐近生长区、但尚未出现有限尺寸饱和时，高度涨落的典型尺度为 $t^{1/3}$，空间粗糙指数为 $1/2$，动态指数为 $3/2$。这与普通布朗扩散不同。Sasamoto与Spohn、Amir—Corwin—Quastel等人在2010年前后推进一维精确分布研究；Takeuchi与Sano的液晶实验则检验了标度和更细的涨落统计。[Takeuchi—Sano，2010](https://arxiv.org/abs/1001.5121)。

必须区分三件事：KPZ方程是一个随机动力学模型；KPZ普适类是共享特定尺度统计的一批系统；一般的粗糙界面不自动属于这个类。在同一KPZ普适类内，平坦、弯曲或平稳初态可以对应不同的极限分布，不能只比较指数；改变噪声相关、无序或守恒结构，还可能改变是否属于这一普适类。

<a id="q-11-6"></a>

## 11.6 一个物理上很好用的随机方程，为什么数学上甚至还没定义好？

白噪声驱动下，KPZ的高度场往往不够光滑，$|\nabla h|^2$不能按普通函数乘法随意定义。这里不是“积分技巧不熟练”，而是原来写下的表达式本身需要严格解释。

在Hairer之前，Cole—Hopf途径已能定义一维KPZ的一类解；Bertini与Giacomin1997年进一步从特定弱非对称粒子系统建立相应缩放极限。[Bertini—Giacomin，1997：《Stochastic Burgers and KPZ Equations from Particle Systems》](https://link.springer.com/article/10.1007/s002200050044)。

Hairer2013年的《Solving the KPZ Equation》发展了新的路径式解理论，使奇异非线性、近似与解对噪声的依赖获得更直接的分析框架；相关思想随后发展为正则结构理论。[Hairer，2013](https://annals.math.princeton.edu/2013/178-2/p04)。这项贡献应放在已有Cole—Hopf解与粒子系统极限工作的连续历史中理解。

于是，同一个现象可以产生三种不同但相互支持的论文：实验者检验某种界面是否具有KPZ统计；物理学家研究为什么出现这个普适类；数学家证明极限存在、解如何定义及离散模型怎样收敛。Le Doussal的[2025年KPZ发展综述](https://arxiv.org/abs/2507.08341)提供了从1986年至近年多条支线的追踪入口。

<!-- include-derivation: derivations/16-cole-hopf.md -->
[阅读推导札记：Cole—Hopf变换与白噪声极限](../derivations/16-cole-hopf.md)
<!-- /include-derivation -->

