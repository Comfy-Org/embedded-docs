# ByteDance Seedance 2.0 Texto para Vídeo

Este nó gera um vídeo a partir de uma descrição textual usando os modelos Seedance 2.5 ou 2.0 da ByteDance. Ele envia seu prompt para o modelo selecionado, aguarda o processamento do vídeo e retorna o resultado final.

## Entradas

O parâmetro `model` é um combo dinâmico. Ao selecionar um modelo, ele revela várias entradas específicas do modelo que devem ser preenchidas, incluindo o prompt de texto, resolução, proporção de aspecto, duração e configuração de geração de áudio.

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `model` | O modelo a ser usado para geração de vídeo. O Seedance 2.5 é o modelo mais recente, gerando vídeos de até 30 segundos com saída em mp4/mov; o Seedance 2.0 oferece qualidade máxima com 1080p/4k; o Fast é para otimização de velocidade; o Mini é a geração mais rápida e de menor custo. | DYNAMIC_COMBO | Sim | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed (padrão: 0). | INT | Não | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água ao vídeo (padrão: False). Esta é uma configuração avançada. | BOOLEAN | Não | True / False |

### Entradas do Seedance 2.5

Essas entradas aparecem quando `model` está definido como `Seedance 2.5`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `prompt` | Prompt de texto para geração de vídeo. Coloque as falas entre aspas duplas para direcionar o diálogo gerado (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída (padrão: `"720p"`). | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 4 a 30 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Não | True / False |
| `output_format` | Formato de contêiner do vídeo de saída (padrão: `"mp4"`). | COMBO | Sim | `"mp4"` |

### Entradas do Seedance 2.0

Essas entradas aparecem quando `model` está definido como `Seedance 2.0`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `prompt` | Prompt de texto para geração de vídeo (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 7). | INT | Sim | 4 a 15 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Não | True / False |

### Entradas do Seedance 2.0 Fast e do Seedance 2.0 Mini

Essas entradas aparecem quando `model` está definido como `Seedance 2.0 Fast` ou `Seedance 2.0 Mini`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `prompt` | Prompt de texto para geração de vídeo (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `ratio` | Proporção de aspecto do vídeo de saída (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 7). | INT | Sim | 4 a 15 |
| `generate_audio` | Habilita a geração de áudio para o vídeo de saída (padrão: True). | BOOLEAN | Não | True / False |

**Nota:** O `prompt` deve conter pelo menos 1 caractere após a remoção de espaços em branco; caso contrário, a tarefa falha na validação. Os limites de duração dependem do modelo: o Seedance 2.5 suporta de 4 a 30 segundos, enquanto o Seedance 2.0, o Seedance 2.0 Fast e o Seedance 2.0 Mini suportam de 4 a 15 segundos. As opções de resolução também diferem por modelo: o Seedance 2.5 suporta 480p e 720p; o Seedance 2.0 suporta 480p, 720p, 1080p e 4k; o Seedance 2.0 Fast e o Seedance 2.0 Mini suportam apenas 480p e 720p.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|--------------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `66d200f4ddf674b897def63604b0f29dcbf655e00b4e9b9c11e31b671ead94bc`
