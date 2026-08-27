# ByteDance Seedance 2.0 Texto para Vídeo

Este nó gera um vídeo a partir de um prompt de texto usando os modelos Seedance 2.5 ou 2.0 da ByteDance. Ele envia o prompt para o modelo selecionado, aguarda a conclusão do processamento do vídeo e retorna o arquivo de vídeo resultante.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `modelo` | O modelo Seedance a ser usado para geração de vídeo. O Seedance 2.5 é o modelo mais novo, com suporte a vídeos de até 30 segundos e saída mp4/mov; o Seedance 2.0 é para máxima qualidade e 4k; o Seedance 2.0 Fast é para otimização de velocidade; o Seedance 2.0 Mini é para a geração mais rápida e de menor custo. A seleção de um modelo revela entradas adicionais para o prompt, resolução, proporção de tela, duração e geração de áudio. | DYNAMIC_COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `semente` | Controla se o nó deve ser executado novamente; os resultados não são determinísticos, independentemente da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |
| `marca_d'água` | Se deve adicionar uma marca d'água ao vídeo. (padrão: False) Esta é uma configuração avançada. | BOOLEAN | Não | True / False |

### Entradas do Seedance 2.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `prompt` | Prompt de texto para geração de vídeo. Coloque falas entre aspas duplas para direcionar o diálogo gerado. | STRING | Sim | — |
| `resolution` | Resolução do vídeo de saída. (padrão: `"720p"`) | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Proporção de tela do vídeo de saída. (padrão: `"16:9"`) | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 5) | INT | Sim | 4 a 30 |
| `generate_audio` | Ativar a geração de áudio para o vídeo de saída. (padrão: True) | BOOLEAN | Sim | True / False |
| `output_format` | Formato de contêiner do vídeo de saída. (padrão: `"mp4"`) | COMBO | Sim | `"mp4"` |

### Entradas do Seedance 2.0

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `prompt` | Prompt de texto para geração de vídeo. | STRING | Sim | — |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de tela do vídeo de saída. (padrão: `"16:9"`) | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 7) | INT | Sim | 4 a 15 |
| `generate_audio` | Ativar a geração de áudio para o vídeo de saída. (padrão: True) | BOOLEAN | Sim | True / False |

### Entradas do Seedance 2.0 Fast e do Seedance 2.0 Mini

Compartilhadas pelo Seedance 2.0 Fast e pelo Seedance 2.0 Mini; ambos os modelos expõem os mesmos parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `prompt` | Prompt de texto para geração de vídeo. | STRING | Sim | — |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de tela do vídeo de saída. (padrão: `"16:9"`) | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 7) | INT | Sim | 4 a 15 |
| `generate_audio` | Ativar a geração de áudio para o vídeo de saída. (padrão: True) | BOOLEAN | Sim | True / False |

**Nota:** O seletor `model` é dinâmico; as entradas exibidas em cada seção do modelo aparecem quando esse modelo é selecionado. O prompt deve ter pelo menos 1 caractere após a remoção de espaços em branco. Os limites de resolução e duração dependem do modelo selecionado: o Seedance 2.5 suporta 480p/720p/1080p e de 4 a 30 segundos; o Seedance 2.0 suporta 480p/720p/1080p/4k e de 4 a 15 segundos; e o Seedance 2.0 Fast e o Seedance 2.0 Mini suportam apenas 480p/720p e de 4 a 15 segundos. O valor de `seed` controla apenas se o nó será executado novamente; ele não torna os resultados determinísticos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e3b11f5a538d4b9b7e49f651d3939651edfe85000e02e66a8d7700c3389c4b9c`
