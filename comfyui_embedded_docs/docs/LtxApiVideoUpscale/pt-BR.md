# LTX Video Upscale

Aumenta a resolução de um vídeo para 1080p, 4K ou 8K, mantendo sua proporção, taxa de quadros e áudio.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo para aumentar a resolução, com o lado menor de pelo menos 480 pixels e no máximo 7680x4320 em qualquer orientação. Até 2401 quadros para 1080p, 601 quadros para 4K e 241 quadros para 8K. | VIDEO | Sim | - |
| `resolution` | Tamanho de saída, o maior possível que caiba em 1920x1080, 3840x2160 ou 7680x4320 e rotacionado para vídeos em retrato. Padrão: `"4k"`. | COMBO | Sim | `"1080p"`<br>`"4k"`<br>`"8k"` |
| `seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 4294967295 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo com resolução aumentada, com seu áudio preservado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoUpscale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9b3b760365568ab2f6572c5f4f28758d67c4f5795fc39716ed4f648aafef80e`
