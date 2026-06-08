O nó ModelMergeWAN2_1 mescla dois modelos WAN2.1 combinando seus componentes usando médias ponderadas. Ele suporta diferentes tamanhos de modelo, incluindo modelos de 1,3B com 30 blocos e modelos de 14B com 40 blocos, com tratamento especial para modelos de imagem para vídeo que incluem um componente extra de incorporação de imagem. Cada componente dos modelos pode ser ponderado individualmente para controlar a proporção de mesclagem entre os dois modelos de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | Primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | Segundo modelo a ser mesclado | MODEL | Sim | - |
| `patch_embedding.` | Peso para o componente de incorporação de patches (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `time_embedding.` | Peso para o componente de incorporação temporal (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `time_projection.` | Peso para o componente de projeção temporal (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `text_embedding.` | Peso para o componente de incorporação de texto (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `img_emb.` | Peso para o componente de incorporação de imagem, usado em modelos de imagem para vídeo (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.0.` | Peso para o bloco 0 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.1.` | Peso para o bloco 1 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.2.` | Peso para o bloco 2 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.3.` | Peso para o bloco 3 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.4.` | Peso para o bloco 4 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.5.` | Peso para o bloco 5 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.6.` | Peso para o bloco 6 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.7.` | Peso para o bloco 7 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.8.` | Peso para o bloco 8 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.9.` | Peso para o bloco 9 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.10.` | Peso para o bloco 10 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.11.` | Peso para o bloco 11 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.12.` | Peso para o bloco 12 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.13.` | Peso para o bloco 13 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.14.` | Peso para o bloco 14 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.15.` | Peso para o bloco 15 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.16.` | Peso para o bloco 16 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.17.` | Peso para o bloco 17 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.18.` | Peso para o bloco 18 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.19.` | Peso para o bloco 19 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.20.` | Peso para o bloco 20 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.21.` | Peso para o bloco 21 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.22.` | Peso para o bloco 22 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.23.` | Peso para o bloco 23 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.24.` | Peso para o bloco 24 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.25.` | Peso para o bloco 25 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.26.` | Peso para o bloco 26 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.27.` | Peso para o bloco 27 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.28.` | Peso para o bloco 28 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.29.` | Peso para o bloco 29 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.30.` | Peso para o bloco 30 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.31.` | Peso para o bloco 31 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.32.` | Peso para o bloco 32 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.33.` | Peso para o bloco 33 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.34.` | Peso para o bloco 34 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.35.` | Peso para o bloco 35 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.36.` | Peso para o bloco 36 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.37.` | Peso para o bloco 37 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.38.` | Peso para o bloco 38 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `blocks.39.` | Peso para o bloco 39 (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |
| `head.` | Peso para o componente de cabeça (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |

**Nota:** Todos os parâmetros de peso usam uma faixa de 0,0 a 1,0 com incrementos de 0,01. O nó suporta até 40 blocos para acomodar diferentes tamanhos de modelo, onde modelos de 1,3B usam 30 blocos e modelos de 14B usam 40 blocos. O parâmetro `img_emb.` é específico para modelos de imagem para vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado combinando componentes de ambos os modelos de entrada de acordo com os pesos especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d550a2f62bbcb4b46ccdd8a04fab80e93f96ea63426d48acb3515d51175efc99`
