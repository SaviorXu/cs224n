$$
P(O=o|C=c)=\frac{exp(\boldsymbol{u}_0^T\boldsymbol{v}_c)}{\sum_{w\in{Vocab}}exp(\boldsymbol{u}_w^T\boldsymbol{v}_c)}其中v_c表示中心向量，U表示中心向量的上下文向量组成的矩阵
$$


$$
J_{naive-softmax}(v_c,o,U)=-logP(O=o|C=c)
$$
a.
$$
-\sum_{w\in{Vocab}}{y_wlog(\hat{y}_w)}=-log(\hat{y}_o)
$$
其中，
$$
y_w=\begin{cases}1,w=o\\0,w\neq{o} \end{cases}
$$
b.
$$
J_{naive\_softmax}=-log\frac{exp(\boldsymbol{u}_o^T\boldsymbol{v}_c)}{\sum_{w\in{Vocab}}exp(\boldsymbol{u}_w^T\boldsymbol{v}_c)}=-\boldsymbol{u}_o^T\boldsymbol{v}_c+log\sum_{w\in{Vocab}}exp(\boldsymbol{u}_w^T\boldsymbol{v}_c)
$$

$$
\frac{\partial{J}}{\partial{\boldsymbol{v}_c}}=-\boldsymbol{u_o}+\sum_{w\in{Vocab}}\frac{exp(\boldsymbol{u}_w^T\boldsymbol{v_c})}{\sum_{i\in{Vocab}}exp(\boldsymbol{u}_i^T\boldsymbol{v}_c)}\boldsymbol{u}_w=(\hat{\boldsymbol{y}}-\boldsymbol{y})U^T
$$

c.
$$
w=o时，\frac{\partial{J}}{\partial{\boldsymbol{u}_o}}=-\boldsymbol{v}_c+\frac{exp(\boldsymbol{u}_o^T\boldsymbol{v}_c)}{\sum_{w\in{Vocab}}exp(\boldsymbol{u}_w^T\boldsymbol{v}_c)}\boldsymbol{v}_c=(P(o|c)-1)\boldsymbol{v}_c
$$

$$
w\neq{o}时，\frac{\partial{J}}{\partial{\boldsymbol{u}_w}}=\frac{exp(\boldsymbol{u}_w^T\boldsymbol{v}_c)}{\sum_{i\in{Vocab}}exp(\boldsymbol{u}_i^T\boldsymbol{v}_c)}\boldsymbol{v}_c=P(w|c)\boldsymbol{v}_c
$$

d.
$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

其中$\sigma(-x)+\sigma(x)=1$,$\sigma^{'}(x)=\sigma{(x)}[1-\sigma(x)]$

e.
$$
J_{neg-sample}(\boldsymbol{v}_c,o,\boldsymbol{U})=-log(\sigma(\boldsymbol{u}_o^{T}\boldsymbol{v}_c))-\sum_{k=1}^{K}log(\sigma(-\boldsymbol{u}_k^T\boldsymbol{v}_c))=-log(\sigma(\boldsymbol{u}_o^{T}\boldsymbol{v}_c))-\sum_{k=1}^{K}log[1-\sigma(\boldsymbol{u}_k^T\boldsymbol{v}_c)]
$$

$$
\frac{\partial J}{\partial{\boldsymbol{v}_c}}=-[1-\sigma(\boldsymbol{u}_o^T\boldsymbol{v}_c)]\boldsymbol{u}_o+\sum_{k=1}^K\sigma(\boldsymbol{u}_k^T\boldsymbol{v}_v)\boldsymbol{u}_
k
$$

$$
\frac{\partial J}{\partial \boldsymbol{u}_o}=-[1-\sigma(\boldsymbol{u}_o^T\boldsymbol{v}_c)]\boldsymbol{v}_c
$$

$$
\frac{\partial J}{\partial u_k}=\sigma(\boldsymbol{u}_k^T\boldsymbol{v}_c)\boldsymbol{v}_c
$$

f.
$$
J_{skip-gram}(\boldsymbol{v}_c,\boldsymbol{w}_{t-m},...,\boldsymbol{w}_{t+m},\boldsymbol{U})=\sum_{-m\leq j \leq m,j\neq 0}J(\boldsymbol{v}_c,w_{t+j},\boldsymbol{U})
$$

$$
\frac{\partial J_{skip-gram}(\boldsymbol{v}_c,\boldsymbol{w}_{t-m},...\boldsymbol{w}_{t+m},\boldsymbol{U})}{\partial{U}}=\sum_j{\frac{\partial{J(\boldsymbol{v}_c,\boldsymbol{w}_{t+j},\boldsymbol{U})}}{\partial{\boldsymbol{U}}}}
$$

$$
\frac{\partial J_{skip-gram}(\boldsymbol{v}_c,\boldsymbol{w}_{t-m},...\boldsymbol{w}_{t+m},\boldsymbol{U})}{\partial{v}_c}=\sum_j{\frac{\partial{J(\boldsymbol{v}_c,\boldsymbol{w}_{t+j},\boldsymbol{U})}}{\partial{\boldsymbol{v}_c}}}
$$









