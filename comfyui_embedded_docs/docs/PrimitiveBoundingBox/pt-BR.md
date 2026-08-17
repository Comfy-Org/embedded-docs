# Caixa Delimitadora

O nó PrimitiveBoundingBox cria uma área retangular simples definida pela sua posição e tamanho. Ele recebe as coordenadas X e Y do canto superior esquerdo, juntamente com os valores de largura e altura, e gera uma estrutura de dados de caixa delimitadora que pode ser usada por outros nós em um fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `x` | A coordenada X do canto superior esquerdo da caixa delimitadora (padrão: 0). | INT | Sim | 0 a 8192 |
| `y` | A coordenada Y do canto superior esquerdo da caixa delimitadora (padrão: 0). | INT | Sim | 0 a 8192 |
| `width` | A largura da caixa delimitadora (padrão: 512). | INT | Sim | 1 a 8192 |
| `height` | A altura da caixa delimitadora (padrão: 512). | INT | Sim | 1 a 8192 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `bounding_box` | Uma estrutura de dados contendo as propriedades `x`, `y`, `width` e `height` do retângulo definido. | BOUNDING_BOX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
