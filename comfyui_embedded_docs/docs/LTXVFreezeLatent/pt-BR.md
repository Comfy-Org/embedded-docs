# LTXV Congelar Latent

O nó LTXV Freeze Latent define a máscara de ruído de um latent como zero, o que mantém esse latent limpo e inalterado durante a amostragem. Ele funciona com latents de vídeo e áudio, então um latent pode ser congelado antes de ser concatenado com outros ou quando não deve passar por denoising algum.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `latent` | Latent de vídeo ou áudio a congelar. Áudio é 4D; vídeo é 5D. | LATENT | Sim | N/A |

### Restrições

- O latent deve conter um tensor simples. Um latent concatenado de áudio e vídeo não é aceito; ele deve ser separado primeiro com o nó Separate AV Latent.
- Apenas latents 4D (áudio) e latents 5D (vídeo) são suportados. Qualquer outro shape causa um erro.
- A máscara de ruído gerada é criada com zeros usando o mesmo dispositivo do tensor de entrada. Para latents de vídeo, a máscara tem shape (batch, 1, frames, 1, 1); para latents de áudio, tem shape (batch, 1, frames, 1).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `latent` | O latent de entrada com uma máscara de ruído de zeros adicionada, de modo que permaneça limpo durante a amostragem. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
