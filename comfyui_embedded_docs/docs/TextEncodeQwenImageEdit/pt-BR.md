> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/pt-BR.md)

O nó TextEncodeQwenImageEdit processa prompts de texto e imagens opcionais para gerar dados de condicionamento para geração ou edição de imagens. Ele utiliza um modelo CLIP para tokenizar a entrada e pode, opcionalmente, codificar imagens de referência usando um VAE para criar latentes de referência. Quando uma imagem é fornecida, ela é redimensionada automaticamente para manter dimensões de processamento consistentes.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `clip` | CLIP | Sim | - | Modelo CLIP usado para tokenização de texto e imagem |
| `prompt` | STRING | Sim | - | Prompt de texto para geração de condicionamento, suporta entrada multilinha e prompts dinâmicos |
| `vae` | VAE | Não | - | Modelo VAE opcional para codificar imagens de referência em latentes |
| `image` | IMAGE | Não | - | Imagem de entrada opcional para fins de referência ou edição |

**Observação:** Quando tanto `image` quanto `vae` são fornecidos, o nó codifica a imagem em latentes de referência e os anexa à saída de condicionamento. A imagem é redimensionada automaticamente para manter uma escala de processamento consistente de aproximadamente 1024x1024 pixels.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `CONDITIONING` | CONDITIONING | Dados de condicionamento contendo tokens de texto e latentes de referência opcionais para geração de imagem |

---
**Source fingerprint (SHA-256):** `143af2c93aa56ace3594ecb257cac9dbaef2666665f3fb6dfd7a987cd2ea326f`
