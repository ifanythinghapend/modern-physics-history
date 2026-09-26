# 推导札记：Bell争论怎样变成一个能测的数？

取CHSH设置：两侧各有两种测量选择，结果均为 $\pm1$。在局域隐藏变量描述中，给定 $\lambda$ 时可写成
$A_0(\lambda),A_1(\lambda),B_0(\lambda),B_1(\lambda)$；
每侧的结果不依赖远方的设置。随机响应可通过增添局部随机变量纳入这一表示。另要求采样分布 $\rho(\lambda)$ 与测量设置独立。

对每一个 $\lambda$ 定义

$$
C(\lambda)=A_0(B_0+B_1)+A_1(B_0-B_1).
$$

因为 $B_0,B_1\in\{-1,1\}$，$B_0+B_1$ 与 $B_0-B_1$ 必有一个为零，另一个为 $\pm2$，故 $|C(\lambda)|=2$。对同一个 $\rho(\lambda)$ 平均：

$$
|S|

=|E_{00}+E_{01}+E_{10}-E_{11}|
\le\int d\lambda\,\rho(\lambda)|C(\lambda)|=2.
$$

量子自旋单态给出 $E(\mathbf a,\mathbf b)=-\mathbf a\cdot\mathbf b$。取

$$
\mathbf a_0=\widehat{\mathbf z},\quad
\mathbf a_1=\widehat{\mathbf x},\quad
\mathbf b_0=\frac{\widehat{\mathbf z}+\widehat{\mathbf x}}{\sqrt2},
\quad
\mathbf b_1=\frac{\widehat{\mathbf z}-\widehat{\mathbf x}}{\sqrt2},
$$

四个相关依次为 $-1/\sqrt2,-1/\sqrt2,-1/\sqrt2,+1/\sqrt2$，于是 $S=-2\sqrt2$。这个设置实现了超出局域界的量子相关。

CHSH组合把上述假设转化为四组关联测量所满足的界。实验随后必须处理随机设置、分离、探测效率及统计置信度；一条形式不等式不能替代这些条件。原始来源：[Clauser、Horne、Shimony、Holt，1969](https://link.aps.org/doi/10.1103/PhysRevLett.23.880)。这里也没有得到可控的超光速通信通道。
