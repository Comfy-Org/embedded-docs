Este nó permite unir duas imagens em uma direção especificada (cima, baixo, esquerda, direita), com suporte para correspondência de tamanhos e espaçamento entre as imagens.

## Entradas

| Nome do Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `imagem1` | A primeira imagem a ser unida | IMAGE | Obrigatório | - | - |
| `imagem2` | A segunda imagem a ser unida; se não for fornecida, retorna apenas a primeira imagem | IMAGE | Opcional | Nenhum | - |
| `direção` | A direção para unir a segunda imagem: direita, baixo, esquerda ou cima | STRING | Obrigatório | right | right/down/left/up |
| `ajustar_tamanho_imagem` | Se deve redimensionar a segunda imagem para corresponder às dimensões da primeira imagem | BOOLEAN | Obrigatório | True | True/False |
| `largura_espacamento` | Largura do espaçamento entre as imagens, deve ser um número par | INT | Obrigatório | 0 | 0-1024 |
| `cor_espacamento` | Cor do espaçamento entre as imagens unidas | STRING | Obrigatório | white | white/black/red/green/blue |

> Para `spacing_color`, ao usar cores diferentes de "white/black", se `match_image_size` estiver definido como `false`, a área de preenchimento será preenchida com preto

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | A imagem unida | IMAGE |

## Exemplo de Fluxo de Trabalho

No fluxo de trabalho abaixo, usamos 3 imagens de entrada de tamanhos diferentes como exemplo:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![fluxo de trabalho](./asset/workflow.webp)

**Primeiro Nó de União de Imagens**

- `match_image_size`: false, as imagens serão unidas em seus tamanhos originais
- `direction`: up, `image2` será colocada acima de `image1`
- `spacing_width`: 20
- `spacing_color`: black

Imagem de saída 1:

![saída1](./asset/output-1.webp)

**Segundo Nó de União de Imagens**

- `match_image_size`: true, a segunda imagem será redimensionada para corresponder à altura ou largura da primeira imagem
- `direction`: right, `image3` aparecerá no lado direito
- `spacing_width`: 20
- `spacing_color`: white

Imagem de saída 2:

![saída2](./asset/output-2.webp)

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/pt-BR.md)
