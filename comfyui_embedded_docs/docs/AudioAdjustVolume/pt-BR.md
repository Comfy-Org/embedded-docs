> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/pt-BR.md)

O nó AudioAdjustVolume modifica o volume do áudio aplicando ajustes de ganho em decibéis (dB). Ele recebe uma entrada de áudio e aplica um fator de ganho com base no nível de volume especificado, onde valores positivos aumentam o volume e valores negativos o diminuem. O nó retorna o áudio modificado com a mesma taxa de amostragem do original.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `audio` | AUDIO | Sim | - | A entrada de áudio a ser processada |
| `volume` | INT | Sim | -100 a 100 | Ajuste de volume em decibéis (dB). 0 = sem alteração, +6 = dobra, -6 = reduz pela metade, etc (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `audio` | AUDIO | O áudio processado com o nível de volume ajustado |

---
**Source fingerprint (SHA-256):** `0436765680671551239f7a89b575cdfb22590fbe662bdfe5da01bd1cd5c496ed`
