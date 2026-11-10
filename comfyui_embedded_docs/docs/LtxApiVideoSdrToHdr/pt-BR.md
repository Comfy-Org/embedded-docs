# LTX Video SDR to HDR

Converte um vídeo SDR em um vídeo HDR de 10 bits em BT.2020 com a função de transferência HLG, na mesma resolução. O áudio não é mantido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo SDR a converter, no máximo 3840x2160 em qualquer orientação. Até 273 quadros em 1080p, 193 quadros em 1440p e 65 quadros em 4K. | VIDEO | Sim | - |
| `seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 4294967295 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo HDR de 10 bits convertido, sem áudio. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoSdrToHdr/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e5c0ef901f504a9477f042b4aef24935f4b85da52ccfaddfc764e9efec490915`
