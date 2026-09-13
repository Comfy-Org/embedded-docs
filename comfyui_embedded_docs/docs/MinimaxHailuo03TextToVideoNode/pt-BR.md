# MiniMax H3 Texto para Vídeo

Este nó gera um vídeo a partir de um prompt de texto usando a família de modelos MiniMax H3: MiniMax H3, MiniMax H3 Max e MiniMax H3 Max Turbo. Você seleciona o modelo, insere um prompt de texto e ajusta configurações como resolução, proporção de aspecto e duração. O nó envia a solicitação para a API MiniMax, aguarda a conclusão da tarefa de geração e retorna o vídeo resultante.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para geração de vídeo (padrão: "MiniMax H3"). Selecionar um modelo também exibe as configurações específicas do modelo descritas nas seções abaixo. | DYNAMIC_COMBO | Sim | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente fornece resultados semelhantes, mas não garante resultados idênticos (padrão: 42). | INT | Sim | 0 a 4294967295 |
| `watermark` | Se deve adicionar uma marca d'água AIGC ao vídeo (padrão: false). Quando ativado, apenas o modelo "MiniMax H3" é compatível. | BOOLEAN | Não | true<br>false |

### Entradas do MiniMax H3

Essas configurações aparecem quando o modelo "MiniMax H3" é selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Deve conter pelo menos um caractere não em branco. | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "768P"<br>"2K" |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: "16:9"). | COMBO | Sim | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duração do vídeo de saída em segundos (4-15) (padrão: 5). | INT | Sim | 4 a 15 |

### Entradas do MiniMax H3 Max e do MiniMax H3 Max Turbo

Essas configurações são compartilhadas pelos modelos "MiniMax H3 Max" e "MiniMax H3 Max Turbo" e aparecem quando qualquer um dos modelos é selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Deve conter pelo menos um caractere não em branco e pode ter até 50.000 caracteres. | STRING | Sim | Até 50000 caracteres |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "480P"<br>"768P" |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: "16:9"). | COMBO | Sim | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duração do vídeo de saída em segundos (5-15) (padrão: 5). | INT | Sim | 5 a 15 |
| `prompt_expansion_mode` | Quanto esforço é gasto para reescrever o prompt antes da geração (padrão: "balanced"). | COMBO | Sim | "balanced"<br>"quality" |

### Notas

- Para todos os modelos, o prompt deve conter pelo menos um caractere não em branco.
- A configuração `watermark` é compatível apenas com "MiniMax H3". Ativá-la com "MiniMax H3 Max" ou "MiniMax H3 Max Turbo" causa um erro.
- Os modelos "MiniMax H3 Max" e "MiniMax H3 Max Turbo" limitam o prompt a 50.000 caracteres.
- Os limites de resolução e duração dependem do modelo selecionado: "MiniMax H3" é compatível com resolução "768P" e "2K" e vídeos de 4 a 15 segundos, enquanto "MiniMax H3 Max" e "MiniMax H3 Max Turbo" são compatíveis com resolução "480P" e "768P" e vídeos de 5 a 15 segundos.
- O preço estimado exibido para este nó é calculado a partir do modelo, da resolução e da duração selecionados.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado a partir do prompt de texto fornecido. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
