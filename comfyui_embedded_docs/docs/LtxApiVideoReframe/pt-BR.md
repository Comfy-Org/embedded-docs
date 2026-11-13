# LTX Video Reframe

Reenquadra um vídeo para uma nova resolução e proporção de tela. A área fora do vídeo original é gerada para corresponder ao conteúdo dele, de modo que um clipe em retrato possa se tornar um em paisagem, ou o contrário.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo a ser reenquadrado, com até 60 segundos e 1800 quadros, com cada lado entre 64 e 4096 pixels. | VIDEO | Sim | - |
| `resolution` | Tamanho da saída e proporção de tela, em 720p ou 1080p. Padrão: `"(1080p) 1080x1920 (9:16)"`. | COMBO | Sim | `"(720p) 720x720 (1:1)"`<br>`"(720p) 720x900 (4:5)"`<br>`"(720p) 900x720 (5:4)"`<br>`"(720p) 720x1280 (9:16)"`<br>`"(720p) 1280x720 (16:9)"`<br>`"(1080p) 1080x1080 (1:1)"`<br>`"(1080p) 1080x1350 (4:5)"`<br>`"(1080p) 1350x1080 (5:4)"`<br>`"(1080p) 1080x1920 (9:16)"`<br>`"(1080p) 1920x1080 (16:9)"` |
| `placement` | Onde o vídeo original fica no novo quadro. O vídeo sempre preenche um lado do quadro, então uma âncora o move apenas ao longo do outro lado. Padrão: `"center"`. | DYNAMIC_COMBO | Sim | `"center"`<br>`"top"`<br>`"bottom"`<br>`"left"`<br>`"right"`<br>`"custom"` |
| `seed` | Controla se o nó é executado novamente; os resultados são não determinísticos independentemente da semente. Padrão: 42. | INT | Não | 0 a 4294967295 |

### Entradas de posicionamento "custom"

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `x` | Borda esquerda do vídeo como uma fração da largura da saída. Padrão: 0.25. | FLOAT | Não | 0.0 a 0.99 (passo 0.01) |
| `y` | Borda superior do vídeo como uma fração da altura da saída. Padrão: 0.25. | FLOAT | Não | 0.0 a 0.99 (passo 0.01) |
| `width` | Largura do vídeo como uma fração da largura da saída; a altura segue a proporção de tela do vídeo. O vídeo deve permanecer dentro do quadro e pode ser ampliado no máximo 2x. Padrão: 0.5. | FLOAT | Não | 0.01 a 1.0 (passo 0.01) |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo reenquadrado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoReframe/pt-BR.md)

---
**Source fingerprint (SHA-256):** `85fcce4a8054fa8faf0085a55510ee09bce89afd1cf9f19d6ea45105549f2656`
