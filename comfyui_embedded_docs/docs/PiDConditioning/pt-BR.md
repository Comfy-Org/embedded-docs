# PiD Condicionamento

Anexa um `latent` e um valor `degrade_sigma` a um CONDITIONING para que possa ser usado para decodificação ou upscaling de PiD. Isso permite controlar o quanto o `latent` é degradado antes de ser processado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Os dados de condicionamento aos quais anexar o `latent` e o `degrade_sigma`. | CONDITIONING | Sim | - |
| `latent` | O `latent` (de VAEEncode ou de um KSampler) a ser anexado ao condicionamento. | LATENT | Sim | - |
| `latent_format` | O formato do `latent`. Latents Flux1 (16 canais) e Flux2 (128 canais) são detectados automaticamente a partir da dimensão de canais na opção `"flux"`. Para SD3 (16 canais), SDXL (4 canais) ou QwenImage (16 canais), selecione manualmente (padrão: `"flux"`). | COMBO | Sim | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | A quantidade de degradação a aplicar. 0 significa um `latent` limpo. Aumente este valor para remover ruído de saídas `latent` corrompidas (padrão: 0.0). | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |

Observação: quando `latent_format` é definido como `"flux"`, o nó detecta automaticamente o tipo de `latent` a partir da dimensão de canais: 128 canais são tratados como latents Flux2, enquanto 16 canais são tratados como latents Flux1.

Observação: um valor não suportado de `latent_format` gera um erro, mas todas as opções disponíveis são tratadas pelo nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `CONDITIONING` | Os dados de condicionamento originais com o `latent` e o valor `degrade_sigma` anexados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
