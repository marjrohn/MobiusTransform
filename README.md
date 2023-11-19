# Transformação de Möbius
Visualizando uma transformação de Möbius usando matplotlib.

## Explicação
-------------
Uma _transformaação de Möbius_ é uma função complexa $M: \mathbb{C} \longrightarrow \mathbb{C}$ na seguinte forma
$$M(z) = \frac{az + b}{cz + d}$$
onde $a, b, c, d$ são constantes complexas, e $ad - bc \neq = 0$. Esta última condição é para garantir que $M$ seja uma função _invertível_.

Segue abaixo exemplo elementares:
* Translação: $M(z) = z + p$, $p \in \mathbb{C}$,
* Dilatação: $M(z) = r z$, $r \in \mathbb{R}$ ,
* Rotação: $M(z) = e^{i \theta} z$, $\theta \in [0, 2\pi)$,
* Inversão: $M(z) = \dfrac{1}{z}$.

## Como usar
--------------
Clone este repositorio e instale os requerimentos.
```console
$ git clone ...
$ python3 -m venv .venv/
$ source .venv/bin/activate
$ pip install --requeriments MobiusTransform/requeriments.txt
```

Além disso é necessario ter FFmpeg instalado.

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

