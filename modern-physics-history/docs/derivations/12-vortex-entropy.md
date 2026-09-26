# 推导札记：一个涡旋的能量与熵怎样竞争？

取二维相位场的长波能量

$$
E[\theta]=\frac{\rho_s}{2}\int|\nabla\theta|^2\,d^2x,
$$

其中 $\rho_s$ 是具有能量量纲的相位刚度。对有限圆盘中的单位涡旋，核外 $\theta$ 绕中心转一圈变化 $2\pi$，故 $|\nabla\theta|=1/r$。以 $a$ 为核尺度、$L$ 为系统尺度：

$$
E_v-E_{\rm core}
=\frac{\rho_s}{2}\int_a^L\frac1{r^2}\,2\pi r\,dr
=\pi\rho_s\log\frac La.
$$

涡旋中心大约有 $(L/a)^2$ 个可区分位置，于是位置熵估算为

$$
S_v\simeq k_B\log (L/a)^2=2k_B\log\frac La.
$$

自由能的大尺度部分因此是

$$
F_v\simeq E_{\rm core}
+(\pi\rho_s-2k_BT)\log\frac La.
$$

低温时产生自由涡旋的自由能代价随系统尺度增大；升温时位置熵能够与它竞争。因此，分析转变时需要把涡旋作为激发纳入描述。

这只是孤立涡旋的能熵估算。完整BKT转变要处理涡旋—反涡旋相互作用、边界或中性条件，以及刚度随尺度的重整化；不能把裸刚度代入就宣称得到精确转变温度。普适跳变关系使用的是长波重整化刚度。历史和技术背景见[2016年诺贝尔奖科学背景](https://www.nobelprize.org/prizes/physics/2016/advanced-information/)。
