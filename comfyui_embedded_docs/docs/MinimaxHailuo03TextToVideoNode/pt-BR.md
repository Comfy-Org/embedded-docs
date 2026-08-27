# MiniMax H3 Texto para Vídeo

Este nó gera um vídeo a partir de um prompt de texto usando o modelo MiniMax H3. Ele envia o texto juntamente com as configurações de vídeo, como resolução, proporção de aspecto e duração, para a API do MiniMax, aguarda a conclusão da tarefa de geração e retorna o vídeo resultante.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `modelo` | Modelo a ser usado para geração de vídeo. (padrão: "MiniMax H3"). Selecionar este modelo também fornece as configurações de prompt de texto, resolução, proporção e duração para o vídeo gerado (consulte Entradas do MiniMax H3 abaixo). | DYNAMIC_COMBO | Sim | `"MiniMax H3"` |
| `semente` | Semente aleatória. A mesma solicitação com a mesma semente gera resultados semelhantes, mas não necessariamente idênticos. (padrão: 42) | INT | Sim | 0 a 4294967295 |
| `marca d'água` | Se deve adicionar uma marca d'água AIGC ao vídeo. (padrão: false) | BOOLEAN | Não | true<br>false |

### Entradas do MiniMax H3

Estas configurações aparecem quando o modelo "MiniMax H3" é selecionado.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `prompt` | Prompt de texto para a geração de vídeo. | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "768P"<br>"2K" |
| `ratio` | Proporção de aspecto do vídeo de saída. (padrão: "16:9") | COMBO | Sim | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duração do vídeo de saída em segundos (4-15). (padrão: 5) | INT | Sim | 4 a 15 |

Observação: o prompt de texto incluído na opção `model` deve conter pelo menos um caractere que não seja espaço em branco. O preço estimado exibido para este nó é calculado a partir da resolução selecionada e da duração do vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `VIDEO` | O vídeo gerado a partir do prompt de texto fornecido. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `93f7c81ba4053da999d29392bce23f7fd809d21876ea489747d203201ed0377f`
