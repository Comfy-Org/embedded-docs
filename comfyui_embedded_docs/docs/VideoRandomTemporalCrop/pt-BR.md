# Cortar Vídeo (Temporal Aleatório)

Recorta aleatoriamente uma faixa contínua de quadros de um vídeo de entrada. O comprimento do corte é controlado pelo parâmetro `length`, e a posição inicial é escolhida usando uma semente aleatória. O nó opera de forma lazy, o que significa que ele não processa todo o vídeo até que a saída seja utilizada downstream.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `vídeo` | Vídeo de entrada. | VIDEO | Sim | – |
| `comprimento` | Número de quadros a manter. (padrão: 16) | INT | Sim | min: 1, max: 99999 |
| `semente` | Semente aleatória. (padrão: 0) | INT | Sim | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `vídeo` | Vídeo cortado (lazy). | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
