# Cortar Vídeo (Temporal Aleatório)

Recorta aleatoriamente um intervalo contínuo de quadros de um vídeo de entrada. O número de quadros a manter é definido pelo parâmetro `length`, e a posição inicial é escolhida aleatoriamente usando o parâmetro `seed`. O nó opera de forma lazy, o que significa que ele não processa o vídeo inteiro até que a saída seja usada downstream.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `vídeo` | Vídeo de entrada. | VIDEO | Sim | – |
| `comprimento` | Número de quadros a manter. Se `length` for maior que o número total de quadros no vídeo, o vídeo inteiro é mantido. (padrão: 16) | INT | Sim | min: 1, max: 99999 |
| `semente` | Semente aleatória. (padrão: 0) | INT | Sim | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `vídeo` | Vídeo cortado (lazy). | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
