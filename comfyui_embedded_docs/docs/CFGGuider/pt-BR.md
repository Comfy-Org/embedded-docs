# CFGGuider

O nó CFGGuider cria um sistema de orientação para controlar o processo de amostragem na geração de imagens. Ele recebe um modelo juntamente com entradas de condicionamento positivo e negativo, em seguida, aplica uma escala de orientação livre de classificador para direcionar a geração em direção ao conteúdo desejado, evitando elementos indesejados. Este nó gera um objeto guia que pode ser usado por nós de amostragem para controlar a direção da geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser usado para orientação | MODEL | Sim | - |
| `positivo` | O condicionamento positivo que guia a geração em direção ao conteúdo desejado | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo que afasta a geração de conteúdo indesejado | CONDITIONING | Sim | - |
| `cfg` | A escala de orientação livre de classificador que controla o quão fortemente o condicionamento influencia a geração (padrão: 8,0) | FLOAT | Sim | 0,0 a 100,0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `GUIDER` | Um objeto guia que pode ser passado para nós de amostragem para controlar o processo de geração | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80c1f733dc26717c5762655404b9c36b53bb9059ceb6a8531ef1a853e2fe2380`
