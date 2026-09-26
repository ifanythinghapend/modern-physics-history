# 推导札记：能量元怎样改变整个辐射谱？

**要算什么，以及在什么条件下计算**

记 $u_\nu(T)d\nu$ 为单位体积内、频率在 $\nu$ 到 $\nu+d\nu$ 之间的**热辐射能量**。它是按频率定义的能量密度谱，不是从表面射出的功率。以下使用普通频率 $\nu$，角频率是 $\omega=2\pi\nu$；$h$ 为普朗克常数，$k_B$ 为玻尔兹曼常数，$c$ 为真空光速。

模型是一只足够大的三维真空腔，辐射通过与腔壁交换能量达到温度 $T>0$ 的热平衡。腔内场取理想自由电磁场，各个正常模式彼此独立；腔壁的吸收与发射用于建立平衡，并未因此被否认。模式计数取大体积的连续近似，不讨论有限腔体的精细谱线或介质改变的色散关系。

每个模式用量子谐振子描述。这是现代量子统计的教学重构，不能写成普朗克在1900年已经采用了完整的量子场与光子语言。现代模型及模式数可核对[Fitzpatrick讲义§8.10](https://farside.ph.utexas.edu/teaching/sm1/statmech.pdf)；历史路线在本札记后半部分另行说明。

**第一步：一个模式的平均热能**

对固定的 $\nu>0$，先把能量零点选在基态，热激发能量为

$$
E_n=nh\nu,\qquad n=0,1,2,\ldots,\qquad
\beta=\frac{1}{k_BT}.
$$

令 $r=e^{-\beta h\nu}$，则 $0<r<1$。正则分布给出 $p_n=r^n/Z_\nu$，其中

$$
Z_\nu=1+r+r^2+\cdots.
$$

将这个级数乘以 $r$ 后相减，得到 $(1-r)Z_\nu=1$，所以

$$
Z_\nu=\frac{1}{1-r}.
$$

平均激发数需要的不是这一个级数本身，而是带有权重 $n$ 的级数。在 $0<r<1$ 内可逐项求导：

$$
\frac{d}{dr}\sum_{n=0}^{\infty}r^n
=\sum_{n=1}^{\infty}nr^{n-1}
=\frac{1}{(1-r)^2}.
$$

再乘以 $r$，并用 $Z_\nu$ 归一化：

$$
\begin{aligned}
\langle n\rangle
&=\frac{\sum_{n=0}^{\infty}nr^n}{\sum_{n=0}^{\infty}r^n}
=\frac{r/(1-r)^2}{1/(1-r)}\\
&=\frac{r}{1-r}
=\frac{1}{e^{\beta h\nu}-1}.
\end{aligned}
$$

于是每模式的平均热能为

$$
\langle E\rangle_\nu
=h\nu\langle n\rangle
=\frac{h\nu}{e^{h\nu/(k_BT)}-1}.
$$

也可以用配分函数复核符号与归一化：

$$
\begin{aligned}
-\frac{\partial\log Z_\nu}{\partial\beta}
&=\frac{\partial}{\partial\beta}
\log(1-e^{-\beta h\nu})\\
&=\frac{h\nu e^{-\beta h\nu}}{1-e^{-\beta h\nu}}
=\langle E\rangle_\nu.
\end{aligned}
$$

这不是说一个模式只容许一个能量元。任意非负整数 $n$ 都允许；量子化改变的是相邻能级的间距，从而改变它们在热平衡中的权重。

**第二步：同一频率附近有多少模式？**

为计算大体积下的模式密度，暂用边长 $L$、体积 $V=L^3$ 的周期性盒子。允许的波矢分量为 $k_i=2\pi m_i/L$，其中 $m_i$ 是整数。因此，每个波矢点在 $\boldsymbol{k}$ 空间占据体积 $(2\pi/L)^3$。

半径 $k$、厚度 $dk$ 的球壳体积为 $4\pi k^2dk$。每个非零波矢有两个横向偏振，故该球壳内的模式数为

$$
dN=2\frac{V}{(2\pi)^3}\,4\pi k^2dk.
$$

这里已经数遍所有传播方向，不能再额外乘一次“正反方向”的因子。除以实际空间体积 $V$，并使用 $k=2\pi\nu/c$、$dk=(2\pi/c)d\nu$：

$$
\begin{aligned}
g(\nu)d\nu
&=\frac{dN}{V}
=\frac{k^2}{\pi^2}dk\\
&=\frac{1}{\pi^2}
\left(\frac{2\pi\nu}{c}\right)^2
\frac{2\pi}{c}d\nu
=\frac{8\pi\nu^2}{c^3}d\nu.
\end{aligned}
$$

周期性边界是取得大体积主导项的计数方法，并不把真实吸收腔壁改成了周期性材料。对于尺寸与波长可比的腔体，应返回实际边界条件求离散模式。上述计数可对照[Fitzpatrick，式(8.70)—(8.72)](https://farside.ph.utexas.edu/teaching/sm1/statmech.pdf)。

**第三步：把模式数与热平均相乘**

单位体积的谱等于“每单位体积、每单位频率的模式数”乘“每模式平均热能”：

$$
u_\nu(T)=g(\nu)\langle E\rangle_\nu
=\frac{8\pi h\nu^3}{c^3}
\frac{1}{e^{h\nu/(k_BT)}-1}.
$$

$u_\nu$ 的单位为 $\mathrm{J\,m^{-3}\,Hz^{-1}}$，乘上 $d\nu$ 才是能量密度；不要把它与按波长定义的 $u_\lambda$ 直接等同。变量替换必须满足 $u_\lambda=u_\nu|d\nu/d\lambda|$。

令 $x=h\nu/(k_BT)$。两个极限解释了公式的物理内容：

$$
x\ll1:\quad e^x-1=x+O(x^2),\qquad
\langle E\rangle_\nu\simeq k_BT,\qquad
u_\nu\simeq\frac{8\pi k_BT\nu^2}{c^3};
$$

$$
x\gg1:\quad
\langle E\rangle_\nu\simeq h\nu e^{-x},\qquad
u_\nu\simeq\frac{8\pi h\nu^3}{c^3}e^{-x}.
$$

低频恢复瑞利—金斯形式；高频则因激发一个能量元的代价远大于 $k_BT$ 而被指数压低。改变的是热平均，模式密度的几何计数并未改变。这一高频抑制使总热能密度的积分收敛。结果与[普朗克1901年论文式(12)](https://de.wikisource.org/wiki/Ueber_das_Gesetz_der_Energieverteilung_im_Normalspectrum)一致；现代极限计算可核对[Fitzpatrick，式(8.79)—(8.83)](https://farside.ph.utexas.edu/teaching/sm1/statmech.pdf)。

**零点能：说明计算对象，而不是声称它很小**

完整谐振子能级为 $E_n^{\mathrm{full}}=h\nu(n+1/2)$。保留它时，配分函数与平均能量分别为

$$
Z_\nu^{\mathrm{full}}
=\frac{e^{-\beta h\nu/2}}{1-e^{-\beta h\nu}},
\qquad
\langle E^{\mathrm{full}}\rangle_\nu
=\frac{h\nu}{2}+\frac{h\nu}{e^{\beta h\nu}-1}.
$$

固定频率下，所有能级同时平移 $h\nu/2$，这个共同因子会在概率的归一化中约去。因此

$$
\langle E^{\mathrm{full}}\rangle_{\nu,T}
-\langle E^{\mathrm{full}}\rangle_{\nu,0}
=\frac{h\nu}{e^{h\nu/(k_BT)}-1}.
$$

本札记计算的是相对于同一基态的热激发能。这里并没有要求 $h\nu/2$ 很小，也没有证明真空能在所有问题中都可以删去。完整谐振子公式及两项的区分见[Kardar讲义第121页，式VI.11—VI.12](https://ocw.mit.edu/courses/8-333-statistical-mechanics-i-statistical-mechanics-of-particles-fall-2013/368b2180e6efa1417ab336d79b2df6db_MIT8_333F13_Lec20.pdf)。

**回到原论文：计数怎样通过熵决定温度？**

以下用现代记号整理原论文的一条论证路线，不逐字复现发现过程。1901年论文§3—§5先把总能量按能量元分配，§6—§10再借助位移定律确定能量元的频率依赖。设 $N$ 个可区分的同频率谐振子，共有 $P$ 个相同的能量元，每个大小为 $\epsilon$，则总能量为 $U_N=P\epsilon$。

一种分配由非负整数 $n_1,\ldots,n_N$ 指定，并满足 $n_1+\cdots+n_N=P$。把 $P$ 个标记用 $N-1$ 个分隔符分成 $N$ 组，得到分配数

$$
\Omega(N,P)=\binom{P+N-1}{P}
=\frac{(P+N-1)!}{P!\,(N-1)!}.
$$

组合数只回答“有多少种分配”。还需引入这些分配等权的统计假设，才能用 $S_N=k_B\log\Omega$ 计算熵。普朗克在§4明确提出了这一假设；它并不是由排列组合本身证明的物理定律。

取 $N,P$ 都很大、$y=P/N$ 固定，用 $\log m!=m\log m-m+O(\log m)$，保留熵中随系统大小增长的主导项：

$$
\begin{aligned}
\frac{S_N}{k_B}
&\simeq (N+P)\log(N+P)-N\log N-P\log P,\\
s(y):=\frac{S_N}{N}
&\simeq k_B\big[(1+y)\log(1+y)-y\log y\big].
\end{aligned}
$$

其中每谐振子的平均能量为 $\bar E=\epsilon y$。固定频率及 $N$，热力学关系给出

$$
\begin{aligned}
\frac1T
=\frac{\partial S_N}{\partial U_N}
=\frac{ds}{d\bar E}
&=\frac{k_B}{\epsilon}
\big[\log(1+y)+1-\log y-1\big]\\
&=\frac{k_B}{\epsilon}\log\frac{1+y}{y}.
\end{aligned}
$$

因而 $e^{\epsilon/(k_BT)}=1+1/y$，解得

$$
y=\frac{1}{e^{\epsilon/(k_BT)}-1},\qquad
\bar E=\frac{\epsilon}{e^{\epsilon/(k_BT)}-1}.
$$

以上微分采用大系统极限得到的熵主导项，有限 $N,P$ 的精确组合熵并不等同于这一光滑函数。原论文再用位移定律要求单个谐振子的熵只通过 $\bar E/\nu$ 依赖能量与频率；与上式的 $\bar E/\epsilon$ 结构比较，得到 $\epsilon=h\nu$。配合谐振子平均能量与辐射能量密度的关系，便得到同一辐射谱。[1901年原文§3—§10、式(6)、(8)、(11)—(12)](https://de.wikisource.org/wiki/Ueber_das_Gesetz_der_Energieverteilung_im_Normalspectrum)；[1900年报告英译，PDF第3—5页](https://commons.princeton.edu/josephhenry/wp-content/uploads/sites/71/2021/01/Planck-1900-Distribution-Law.pdf)。

这条历史路线把实验约束、热力学关系和统计假设接在一起。前面的现代推导则从量子能级与正则分布出发。两者的公式可以相互核对，概念背景与论证地位仍应分别说明。
