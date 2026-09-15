# Topaz Aprimoramento de Imagem

Topaz Image Enhance aplica upscaling e aprimoramento de imagem padrão do setor a uma única imagem de entrada usando modelos Topaz. Ele envia a imagem para a API Topaz, processa-a com o modelo selecionado e retorna o resultado aprimorado. Você pode escolher entre três modelos: Reimagine, Bloom 2 e Wonder 3.5.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada a ser aprimorada. Apenas uma imagem de entrada é suportada. | IMAGE | Sim | Imagem única |
| `modelo` | O modelo de aprimoramento Topaz a ser usado. O modelo selecionado determina quais configurações específicas do modelo aparecem. | DYNAMIC_COMBO | Sim | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `largura de saída` | O valor zero significa calcular automaticamente (normalmente será o tamanho original ou dimensionado proporcionalmente a `output_height`, se especificado). Wonder 3.5 suporta fatores de upscaling apenas de 1x a 6x. Bloom 2 e Wonder 3.5 preservam a proporção da imagem de entrada e tratam o tamanho solicitado como uma meta. (padrão: 0) | INT | Não | 0 a 32000 |
| `altura de saída` | O valor zero significa gerar na mesma altura que o original ou dimensionar proporcionalmente a `output_width`, se especificado. Wonder 3.5 suporta fatores de upscaling apenas de 1x a 6x. Bloom 2 e Wonder 3.5 preservam a proporção da imagem de entrada e tratam o tamanho solicitado como uma meta. (padrão: 0) | INT | Não | 0 a 32000 |

### Entradas do Reimagine

Estas configurações se aplicam quando `model` está definido como `"Reimagine"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto opcional para orientar o upscaling criativo. (padrão: "") | STRING | Sim | Qualquer texto |
| `creativity` | Nível de criatividade para o aprimoramento. (padrão: 3) | INT | Sim | 1 a 9 |
| `subject_detection` | Modo de detecção de sujeito (avançado). | COMBO | Sim | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Aprimorar rostos (se presentes) durante o processamento. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `face_enhancement_creativity` | Define o nível de criatividade para o aprimoramento de rostos. (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `face_enhancement_strength` | Controla quão nítidos são os rostos aprimorados em relação ao fundo. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `face_preservation` | Preservar a identidade facial dos sujeitos. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `color_preservation` | Preservar as cores originais. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `crop_to_fill` | Por padrão, a imagem recebe letterbox quando a proporção de saída difere. Ative para recortar a imagem e preencher as dimensões de saída. (padrão: False) | BOOLEAN | Sim | true<br>false |

### Entradas do Bloom 2

Estas configurações se aplicam quando `model` está definido como `"Bloom 2"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto opcional para geração. Deixe vazio para gerar automaticamente um prompt a partir da imagem de entrada. (padrão: "") | STRING | Sim | Qualquer texto |
| `creativity` | 1 é aprimoramento contido, 9 é reinterpretação acentuada com detalhes recém-gerados. (padrão: 3) | INT | Sim | 1 a 9 |
| `seed` | Semente para geração reproduzível. (padrão: 2) | INT | Sim | 1 a 2000 |
| `color_preservation` | Preservar as cores originais. (padrão: True) | BOOLEAN | Sim | true<br>false |
| `grain` | Adicionar granulação à imagem de saída. (padrão: False) | BOOLEAN | Sim | true<br>false |
| `grain_model` | Modelo de granulação a ser usado. É ignorado se `grain` estiver desativado. | COMBO | Sim | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Força do efeito de granulação. É ignorado se `grain` estiver desativado. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |
| `grain_size` | Tamanho das partículas de granulação. É ignorado se `grain` estiver desativado. (padrão: 1.0) | FLOAT | Sim | 1.0 a 5.0 |
| `grain_density` | Intensidade do efeito de granulação. É ignorado se `grain` estiver desativado. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |

### Entradas do Wonder 3.5

Estas configurações se aplicam quando `model` está definido como `"Wonder 3.5"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Nível de aprimoramento para diferentes condições de entrada. (padrão: "high") | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Adicionar granulação à imagem de saída. (padrão: False) | BOOLEAN | Sim | true<br>false |
| `grain_model` | Modelo de granulação a ser usado. É ignorado se `grain` estiver desativado. | COMBO | Sim | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Força do efeito de granulação. É ignorado se `grain` estiver desativado. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |
| `grain_size` | Tamanho das partículas de granulação. É ignorado se `grain` estiver desativado. (padrão: 1.0) | FLOAT | Sim | 1.0 a 5.0 |
| `grain_density` | Intensidade do efeito de granulação. É ignorado se `grain` estiver desativado. (padrão: 0.5) | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** Apenas uma imagem de entrada é suportada; o nó lança um erro se o lote de entrada contiver mais de uma imagem. As configurações de granulação (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) são ignoradas a menos que `grain` esteja habilitado. Para o Bloom 2, deixar `prompt` vazio gera automaticamente um prompt a partir da imagem de entrada. Wonder 3.5 suporta fatores de upscaling apenas de 1x a 6x; Bloom 2 e Wonder 3.5 preservam a proporção da imagem de entrada e tratam o tamanho solicitado como uma meta.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem aprimorada e ampliada retornada pela API Topaz. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
