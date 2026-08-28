# Concatenar latente AV

Este nó mescla um latente de vídeo e um latente de áudio em um único latente conjunto de áudio-vídeo (AV), pronto para modelos AV como LTXV ou MiniMax H3. Se a entrada de vídeo já for um latente AV, o fluxo de vídeo é mantido e apenas o fluxo de áudio é substituído pelo latente de áudio fornecido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video_latent` | A representação latente dos dados de vídeo. Quando ela já contém ambos os fluxos, de vídeo e de áudio, o nó mantém o fluxo de vídeo e troca o áudio pelo de `audio_latent`. | LATENT | Sim |  |
| `audio_latent` | A representação latente dos dados de áudio. Seu comprimento é ajustado para caber no fluxo de vídeo: áudios mais longos são truncados e áudios mais curtos são preenchidos com zeros. | LATENT | Sim |  |

**Nota:** As amostras de ambas as entradas são combinadas como um par de fluxos de vídeo e áudio em um tensor aninhado. Se qualquer uma das entradas contiver um `noise_mask`, a saída incluirá uma máscara combinada; uma máscara ausente é substituída por uma máscara toda preenchida com uns, com a forma das amostras. Quando um áudio mais curto é preenchido com zeros, a região preenchida fica sem máscara para que o modelo possa gerá-la. O nó lança um erro se o latente de áudio não puder ser ajustado ao latente de vídeo, por exemplo, quando os dois latentes diferem em mais de uma dimensão ou quando diferem nas dimensões de lote ou de canal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | Um latente contendo as amostras de vídeo e áudio empacotadas juntas como dois fluxos, além de um `noise_mask` combinado quando pelo menos uma entrada fornece um. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
