# Topaz Video Enhance

O nó **Topaz Video Enhance V2** dá nova vida ao vídeo com tecnologia avançada de upscaling e recuperação. Ele pode aumentar a resolução de um vídeo usando diferentes modelos de upscaling Topaz, ajustar a taxa de quadros por meio de interpolação e aplicar configurações de aprimoramento criativas ou realistas.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo de entrada a ser processado. Deve estar no formato de contêiner MP4. | VIDEO | Sim | - |
| `modelo de upscaling` | O modelo de IA usado para fazer upscaling do vídeo. Os subparâmetros disponíveis dependem do modelo selecionado. Selecionar `"Disabled"` desativa o upscaling. | DYNAMIC_COMBO | Sim | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `modelo de interpolação` | O modelo de IA usado para interpolação de quadros. Os subparâmetros disponíveis dependem do modelo selecionado. Selecionar `"Disabled"` desativa a interpolação. | DYNAMIC_COMBO | Sim | `"Disabled"`<br>`"apo-8"` |
| `nível de compressão dinâmica` | Nível CQP usado para compressão de vídeo (padrão: `"Low"`). | COMBO | Não | `"Low"`<br>`"Mid"`<br>`"High"` |

As seções a seguir descrevem os subparâmetros que aparecem para cada opção dos seletores `upscaler_model` e `interpolation_model`. As opções `"Disabled"` não exibem parâmetros adicionais.

### Entradas do Astra 2

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Resolução de saída alvo do upscaling. | COMBO | Sim (quando "Astra 2" é selecionado) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Força criativa do upscaling (padrão: 0.5). | FLOAT | Não | 0.0 a 1.0 (passo 0.1) |
| `upscaler_model.prompt` | Prompt de cena opcional, descritivo (não instrutivo). Quando definido, limita a entrada a 450 quadros (~15s a 30 fps) (padrão: vazio). | STRING | Não | - |
| `upscaler_model.sharp` | Nitidez pré-aprimoramento: 0.0=desfoque gaussiano, 0.5=passagem direta (padrão), 1.0=nitidez USM. | FLOAT | Não | 0.0 a 1.0 (passo 0.01) |
| `upscaler_model.realism` | Aproxima a saída do realismo fotográfico. Deixe em 0 para o padrão do modelo (padrão: 0.0). | FLOAT | Não | 0.0 a 1.0 (passo 0.01) |

### Entradas do Starlight (Astra) Fast

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Resolução de saída alvo do upscaling. | COMBO | Sim (quando este modelo é selecionado) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Entradas do Starlight (Astra) Creative

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Resolução de saída alvo do upscaling. | COMBO | Sim (quando este modelo é selecionado) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Força criativa do upscaling (padrão: `"low"`). | COMBO | Não | `"low"`<br>`"middle"`<br>`"high"` |

### Entradas do Starlight Precise 2.5

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Resolução de saída alvo do upscaling. | COMBO | Sim (quando este modelo é selecionado) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Entradas do apo-8

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `interpolation_model.interpolation_frame_rate` | Taxa de quadros de saída (padrão: 60). | INT | Sim (quando "apo-8" é selecionado) | 15 a 240 |
| `interpolation_model.interpolation_slowmo` | Fator de câmera lenta aplicado ao vídeo de entrada. Por exemplo, 2 deixa a saída duas vezes mais lenta e dobra a duração (padrão: 1). | INT | Não | 1 a 16 |
| `interpolation_model.interpolation_duplicate` | Analisar a entrada em busca de quadros duplicados e removê-los (padrão: False). | BOOLEAN | Não | True<br>False |
| `interpolation_model.interpolation_duplicate_threshold` | Sensibilidade de detecção para quadros duplicados (padrão: 0.01). | FLOAT | Não | 0.001 a 0.1 (passo 0.001) |

**Restrições importantes:**

- Pelo menos um entre `upscaler_model` ou `interpolation_model` deve estar habilitado. Se ambos estiverem definidos como `"Disabled"`, o nó gera um erro porque não há nada para processar.
- O vídeo de entrada `video` deve estar no formato de contêiner MP4.
- O modelo `"Astra 2"` é limitado a 9000 quadros de entrada. Quando um `prompt` é definido, o limite é de 450 quadros de entrada (~15 segundos a 30 fps). O nó gera um erro se o vídeo exceder o limite aplicável.
- `upscaler_model.upscaler_resolution` é obrigatório sempre que um modelo de upscaling diferente de `"Disabled"` for selecionado. `"FullHD (1080p)"` tem como alvo um resultado 1080p e `"4K (2160p)"` tem como alvo um resultado 2160p; a largura e a altura exatas da saída são calculadas a partir da proporção de aspecto da entrada, limitadas a um lado maior máximo de 1920 ou 3840 pixels, respectivamente, e arredondadas para um número par.
- `interpolation_model.interpolation_frame_rate` é obrigatório sempre que `interpolation_model` for `"apo-8"`.
- Arquivos muito grandes não são suportados no momento; os uploads são limitados a uma única parte; caso contrário, o nó gera um erro.
- Vários parâmetros (`sharp`, `realism`, `interpolation_slowmo`, `interpolation_duplicate`, `interpolation_duplicate_threshold`) são marcados como avançados na interface e podem ficar ocultos por padrão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo aprimorado após a aplicação dos filtros de upscaling e/ou interpolação selecionados. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `14627dc772a6a46a645517bd34b545e0986a84561e24bdfe810b67f791ee47e3`
