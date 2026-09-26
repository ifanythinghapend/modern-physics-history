<a id="chapter-19"></a>

# 19. 数学、计算和仪器：它们如何改变“什么问题值得问”？

一个结果可以由实验测量、严格证明或受控的近似计算得到，这些工作所回答的问题并不完全相同。仪器和计算方法的进步，还会改变哪些问题能够进入研究。

<a id="q-19-1"></a>

## 19.1 物理理论预测成功，是否就意味着它的数学对象已经定义清楚？

量子力学催生了谱理论、算符代数及表示论在物理中的广泛应用。Wigner用对称群的表示组织粒子状态；von Neumann系统化算符框架。量子场论又遇到算符值分布、乘积发散和无限自由度等新困难，Wightman、Haag—Kastler、Osterwalder—Schrader、Glimm—Jaffe等人的不同路线，试图明确理论成立的数学条件。

这里要问的是：这个四维量子理论作为数学对象是否存在？真空如何定义？能谱是否有正的质量隙？哪些从形式计算中得到的性质可以严格证明？

四维量子Yang—Mills存在性与质量隙问题，正体现这种距离。Clay研究所的正式问题说明仍将其作为开放难题。[Yang—Mills与质量隙](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)。这不否定规范理论的实验成就，而是指出预测实践与完整数学构造承担不同任务。

<a id="q-19-2"></a>

## 19.2 解出一个方程，与理解一类物理过程，有什么区别？

数学物理还关心解的存在、唯一、稳定、散射、奇点与尺度极限。对波动方程，知道一个平面波解远不够；要研究一般初态如何传播、能量向哪里走、非线性是否造成聚焦或衰减。

相对论中，Choquet-Bruhat关于爱因斯坦方程初值问题的工作，首先回答适当初始数据能否确定局部演化。Christodoulou与Klainerman关于Minkowski时空的全局非线性稳定性研究，以及后来的Kerr稳定性研究，则进一步追问小扰动能否在长时间内保持受控。局部存在与适定性、最大演化区域、全局稳定性，是相关但不同的问题。

统计物理中则可以问：粒子数趋于无穷时，相变是否出现？格点间距趋于零时，是否得到所声称的连续场？随机模型在缩放后是否收敛到某个普适过程？这解释了为什么PDE、概率、几何和泛函分析都能成为物理研究的入口。

初值问题的一个明确原始结果是[Choquet-Bruhat—Geroch，1969：《Global Aspects of the Cauchy Problem in General Relativity》](https://link.springer.com/article/10.1007/BF01645389)：对满足约束及正则性要求的真空初始数据，存在最大全局双曲发展，并在保持给定初始数据的等距意义下唯一。这里的“最大”并不等于测地线完备，也不排除奇点。黑洞扰动的稳定性则需另查[Giorgi—Klainerman—Szeftel，2022](https://arxiv.org/abs/2205.14808)等工作。

<a id="q-19-3"></a>

## 19.3 没有解析解，计算能给出怎样的知识？

1953年的Metropolis、Arianna Rosenbluth、Marshall Rosenbluth、Augusta Teller、Edward Teller论文，发展了具有巨大影响的统计抽样方法。它允许从高维构型空间中抽取有代表性的状态，而不必枚举所有可能。[1953年Monte Carlo原论文](https://pubs.aip.org/aip/jcp/article/21/6/1087/202680/Equation-of-State-Calculations-by-Fast-Computing)。

Wilson1974年的格点规范理论将场论放在离散时空格点上，使非微扰计算具有具体形式。[Wilson，1974：《Confinement of Quarks》](https://link.aps.org/doi/10.1103/PhysRevD.10.2445)。格点计算还必须控制有限体积、格距和统计误差，并研究连续极限。

White1992年的密度矩阵重整化群，利用量子态的重要子空间有效压缩一维强关联问题；后来与矩阵乘积态、纠缠和张量网络的联系进一步清晰。[White，1992](https://link.aps.org/doi/10.1103/PhysRevLett.69.2863)；[Schollwöck关于DMRG的综述](https://arxiv.org/abs/cond-mat/0409292)。

计算带来三种不同成就：发现意外现象，给出受误差控制的定量预测，或生成可以独立核验的证明证书。普通浮点模拟通常属于前两类；不能只因结果稳定就称为严格证明。反过来，数值研究也不能因此被视为没有理论价值——FPUT问题和现代多体物理都说明计算可以提出新的概念问题。

<a id="q-19-4"></a>

## 19.4 如果没有新的仪器，许多新理论还有机会出现吗？

新的分辨率、能量、温度和统计规模，会把原来不可问的问题变成实验对象。下面列的是工具改变问题的典型方式，而非完整仪器史：

| 工具与历史代表 | 新增的实验能力 | 由此打开的研究问题 | 贡献核验入口 |
|---|---|---|---|
| 云室；C. T. R. Wilson | 让带电粒子径迹可见 | 辐射是什么粒子？碰撞和衰变怎样发生？ | [Wilson机构资料](https://www.nobelprize.org/prizes/physics/1927/wilson/facts/) |
| 回旋加速器；Ernest Lawrence | 可控地提高带电粒子能量 | 核反应阈值、核结构、新粒子 | [Lawrence机构资料](https://www.nobelprize.org/prizes/physics/1939/lawrence/facts/) |
| 气泡室；Donald Glaser | 在液体中记录粒子径迹 | 稀有反应与粒子分类 | [Glaser机构资料](https://www.nobelprize.org/prizes/physics/1960/glaser/facts/) |
| 多丝正比室；Georges Charpak | 快速电子读出大量带电径迹 | 高事件率精密实验和大型探测器 | [Charpak机构资料](https://www.nobelprize.org/prizes/physics/1992/charpak/facts/) |
| 电子显微镜；Ernst Ruska等人 | 比可见光更细的结构分辨 | 晶格、缺陷、纳米材料与结构生物学 | [显微技术资料](https://www.nobelprize.org/prizes/physics/1986/summary/) |
| 中子散射；Clifford Shull、Bertram Brockhouse等人 | 测量结构及激发的动量、能量信息 | 原子怎样排布？声子和磁振子的色散是什么？ | [中子散射资料](https://www.nobelprize.org/prizes/physics/1994/summary/) |
| 扫描隧道显微镜；Gerd Binnig、Heinrich Rohrer | 在局域尺度探测表面电子态 | 表面结构、局域态密度、纳米操控 | [扫描隧道显微镜资料](https://www.nobelprize.org/prizes/physics/1986/summary/) |
| 核磁共振；Bloch、Purcell等人 | 读出自旋响应及局部环境 | 物质结构、动力学、医学成像 | [磁共振资料](https://www.nobelprize.org/prizes/physics/1952/summary/) |
| CCD；Willard Boyle、George Smith | 高效电子成像 | 天文弱信号与精密成像 | [光纤与CCD资料](https://www.nobelprize.org/prizes/physics/2009/summary/) |
| 光纤与低损耗传输；Charles Kao、George Hockham等人 | 长距离相干或量子光信号传输 | 光通信、量子网络与分布式测量 | [光纤与CCD资料](https://www.nobelprize.org/prizes/physics/2009/summary/) |
| 激光冷却与原子囚禁；Chu、Cohen-Tannoudji、Phillips等 | 降低并控制原子的运动能量 | 冷原子碰撞、精密谱学与量子操控 | [冷却与囚禁讲演](https://link.aps.org/doi/10.1103/RevModPhys.70.721) |

例如中子散射测到的动力学结构因子，与密度或自旋的时空关联有关。理论中的“关联函数”，由此与探测器上随动量和能量变化的计数联系起来；实际反演还需要散射模型、仪器响应和归一化。[1994年诺贝尔奖：中子散射](https://www.nobelprize.org/prizes/physics/1994/summary/)。

材料、测量和工程能力的进步，往往先于粒子发现、量子控制和宇宙学测量精度的提高。

<a id="q-19-5"></a>

## 19.5 统计物理为什么会出现在神经网络和计算中？

Hopfield1982年的模型将记忆状态与动力系统的吸引子联系起来。自旋模型、能量函数、无序和多稳态，提供了研究集体计算的一套工具。[Hopfield，1982年原论文](https://www.pnas.org/doi/10.1073/pnas.79.8.2554)。

随后Boltzmann机器等模型进一步发展概率学习。今天机器学习也被用于实验控制、事件识别、波函数表示和复杂模型的近似。

但应当分清三个方向：物理思想启发学习算法；用学习方法解决物理计算；研究学习系统自身的统计规律。它们可以交叉，却不能互相替代。预测准确也未必等于已找到机制，物理应用仍需对称性、守恒、误差与外推能力的检验。

Hopfield模型到后续概率学习的支线可对照[Ackley、Hinton、Sejnowski，1985：《A Learning Algorithm for Boltzmann Machines》](https://doi.org/10.1207/s15516709cog0901_7)。物理模型提供研究学习系统的结构，不意味着今天所有网络都服从同一个平衡自旋模型。

<a id="q-19-6"></a>

## 19.6 为什么二十世纪的物理越来越依赖大型合作？

高能加速器、航天观测、引力波探测和大规模数据分析，要求长期基础设施、专门工程与稳定资金。大学、工业实验室和国家实验室承担不同角色。战争与冷战时期的投入、人员迁移和科研组织方式，也改变了哪些问题能被持续研究。

一个方向能够长期发展，既有科学上的原因，也有仪器、人才培养和协作条件的支持。Bose、Saha、Chandrasekhar，Yukawa、Tomonaga、Kubo，以及Yang、Lee、Wu等人的工作，也说明现代物理的思想网络始终跨越国家，不能简化成少数欧美机构的单线历史。

David Kaiser的《Quantum Legacies》特别适合补充这一层：科学家的训练、机构规模、教学与政治环境，如何与量子物理的扩展相互作用。[MIT对该书研究主题的介绍](https://news.mit.edu/2020/quantum-legacies-book-kaiser-physics-0429)。

理论、计算和实验方法常在分支之间流动。按方法重新整理这些联系，可以补充按研究对象划分的学科目录。
