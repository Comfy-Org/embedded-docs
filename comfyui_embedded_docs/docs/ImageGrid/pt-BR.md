# Grade de Imagens

O nó Grade de Imagens combina múltiplas imagens em uma única grade ou colagem organizada. Ele recebe uma lista de imagens e as organiza em um número especificado de colunas, redimensionando cada imagem para caber em um tamanho de célula definido e adicionando espaçamento opcional entre elas. O resultado é uma única imagem nova contendo todas as imagens de entrada em um layout de grade.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | Uma lista de imagens a serem organizadas na grade. O nó requer pelo menos uma imagem para funcionar. | IMAGE | Sim | - |
| `colunas` | O número de colunas na grade (padrão: 4). | INT | Não | 1 - 20 |
| `largura_da_célula` | A largura, em pixels, de cada célula na grade (padrão: 256). | INT | Não | 32 - 2048 |
| `altura_da_célula` | A altura, em pixels, de cada célula na grade (padrão: 256). | INT | Não | 32 - 2048 |
| `espaçamento` | A quantidade de espaçamento, em pixels, a ser colocada entre as imagens na grade (padrão: 4). | INT | Não | 0 - 50 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A única imagem de saída contendo todas as imagens de entrada organizadas em uma grade. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/pt-BR.md)

---
**Source fingerprint (SHA-256):** `79d0942c79d3966d06fe804f839c1d677764cef90265bd621bf915fe6de0ad46`
