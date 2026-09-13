# Geração de Vídeo com Múltiplos Quadros Vidu

This node generates a video by creating transitions between multiple keyframes. It starts from an initial image and animates through a sequence of user-defined end images and prompts, producing a single video file as output.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Vidu a ser usado para geração de vídeo. | COMBO | Sim | "viduq2-pro"<br>"viduq2-turbo" |
| `start_image` | A imagem do frame inicial. A proporção de aspecto deve estar entre 1:4 e 4:1. | IMAGE | Sim | Proporção de aspecto 1:4 a 4:1 |
| `seed` | Um valor de seed para geração de números aleatórios para garantir resultados reproduzíveis (padrão: 1). | INT | Sim | 0 a 2147483647 |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | "720p"<br>"1080p" |
| `frames` | Número de transições de keyframes (2-9). Selecionar um valor revela dinamicamente as entradas necessárias para cada frame. | DYNAMIC_COMBO | Sim | "2"<br>"3"<br>"4"<br>"5"<br>"6"<br>"7"<br>"8"<br>"9" |

### Entradas de frames (compartilhadas por todas as opções de contagem de frames)

Quando `frames` é definido como um número, as três entradas a seguir são exibidas para cada frame `i`, de 1 até esse número. Por exemplo, escolher "3" adiciona `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2` e `prompt3` / `end_image3` / `duration3`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt{i}` | Prompt de texto para a transição do frame {i}. Campo de texto multilinha. Máximo de 2000 caracteres. | STRING | Sim | Até 2000 caracteres |
| `end_image{i}` | Imagem do frame final para o segmento {i}. A proporção de aspecto deve estar entre 1:4 e 4:1. | IMAGE | Sim | Proporção de aspecto 1:4 a 4:1 |
| `duration{i}` | Duração do segmento {i} em segundos (padrão: 4). | INT | Sim | 2 a 7 |

**Notas:**

- Todas as entradas são obrigatórias. `seed` tem um valor padrão, mas ainda é uma entrada obrigatória.
- `start_image` e cada `end_image{i}` devem ter uma proporção de aspecto entre 1:4 e 4:1.
- Cada `prompt{i}` tem comprimento máximo de 2000 caracteres.
- Cada `duration{i}` deve estar entre 2 e 7 segundos.
- O número de frames pode ser entre 2 e 9, então os índices de frames possíveis vão de 1 a 9.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado contendo todas as transições animadas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
