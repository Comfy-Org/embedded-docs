# TextEncodeQwenImageEdit

O nó TextEncodeQwenImageEdit converte prompts de texto e imagens opcionais em dados de condicionamento para geração ou edição de imagens. Ele utiliza um modelo CLIP para tokenizar a entrada e pode, opcionalmente, codificar imagens de referência com um VAE para criar latentes de referência. Quando uma imagem é fornecida, ela é redimensionada automaticamente para manter uma escala de processamento consistente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização de texto e imagem | CLIP | Sim | - |
| `prompt` | Prompt de texto para geração de condicionamento, suporta entrada multilinha e prompts dinâmicos | STRING | Sim | - |
| `vae` | Modelo VAE opcional para codificar imagens de referência em latentes | VAE | Não | - |
| `image` | Imagem de entrada opcional para referência ou edição | IMAGE | Não | - |

**Nota:** Quando uma imagem é fornecida, ela é redimensionada para que sua contagem total de pixels permaneça próxima a 1.048.576 (1024 × 1024), e apenas seus canais RGB são utilizados. A imagem redimensionada é passada para o tokenizador CLIP juntamente com o prompt. Quando tanto `image` quanto `vae` são fornecidos, o nó também codifica a imagem em latentes de referência e os anexa à saída de condicionamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento contendo tokens de texto e latentes de referência opcionais para geração de imagens | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
