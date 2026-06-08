O nó ImageYUVToRGB converte imagens do espaço de cores YUV para o espaço de cores RGB. Ele recebe três imagens de entrada separadas representando os canais Y (luminância), U (projeção azul) e V (projeção vermelha) e as combina em uma única imagem RGB usando conversão de espaço de cores.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `Y` | A imagem de entrada do canal Y (luminância) | IMAGE | Sim | - |
| `U` | A imagem de entrada do canal U (projeção azul) | IMAGE | Sim | - |
| `V` | A imagem de entrada do canal V (projeção vermelha) | IMAGE | Sim | - |

**Nota:** Todas as três imagens de entrada (Y, U e V) devem ser fornecidas juntas e devem ter dimensões compatíveis para uma conversão adequada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A imagem RGB convertida | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ee160be21fce75b3a3e41e25dc1cb0b20305383ff26f9698f07b93d42f98c64f`
