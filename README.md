# Transformação de Möbius
Visualizando uma transformação de Möbius usando matplotlib.

## Explicação
-------------
Uma _transformaação de Möbius_ é uma função complexa $M: \mathbb{C} \longrightarrow \mathbb{C}$ na seguinte forma
$$M(z) = \dfrac{az + b}{cz + d}$$
onde $a, b, c, d$ são constantes complexas, e $ad - bc \neq 0$. Esta última condição é para garantir que $M$ seja uma função _invertível_.

Segue abaixo exemplo elementares:
* Translação: $M(z) = z + b$, $b \in \mathbb{C}$
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/c2faa3c9-78f0-4c2c-a6b5-0fbeb360afc0" width=600px />

* Dilatação: $M(z) = \rho z$, $\rho \in \mathbb{R}$
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/2a24d5ca-b484-4ef7-af1e-62246fa7144c" width=600px />

* Rotação: $M(z) = e^{i \theta} z$, $\theta \in [0, 2\pi)$
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/5e08c148-5dbc-4c1d-abd6-024d5dc76605" width=600px />

* Inversão: $M(z) = \dfrac{1}{z}$.
<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/83ec26b4-a2de-4083-9cc6-64abbdd833d9" width=600px />

### Pontos Fixos
Os pontos fixos de uma transformação é obtido resolve a seguinte equação
$$M(z) = \dfrac{az + b}{cz + d} = z,$$
que resulta na seguinte equação
$$cz^2 + (d - a) z - b = 0.$$
Que dá as seguintes soluções quando $M(z)$ está _normalizada_, isto é, quando $ad - bc = 1$,
$$\begin{matrix}
  \displaystyle p = \dfrac{(a - d) + \sqrt{(a + d)^2 + 4}}{2c}, \\ \ \\
  \displaystyle q = \dfrac{(a - d) - \sqrt{(a + d)^2 + 4}}{2c}.
\end{matrix}$$

Portanto uma transformação de Möbius tem no máximo dois pontos fixos. E possui um ponto fixo quando $a - d = \pm 2$. 
Uma transformação que tem um único ponto fixo é classificada como _parabólica_.

#### Classificação de $M(z)$ para dois pontos fixos.
Para isso vamos considerar duas funções auxiliares, a primeira é
$$F(z) = \dfrac{z - p}{z - q}.$$
Ela mapeia os pontos fixos p, q para $0$ e $\infty$ respectivamente. Uma transformação que tem $0$ e $\infty$ como ponto fixo é essencialmente uma dilação ou/e rotação, e daí vem a segunda função
$$N(z) = m z.$$


## Como usar
--------------
Clone este repositorio e instale os requerimentos.
```console
~$ git clone ... && \
python3 -m venv .venv/ && \
source .venv/bin/activate && \
pip install --requeriments MobiusTransform/requeriments.txt
```

Além disso é necessario ter ffmpeg instalado para criação de videos.

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

