# 推导札记：Dirac为什么会走到矩阵，而不只是另一条微分方程？

对自由粒子，要求相对论色散关系
$E^2=c^2\mathbf p^2+m^2c^4$。
进一步要求演化方程对时间和空间微分都取一阶，并取与位置、动量无关的系数。为同时满足自伴性与色散关系，允许系数成为Hermitian矩阵，试写

$$
H=c\sum_{i=1}^3\alpha_i p_i+\beta mc^2.
$$

将它平方：

$$
\begin{aligned}
H^2={}&c^2\sum_i\alpha_i^2p_i^2\\
&+c^2\sum_{i<j}(\alpha_i\alpha_j+\alpha_j\alpha_i)p_ip_j\\
&+mc^3\sum_i(\alpha_i\beta+\beta\alpha_i)p_i
+\beta^2m^2c^4.
\end{aligned}
$$

要对任意动量都等于所需色散关系，必须有

$$
\{\alpha_i,\alpha_j\}=2\delta_{ij}I,\qquad
\{\alpha_i,\beta\}=0,\qquad \beta^2=I.
$$

普通数不可能满足这组要求：若 $\alpha_i^2=\beta^2=1$，它们又作为数彼此交换，就不能同时反对易。矩阵却可以；四分量旋量提供了三维空间中熟悉的实现。代入 $\mathbf p=-i\hbar\nabla$，便得到一阶的Dirac演化方程。

这些代数条件要求引入矩阵。至于自旋、正负能量解和反粒子，需要进一步研究方程的解及其场论表述。历史与原始结构：[Dirac，1928](https://royalsocietypublishing.org/rspa/article/117/778/610/2242/The-quantum-theory-of-the-electron)；本段采用现代记号。
