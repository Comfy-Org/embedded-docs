# Text Encode Ming Image Edit

Text Encode Ming Image Edit codifica um prompt de texto em condicionamento para edição de imagem Ming, opcionalmente misturando imagens de referência. O prompt e as imagens de referência são tokenizados por um modelo CLIP e, quando um VAE está conectado, as imagens de referência também são codificadas em quadros latentes que são anexados ao condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | O modelo CLIP usado para tokenizar o prompt e as imagens de referência. | CLIP | Sim | - |
| `vae` | VAE opcional que codifica as imagens de referência em quadros latentes anexados ao condicionamento. Sem um VAE, as imagens apenas condicionam o codificador de texto por meio da torre de visão. | VAE | Não | - |
| `prompt` | Prompt de texto a codificar. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | Texto multilinha |
| `images` | Slot expansível: imagens de referência opcionais vistas pelo codificador de texto e anexadas à sequência latente como quadros limpos. Conecte 1..8 imagens (`image_1`, `image_2`, ...); imagens posteriores são redimensionadas para o tamanho da primeira, e o latente amostrado deve corresponder ao tamanho dela. Apenas os canais RGB são usados. | IMAGE | Não | 0 a 8 |

**Observação:** As imagens de referência são lidas em ordem numérica dos nomes dos seus slots, e slots vazios são ignorados. Latentes de referência só são produzidos quando tanto o `vae` quanto pelo menos uma imagem são fornecidos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `CONDITIONING` | Condicionamento contendo o prompt codificado, além dos latentes de referência quando um VAE e imagens de referência são fornecidos. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMingImageEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `675fb3cc0af006e1284fdb2a5ca2c268c540ee92e1ede90b2359f4e3fc8ba5ea`
