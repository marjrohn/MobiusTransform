# Transformação de Möbius
Visualizando uma transformação de Möbius usando matplotlib.

## Explicação
-------------
Uma _transformação de Möbius_ é uma função complexa $M: \mathbb{C} \longrightarrow \mathbb{C}$ na seguinte forma
$$M(z) = \dfrac{az + b}{cz + d}$$
onde $a, b, c$ e $d$ são constantes complexas, e $ad - bc \neq 0$. Esta última condição é para garantir que $M$ seja uma função _invertível_.

Segue abaixo exemplo elementares:
* Translação: $M(z) = z + b$,  $b \in \mathbb{C}$
  
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/c2faa3c9-78f0-4c2c-a6b5-0fbeb360afc0" width=600px/><img/>

* Dilatação/Contração: $M(z) = \rho z$,  $\rho \in \mathbb{R}$

<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/2a24d5ca-b484-4ef7-af1e-62246fa7144c" width=600px/><img/>

* Rotação: $M(z) = e^{i \theta} z$,  $\theta \in \mathbb{R}$

<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/5e08c148-5dbc-4c1d-abd6-024d5dc76605" width=600px/><img/>

* Inversão: $M(z) = \dfrac{1}{z}$

<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/83ec26b4-a2de-4083-9cc6-64abbdd833d9" width=600px/><video/>

### Pontos Fixos
Os pontos fixos de uma transformação é obtido resolvendo a seguinte equação
$$M(z) = \dfrac{az + b}{cz + d} = z,$$
que resulta em
$$cz^2 + (d - a) z - b = 0.$$
Que dá os seguintes pontos quando $M(z)$ está _normalizada_, isto é, quando $ad - bc = 1$,
```math
  \begin{matrix}
  \displaystyle p = \dfrac{(a - d) + \sqrt{(a + d)^2 - 4}}{2c}, \\ \ \\
  \displaystyle q = \dfrac{(a - d) - \sqrt{(a + d)^2 - 4}}{2c}.
  \end{matrix}
```

Portanto uma transformação de Möbius tem no máximo dois pontos fixos. E possui um único ponto fixo quando $a + d = \pm 2$. 
Uma transformação que tem um único ponto fixo é classificada como **parabólica**.

### Classificação de $M(z)$ para dois pontos fixos.
Para isso vamos considerar duas funções auxiliares, a primeira é
$$F(z) = \dfrac{z - p}{z - q}.$$
Ela mapeia os pontos fixos $p$, $q$ para $0$ e $\infty$ respectivamente. Uma transformação que tem $0$ e $\infty$ como ponto fixo é essencialmente uma dilação e/ou rotação, e daí vem a segunda função
$$N(z) = m z.$$
A transformação $M(z)$ pode ser decomposta da seguinte forma
$$M(z) = \big(F^{-1} \circ N \circ F \big) (z).$$

<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/b0984350-e4a7-47d7-82d1-ca21b940f59e" width=800px/><video/>

A ideia para visualizar $M(z)$ geometricamente é aplicar $N(z)$ no plano polar e mapear o resultado com $F^{-1}$. 

É com o número $m$, no qual será chamado de _multiplicador de_ $M$, que iremos classificar a transformação $M(z)$:

* **Elíptica**: quando $N(z)$ é puramente uma rotação, isto é, quando $m = e^{i \theta}$, $\theta \in \mathbb{R}$.
* **Hiperbólica**: quando $N(z)$ é puramente uma dilatação/contração, isto é, quando $m = \rho$, $\rho \in \mathbb{R}$.
* **Loxodromica**: quando $N(z)$ é uma rotação composta com uma dilatação/contração, isto é, quando $m = \rho e^{i \theta}$.

Para mais detalhes, veja o Capítulo 3 da referência [[1]]($1), em especial a sessão 3.7 que é dedicada em classificar e visualizar uma Transformação de Möbius.


## Como usar
--------------
Clone este repositorio e instale os requerimentos em um ambiente virtual.

```console
git clone https://github.com/marjrohn/MobiusTransform.git && \
python3 -m venv .venv/ && \
source .venv/bin/activate && \
python3 -m pip install --requirement MobiusTransform/requirements.txt
```

Além disso é necessário ter [FFmpeg](https://www.ffmpeg.org/download.html) instalado para criação de videos.


### Exemplos
#### Transformação Elliptica

```py
from MobiusTransform import Elliptic

elliptic = Elliptic(1, -1)
elliptic.create_video('elliptic.mov')
```

<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/8a083512-7fed-4903-8e50-d66db62c7c3e" width=600px /><video />


#### Transformação Hiperbolica
```py
from MobiusTransform import Hyperbolic

hyperbolic = Hyperbolic(1, -1)
hyperbolic.create_video('hyperbolic.mov')
```

<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/8543ca9d-8c16-4fe8-ac9b-e60cd89f2cba" width=600px /><video />


#### Transformação Loxodromica
```py
from MobiusTransform import Loxodromic

loxodromic = Loxodromic(1, -1)
loxodromic.create_video('loxodromic.mov')
```

<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/9e9d4e48-8547-4882-b20d-5dcb31b429e3" width=600px /><video />

#### Transformação Parabolica
```py
from MobiusTransform import Elliptic

parabolic = Parabolic(0)
parabolic..create_video('parabolic.mov')
```
<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/ef050eb2-eabe-43b6-b4eb-ac8f177f2ec1" width=600px /><video/ >


### Alguns detalhes

### Zoom 
Aplicando zoom de 75% no centro da imagem (ponto médio entre $p$ e $q$)

```py
elliptic.set_fixed_points((1, 2), (2, -1))
elliptic.set_zoom(.75)
elliptic.create_image('elliptic_zoom_center.png')
```
<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/ebdcec15-f7f0-46d2-99af-01d17cc0c553" width=800px><img />


Aplicando zoom de 100% em torno do primeiro ponto fixo
```py
elliptic.set_zoom((1, 0))
elliptic.create_image('elliptic_zoom_0.png')
```

<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/6e957bd6-02ea-4b68-b8ea-4b7318216b01" width=800px><img />


Aplicando zoom de 100% em torno do segundo ponto fixo
```py
elliptic.set_zoom((1, 0))
elliptic.create_image('elliptic_zoom_1.png')
```

<img src="https://github.com/marjrohn/MobiusTransform/assets/61857287/07acf537-a083-4f20-8473-2d35dccb4fc9" width=800px><img />

#### Propriedades de Video
É possivel mudar a velocidade do video, resolução, FPS e mudar as cores dos polignos
```py
loxodromic.set_gridsize(1024) # dobra tamanho da malha para criação dos polignos, padrão é 512
loxodromic.set_colors(['cyan', 'magenta', 'yellow', 'black'])
#RGB normalizado também funciona
#loxodromic.set_colors([(0, 1, 1), (1, 0, 1), (1, 1, 0), (0, 0, 0)])

loxodromic.create_video('loxodromic_fancy.mov', 
	resolution=(1200, 800),
	speed=2, 
	duration=20, 
	frame_rate=30
)
```

<video src="https://github.com/marjrohn/MobiusTransform/assets/61857287/5c6c8b4e-4481-45ee-8aa5-666d710b349b" width=600px/><video />


## Referência
<a id="1" />[1] <a/>
Needham, T. (1997). Visual Complex Analysis. Clarendon Press.
