# PiD Condicionamento

Anexa uma imagem latente e um valor de sigma de degradação a um dado CONDITIONING. Isso é usado para decodificação PiD (Pixel-in-Detail) ou upscaling, permitindo controlar o quanto o latente é degradado antes do processamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Os dados de condicionamento aos quais anexar o latente e o sigma de degradação. | CONDITIONING | Sim | - |
| `latent` | A imagem latente (de VAEEncode ou um KSampler) a ser anexada ao condicionamento. | LATENT | Sim | - |
| `latent_format` | O formato do latente. Latentes Flux1 (16 canais) e Flux2 (128 canais) são detectados automaticamente pela dimensão do canal sob "flux". Para SD3 (16 canais), SDXL (4 canais) ou QwenImage (16 canais), selecione manualmente (padrão: "flux"). | COMBO | Sim | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 = latente limpo. Aumente para denoisar saídas latentes corrompidas (padrão: 0.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

Nota: Quando `latent_format` é "flux", o nó detecta automaticamente se o latente é Flux1 (16 canais) ou Flux2 (128 canais) com base na sua dimensão de canal. Se o latente processado tiver 5 dimensões, apenas a primeira fatia ao longo da última dimensão é usada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `CONDITIONING` | Os dados de condicionamento originais com os valores de latente e sigma de degradação anexados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
