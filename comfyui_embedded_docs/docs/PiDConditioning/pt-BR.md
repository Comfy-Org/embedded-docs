# Visão Geral

Anexa uma imagem latente e um valor de sigma de degradação a um dado CONDITIONING. Isso é usado para decodificação ou upscaling PiD (Pixel-in-Detail), permitindo controlar o quanto o latente é degradado antes do processamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Os dados de condicionamento aos quais anexar o latente e o sigma de degradação. | CONDITIONING | Sim | - |
| `latent` | A imagem latente (do VAEEncode ou de um KSampler) a ser anexada ao condicionamento. | LATENT | Sim | - |
| `formato do latent` | O formato do latente. Latentes Flux1 e Flux2 são detectados automaticamente pela dimensão do canal. SD3 deve ser selecionado manualmente (padrão: "flux"). | COMBO | Sim | `"flux"`<br>`"sd3"` |
| `degrade_sigma` | A quantidade de degradação a ser aplicada. 0 significa um latente limpo. Aumente este valor para remover ruído de saídas latentes corrompidas (padrão: 0.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento originais com o latente e os valores de sigma de degradação anexados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7c8de543629c2299fc2c1e035e433dfc249af594773a77e65c69dde67eb104d7`
