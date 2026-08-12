# TopazImageEnhanceV2

O Topaz Image Enhance aplica ampliação de escala (upscaling) e aprimoramento de imagem de padrão industrial a uma única imagem de entrada usando modelos Topaz. Ele envia a imagem para a API do Topaz, processa com o modelo selecionado e retorna o resultado aprimorado. Você pode escolher entre três modelos: Reimagine, Bloom 2 e Wonder 3.5.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser aprimorada. Apenas uma imagem de entrada é suportada. | IMAGE | Sim | Imagem única |
| `model` | O modelo de aprimoramento Topaz a ser utilizado. O modelo selecionado determina quais configurações específicas do modelo aparecem. | STRING | Sim | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Valor zero significa calcular automaticamente (geralmente será o tamanho original ou redimensionado proporcionalmente a `output_height` se especificado). O Wonder 3.5 suporta apenas fatores de ampliação de 1x a 6x. O Bloom 2 e o Wonder 3.5 preservam a proporção de aspecto da entrada e tratam o tamanho solicitado como alvo. (padrão: 0) | INT | Não | 0 a 32000 |
| `output_height` | Valor zero significa gerar a saída com a mesma altura da original ou redimensionado proporcionalmente a `output_width` se especificado. O Wonder 3.5 suporta apenas fatores de ampliação de 1x a 6x. O Bloom 2 e o Wonder 3.5 preservam a proporção de aspecto da entrada e tratam o tamanho solicitado como alvo. (padrão: 0) | INT | Não | 0 a 32000 |

### Configurações do Reimagine

Estas configurações se aplicam quando `model` está definido como `"Reimagine"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto opcional para orientação criativa na ampliação. (padrão: "") | STRING | Sim | Qualquer texto |
| `creativity` | Nível de criatividade para o aprimoramento. (padrão: 3) | INT | Sim | 1 a 9 |
| `subject_detection` | Modo de detecção de assunto. | STRING | Sim | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Aprimorar rostos (se houver) durante o processamento. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `face_enhancement_creativity` | Define o nível de criatividade para o aprimoramento facial. (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `face_enhancement_strength` | Controla a nitidez dos rostos aprimorados em relação ao fundo. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `face_preservation` | Preservar a identidade facial dos assuntos. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `color_preservation` | Preservar as cores originais. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `crop_to_fill` | Por padrão, a imagem recebe barras (letterbox) quando a proporção de aspecto da saída é diferente. Ative para cortar a imagem e preencher as dimensões de saída. (padrão: False) | BOOLEAN | Sim | true<br>false |

### Configurações do Bloom 2

Estas configurações se aplicam quando `model` está definido como `"Bloom 2"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto opcional para geração. Deixe vazio para gerar automaticamente um prompt a partir da imagem de entrada. (padrão: "") | STRING | Sim | Qualquer texto |
| `creativity` | 1 é um aprimoramento contido, 9 é uma reinterpretação acentuada com detalhes recém-gerados. (padrão: 3) | INT | Sim | 1 a 9 |
| `seed` | Semente (seed) para geração reproduzível. (padrão: 2) | INT | Sim | 1 a 2000 |
| `color_preservation` | Preservar as cores originais. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `grain` | Adicionar granulação à imagem de saída. (padrão: False) | BOOLEAN | Sim | true<br>false |
| `grain_model` | Modelo de granulação a ser usado. É ignorado se a granulação estiver desativada. | STRING | Sim | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Força do efeito de granulação. É ignorado se a granulação estiver desativada. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |
| `grain_size` | Tamanho das partículas de granulação. É ignorado se a granulação estiver desativada. (padrão: 1.0) | FLOAT | Sim | 1.0 a 5.0 |
| `grain_density` | Intensidade do efeito de granulação. É ignorado se a granulação estiver desativada. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |

### Configurações do Wonder 3.5

Estas configurações se aplicam quando `model` está definido como `"Wonder 3.5"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Nível de aprimoramento para diferentes condições de entrada. (padrão: "high") | STRING | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Adicionar granulação à imagem de saída. (padrão: False) | BOOLEAN | Sim | true<br>false |
| `grain_model` | Modelo de granulação a ser usado. É ignorado se a granulação estiver desativada. | STRING | Sim | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Força do efeito de granulação. É ignorado se a granulação estiver desativada. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |
| `grain_size` | Tamanho das partículas de granulação. É ignorado se a granulação estiver desativada. (padrão: 1.0) | FLOAT | Sim | 1.0 a 5.0 |
| `grain_density` | Intensidade do efeito de granulação. É ignorado se a granulação estiver desativada. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem aprimorada e ampliada retornada pela API do Topaz. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4301abb7cbab5122490b2ed3b328b199a29409da0dcc5ea5201570c2acbc2a58`
