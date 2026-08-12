# AddLayer

O nó Add Layer transforma uma imagem de entrada em uma camada e a coloca em uma tela, seja iniciando uma nova pilha de camadas ou anexando-a a uma existente. Você pode definir o nome, posição, tamanho, rotação, opacidade, modo de mesclagem, ordem de empilhamento e inversão horizontal ou vertical da camada. Este nó está marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `layers` | Pilha de camadas à qual anexar. Deixe desconectado para iniciar uma nova pilha. | LAYERS | Não | — |
| `image` | Conteúdo da camada em seu tamanho nativo. Um lote se expande em camadas consecutivas. | IMAGE | Sim | — |
| `mask` | Máscara de transparência para esta camada. Áreas mascaradas (valor 1) tornam-se transparentes, multiplicando-se com qualquer canal alfa que a imagem já possua. | MASK | Não | — |
| `name` | Nome da camada exibido no editor do compositor. (padrão: "") | STRING | Não | — |
| `x` | Posicionamento horizontal inicial na tela. (padrão: 0) | INT | Não | -MAX_RESOLUTION a MAX_RESOLUTION |
| `y` | Posicionamento vertical inicial na tela. (padrão: 0) | INT | Não | -MAX_RESOLUTION a MAX_RESOLUTION |
| `opacity` | Opacidade inicial da camada. (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 (passo: 0.01) |
| `blend_mode` | Modo de mesclagem inicial, aplicado às camadas abaixo. Na camada inferior sobre o fundo transparente padrão, modos não normais produzem transparência. (padrão: "normal") | COMBO | Não | Múltiplas opções disponíveis |
| `rotation` | Rotação inicial em graus, no sentido horário. (padrão: 0.0) | FLOAT | Não | -360.0 a 360.0 (passo: 1.0) |
| `width` | Largura de exibição inicial. 0 mantém a largura nativa da imagem. (padrão: 0) | INT | Não | 0 a MAX_RESOLUTION |
| `height` | Altura de exibição inicial. 0 mantém a altura nativa da imagem. (padrão: 0) | INT | Não | 0 a MAX_RESOLUTION |
| `z_index` | Substituição de empilhamento. As camadas são ordenadas de forma estável por z_index; valores iguais mantêm sua ordem na lista. (padrão: 0) | INT | Não | -1000 a 1000 |
| `flip_h` | Inverter a camada horizontalmente. (padrão: False) | BOOLEAN | Não | false / true |
| `flip_v` | Inverter a camada verticalmente. (padrão: False) | BOOLEAN | Não | false / true |

Notas:
- Apenas `image` é obrigatório; todos os outros parâmetros são opcionais.
- Quando `layers` fica desconectado, uma nova pilha de camadas é criada. Quando uma pilha de camadas está conectada, a nova camada é anexada a ela.
- Um lote de imagens na entrada `image` cria múltiplas camadas consecutivas.
- `width` e `height` padrão são 0, o que mantém as dimensões nativas da imagem. Valores maiores que 0 substituem o tamanho de exibição.
- `opacity`, `blend_mode`, `rotation`, `width` e `height` são aplicados apenas quando diferem de seus valores padrão.
- O tamanho da tela de uma pilha de camadas conectada é preservado na saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `layers` | A pilha de camadas com esta camada anexada. | LAYERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddLayer/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b7bf1a012d17cb5768b49d5c0617e13562ba015f695e6c9b1d1bbefba4150f9e`
