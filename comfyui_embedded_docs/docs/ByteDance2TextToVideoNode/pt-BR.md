# ByteDance Seedance 2.0 Texto para Vídeo

Este nó gera um vídeo a partir de um prompt de texto usando os modelos Seedance 2.5 ou 2.0 da ByteDance. Ele envia o prompt ao modelo selecionado, aguarda o término do processamento do vídeo e retorna o arquivo de vídeo resultante. Selecionar o modelo `Seedance 2.5 Draft` renderiza, em vez disso, uma prévia rápida em 480p; conecte o `draft_task_id` resultante ao nó ByteDance Seedance 2.5 Draft to Final Video para renderizar o vídeo final em 1080p.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo Seedance a ser usado para geração de vídeo. O Seedance 2.5 é o modelo mais recente, com suporte a vídeos de até 30 segundos e saída mp4; o Seedance 2.5 Draft renderiza uma prévia rápida em 480p cuja saída `draft_task_id` renderiza o vídeo final em 1080p no nó ByteDance Seedance 2.5 Draft to Final Video; o Seedance 2.0 é para qualidade máxima e 4k; o Seedance 2.0 Fast é para otimização de velocidade; o Seedance 2.0 Mini é para a geração mais rápida e de menor custo. Selecionar um modelo revela entradas adicionais para o prompt, resolução, proporção, duração e geração de áudio. | DYNAMIC_COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `semente` | Controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da `seed`. (padrão: 0) | INT | Não | 0 a 2147483647 |
| `marca_d'água` | Se deve adicionar uma marca d'água ao vídeo. (padrão: False) Esta é uma configuração avançada. | BOOLEAN | Não | True / False |

### Entradas do Seedance 2.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. Coloque falas entre aspas duplas para orientar o diálogo gerado. | STRING | Sim | — |
| `resolution` | Resolução do vídeo de saída. (padrão: `"720p"`) | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Proporção de aspecto do vídeo de saída. (padrão: `"16:9"`) | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 5) | INT | Sim | 4 a 30 |
| `generate_audio` | Ativa a geração de áudio para o vídeo de saída. (padrão: True) | BOOLEAN | Sim | True / False |
| `output_format` | Formato de contêiner do vídeo de saída. (padrão: `"mp4"`) | COMBO | Sim | `"mp4"` |

### Entradas do Seedance 2.5 Draft

Essas entradas aparecem quando `Seedance 2.5 Draft` está selecionado. O conjunto de parâmetros corresponde ao Seedance 2.5 acima, exceto que `resolution` oferece apenas `"480p"` (padrão `"480p"`).

### Entradas do Seedance 2.0

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. | STRING | Sim | — |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de aspecto do vídeo de saída. (padrão: `"16:9"`) | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 7) | INT | Sim | 4 a 15 |
| `generate_audio` | Ativa a geração de áudio para o vídeo de saída. (padrão: True) | BOOLEAN | Sim | True / False |

### Entradas do Seedance 2.0 Fast e do Seedance 2.0 Mini

Compartilhadas pelo Seedance 2.0 Fast e pelo Seedance 2.0 Mini; ambos os modelos expõem os mesmos parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para geração de vídeo. | STRING | Sim | — |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída. (padrão: `"16:9"`) | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 7) | INT | Sim | 4 a 15 |
| `generate_audio` | Ativa a geração de áudio para o vídeo de saída. (padrão: True) | BOOLEAN | Sim | True / False |

**Nota:** O seletor `model` é dinâmico; as entradas mostradas em cada seção de modelo aparecem quando esse modelo é selecionado. O prompt deve ter pelo menos 1 caractere após a remoção de espaços em branco. Os limites de resolução e duração dependem do modelo selecionado: o Seedance 2.5 suporta 480p/720p/1080p e 4 a 30 segundos; o Seedance 2.0 suporta 480p/720p/1080p/4k e 4 a 15 segundos; e o Seedance 2.0 Fast e o Seedance 2.0 Mini suportam apenas 480p/720p e 4 a 15 segundos; o Seedance 2.5 Draft suporta apenas 480p e 4 a 30 segundos. Cada execução retorna seu ID de tarefa como `draft_task_id`, mas apenas o ID de uma execução de `Seedance 2.5 Draft` pode ser renderizado pelo nó ByteDance Seedance 2.5 Draft to Final Video, portanto, com qualquer outro modelo, a saída deve ser deixada desconectada; caso contrário, a execução falhará. O valor de `seed` controla apenas se o nó será executado novamente; ele não torna os resultados determinísticos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |
| `draft_task_id` | ID da tarefa retornado pela execução. Apenas uma execução de `Seedance 2.5 Draft` produz um rascunho que o nó ByteDance Seedance 2.5 Draft to Final Video pode renderizar; com qualquer outro modelo, a saída deve ser deixada desconectada; caso contrário, a execução falhará. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2abad0c4eab5a1286c8da9237bcec52b275c40188b3b7dc9eede5d5f4cbb11d3`
