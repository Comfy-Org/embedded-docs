# Concatenar latente AV

O nó LTXVConcatAVLatent combina um latente de vídeo e um latente de áudio em um único latente conjunto, para uso com modelos audiovisuais como LTXV ou MiniMax H3. Ele agrupa as `samples` de ambas as entradas e, se qualquer uma das entradas incluir um `noise_mask`, essas máscaras também são agrupadas. Se o latente de vídeo já for um latente AV, o nó mantém seu fluxo de vídeo e substitui seu fluxo de áudio pelo latente de áudio fornecido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `video_latent` | Representação latente dos dados de vídeo. | LATENT | Sim |  |
| `audio_latent` | Representação latente dos dados de áudio a serem combinados com o latente de vídeo. | LATENT | Sim |  |

**Observação sobre a duração do áudio:** Quando `video_latent` já é um latente AV, `audio_latent` deve corresponder ao fluxo de áudio incorporado em todas as dimensões, exceto uma. O nó remove ou preenche com zeros o áudio nessa dimensão para se ajustar ao comprimento do fluxo existente. A cauda preenchida é deixada sem máscara para que o modelo possa gerá-la.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | Um latente contendo as `samples` de vídeo e áudio emparelhadas. Se qualquer entrada fornecer um `noise_mask`, a saída também conterá um `noise_mask` emparelhado; uma máscara ausente é substituída por uns. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
