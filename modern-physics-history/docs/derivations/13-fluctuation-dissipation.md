# 推导札记：噪声强度为什么不能随意指定？

先不预先给出涨落—耗散关系，而把随机力强度记为 $A$。在Markov、线性阻力近似下，用Itô形式写

$$
dv=-\frac{\gamma}{m}v\,dt+\frac{\sqrt{2A}}m\,dB_t.
$$

由于 $(dB_t)^2=dt$，Itô公式给出

$$
d(v^2)=2v\,dv+(dv)^2.
$$

取平均，随机积分在相应可积条件下均值为零，于是

$$
\frac d{dt}\langle v^2\rangle
=-\frac{2\gamma}{m}\langle v^2\rangle+\frac{2A}{m^2}.
$$

平稳值为 $A/(\gamma m)$。热平衡又要求经典能量均分
$\langle v^2\rangle=k_BT/m$，所以 $A=\gamma k_BT$，正好恢复本节的噪声相关强度。

若初速度已经按平衡分布准备，令 $\tau=m/\gamma$，则速度相关为
$C_v(t)=\langle v(t)v(0)\rangle=(k_BT/m)e^{-|t|/\tau}$。
位置变化是速度的时间积分，因此

$$
\begin{aligned}
\langle[x(t)-x(0)]^2\rangle
&=2\int_0^t(t-s)C_v(s)\,ds\\
&=2\frac{k_BT}{\gamma}\left[t-\tau(1-e^{-t/\tau})\right].
\end{aligned}
$$

短时展开得到 $(k_BT/m)t^2$，是弹道行为；长时得到 $2Dt$，其中 $D=k_BT/\gamma$。于是第1章的扩散公式有了自己的时间尺度。同一热浴的平衡条件约束了摩擦、噪声和扩散的参数。1908年原文与历史背景见[Langevin论文的Lemons—Gythiel英译](https://pubs.aip.org/aapt/ajp/article/65/11/1079/1054916/Paul-Langevin-s-1908-paper-On-the-Theory-of)；上述Itô记号属于现代重构。
