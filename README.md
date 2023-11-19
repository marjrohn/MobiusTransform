# Transformação de Möbius
Visualizando uma transformação de Möbius usando matplotlib.

## Explicação
-------------
Uma _transformaação de Möbius_ é uma função complexa $M: \mathbb{C} \longrightarrow \mathbb{C}$ na seguinte forma
$$M(z) = \dfrac{az + b}{cz + d}$$
onde $a, b, c, d$ são constantes complexas, e $ad - bc \neq 0$. Esta última condição é para garantir que $M$ seja uma função _invertível_.

Segue abaixo exemplo elementares:
* Translação: $M(z) = z + b$, $b \in \mathbb{C}$
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/c2faa3c9-78f0-4c2c-a6b5-0fbeb360afc0" width=600px/><img/>

* Dilatação: $M(z) = \rho z$, $\rho \in \mathbb{R}$
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/2a24d5ca-b484-4ef7-af1e-62246fa7144c" width=600px/><img/>

* Rotação: $M(z) = e^{i \theta} z$, $\theta \in [0, 2\pi)$
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/5e08c148-5dbc-4c1d-abd6-024d5dc76605" width=600px/><img/>

* Inversão: $M(z) = \dfrac{1}{z}$.
<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/83ec26b4-a2de-4083-9cc6-64abbdd833d9" width=600px/><video/>

### Pontos Fixos
Os pontos fixos de uma transformação é obtido resolvendo a seguinte equação
$$M(z) = \dfrac{az + b}{cz + d} = z,$$
que resulta em
$$cz^2 + (d - a) z - b = 0.$$
Que dá as seguintes soluções quando $M(z)$ está _normalizada_, isto é, quando $ad - bc = 1$,
```math
  \begin{matrix}
  \displaystyle p = \dfrac{(a - d) + \sqrt{(a + d)^2 + 4}}{2c}, \\ \ \\
  \displaystyle q = \dfrac{(a - d) - \sqrt{(a + d)^2 + 4}}{2c}.
  \end{matrix}
```

Portanto uma transformação de Möbius tem no máximo dois pontos fixos. E possui um único ponto fixo quando $a - d = \pm 2$. 
Uma transformação que tem um único ponto fixo é classificada como _parabólica_.

### Classificação de $M(z)$ para dois pontos fixos.
Para isso vamos considerar duas funções auxiliares, a primeira é
$$F(z) = \dfrac{z - p}{z - q}.$$
Ela mapeia os pontos fixos p, q para $0$ e $\infty$ respectivamente. Uma transformação que tem $0$ e $\infty$ como ponto fixo é essencialmente uma dilação ou/e rotação, e daí vem a segunda função
$$N(z) = m z.$$
A transformação $M(z)$ pode ser decomposta da seguinte forma
$$M(z) = \big(F^{-1} \circ N \circ F \big) (z).$$

<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/b0984350-e4a7-47d7-82d1-ca21b940f59e" width=800px/><video/>

A ideia para visualizar $M(z)$ geometricamente é aplciar $N(z)$ no plano polar e mapear o resultado com $F^{-1}(z)$. 

É com o número $m$, no qual será chamado de _multiplicador de_ $M(z)$, que iremos classificar a transformação $M(z)$:

* **Elíptica**: quando $N(z)$ é puramente uma rotação, isto é, quando $m = e^{i \theta}$, $\theta \in \mathbb{R}$.
* **Hiperbólica**: quando $N(z)$ é puramente uma dilatação/contração, isto é, quando $m = \rho$, $\rho \in \mathbb{R}$.
* **Loxodromica**: quando $N(z)$ é uma rotação composta com uma dilatação/contração, isto é, quando $m = \rho e^{i \theta}$.

## Como usar
--------------
Clone este repositorio e instale os requerimentos em um ambiente virtual.

```console
git clone https://github.com/marjrohn/MobiusTransform.git && \
python3 -m venv .venv/ && \
source .venv/bin/activate && \
python3 -m pip install --requirement MobiusTransform/requirements.txt
```

Além disso é necessario ter [FFmpeg](https://www.ffmpeg.org/download.html) instalado para criação de videos.

### Exemplos
#### Transformação Elliptica

```py
from MobiusTransform import Elliptic

Elliptic(-1, 1).create_video('elliptic.mov')
```

-- VIDEO ELLIPTIC --

#### Transformação Hiperbolica
```py
from MobiusTransform import Hyperbolic

Hyperbolic(-1, 1).create_video('elliptic.mov')
```

-- VIDEO HYPERBOLIC

#### Transformação Loxodromica
```py
from MobiusTransform import Elliptic

Loxodromic(-1, 1).create_video('elliptic.mov')
```

-- VIDEO LOXODROMIC --

#### Transformação Parabolica
```py
from MobiusTransform import Elliptic

Parabolic(-1, 1).create_video('elliptic.mov')
```

-- VIDEO PARABOLIC --

###Outros Detalhes

