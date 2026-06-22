# Caixa Delimitadora

O nó PrimitiveBoundingBox cria uma área retangular simples definida por sua posição e tamanho. Ele recebe coordenadas X e Y para o canto superior esquerdo, juntamente com valores de largura e altura, e gera uma estrutura de dados de caixa delimitadora que pode ser usada por outros nós em um fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `x` | A coordenada X do canto superior esquerdo da caixa delimitadora (padrão: 0). | INT | Sim | 0 a 8192 |
| `y` | A coordenada Y do canto superior esquerdo da caixa delimitadora (padrão: 0). | INT | Sim | 0 a 8192 |
| `largura` | A largura da caixa delimitadora (padrão: 512). | INT | Sim | 1 a 8192 |
| `altura` | A altura da caixa delimitadora (padrão: 512). | INT | Sim | 1 a 8192 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `bounding_box` | Uma estrutura de dados contendo as propriedades `x`, `y`, `largura` e `altura` do retângulo definido. | BOUNDING_BOX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/pt-BR.md)

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
