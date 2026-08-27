# PiD Condicionamento

Anexa uma imagem latente e um valor de sigma de degradação a um dado CONDITIONING. Isso é usado para decodificação PiD (Pixel-in-Detail) ou upscaling, permitindo controlar o quanto o latente é degradado antes do processamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `positivo` | Os dados de condicionamento aos quais anexar o latente e o sigma de degradação. | CONDITIONING | Sim | - |
| `latent` | O latente (de VAEEncode ou um KSampler) para anexar ao condicionamento. | LATENT | Sim | - |
| `formato do latent` | O formato do latente. Latentes Flux1 (16 canais) e Flux2 (128 canais) são detectados automaticamente pela dimensão de canais em `"flux"`. Para SD3 (16 canais), SDXL (4 canais) ou QwenImage (16 canais), selecione manualmente (padrão: `"flux"`). | COMBO | Sim | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | A quantidade de degradação a aplicar. 0 significa um latente limpo. Aumente esse valor para remover ruído de saídas latentes corrompidas (padrão: 0.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

Nota: Quando `latent_format` está definido como `"flux"`, o nó detecta automaticamente o tipo de latente a partir da dimensão do canal: 128 canais são tratados como latentes Flux2, enquanto 16 canais são tratados como latentes Flux1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `CONDITIONING` | Os dados de condicionamento originais com o latente e os valores de sigma de degradação anexados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
