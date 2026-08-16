# HappyHorse Texto para Vídeo

Gera um vídeo com base em um prompt de texto usando o modelo HappyHorse. Este nó envia seu prompt e configurações para a API HappyHorse, aguarda a geração do vídeo e baixa o resultado.
## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `model` | O modelo HappyHorse usado para a geração, juntamente com seus subparâmetros. A seleção de um modelo determina quais subparâmetros estão disponíveis (veja as seções dos modelos abaixo). | DYNAMIC_COMBO | Sim | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `seed` | Semente usada para a geração. Usar a mesma semente com as mesmas entradas produzirá o mesmo resultado. (padrão: 0). | INT | Sim | 0 to 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False). | BOOLEAN | Sim | True / False |

### happyhorse-1.1-t2v Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `prompt` | Prompt que descreve os elementos e características visuais. Suporta inglês e chinês. (padrão: ""). | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | "720P"<br>"1080P" |
| `ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `duration` | A duração do vídeo em segundos. (padrão: 5, mín: 3, máx: 15, passo: 1). | INT | Sim | 3 to 15 |

### happyhorse-1.0-t2v Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `prompt` | Prompt que descreve os elementos e características visuais. Suporta inglês e chinês. (padrão: ""). | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | "720P"<br>"1080P" |
| `ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | A duração do vídeo em segundos. (padrão: 5, mín: 3, máx: 15, passo: 1). | INT | Sim | 3 to 15 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---|---|---|
| `VIDEO` | The generated video file. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`
