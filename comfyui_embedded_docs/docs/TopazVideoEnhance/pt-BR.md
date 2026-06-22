# Topaz Video Enhance

O nó Topaz Video Enhance utiliza uma API externa para melhorar a qualidade do vídeo. Ele pode aumentar a resolução do vídeo, elevar a taxa de quadros por meio de interpolação e aplicar compressão. O nó processa um vídeo MP4 de entrada e retorna uma versão aprimorada com base nas configurações selecionadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vídeo` | O arquivo de vídeo de entrada a ser aprimorado. | VIDEO | Sim | - |
| `upscaler_enabled` | Ativa ou desativa o recurso de aumento de resolução do vídeo (padrão: True). | BOOLEAN | Sim | - |
| `upscaler_model` | O modelo de IA usado para aumentar a resolução do vídeo. | COMBO | Sim | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | A resolução alvo para o vídeo com resolução aumentada. | COMBO | Sim | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Nível de criatividade (aplica-se apenas ao Starlight (Astra) Creative). (padrão: "low") | COMBO | Não | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | Ativa ou desativa o recurso de interpolação de quadros (padrão: False). | BOOLEAN | Não | - |
| `interpolation_model` | O modelo usado para interpolação de quadros (padrão: "apo-8"). | COMBO | Não | `"apo-8"` |
| `interpolation_slowmo` | Fator de câmera lenta aplicado ao vídeo de entrada. Por exemplo, 2 faz com que a saída seja duas vezes mais lenta e dobre a duração. (padrão: 1) | INT | Não | 1 a 16 |
| `interpolation_frame_rate` | Taxa de quadros de saída. (padrão: 60) | INT | Não | 15 a 240 |
| `interpolation_duplicate` | Analisa a entrada em busca de quadros duplicados e os remove. (padrão: False) | BOOLEAN | Não | - |
| `interpolation_duplicate_threshold` | Sensibilidade de detecção para quadros duplicados. (padrão: 0,01) | FLOAT | Não | 0,001 a 0,1 |
| `dynamic_compression_level` | Nível CQP. (padrão: "Low") | COMBO | Não | `"Low"`<br>`"Mid"`<br>`"High"` |

**Observação:** Pelo menos um recurso de aprimoramento deve estar ativado. O nó gerará um erro se tanto `upscaler_enabled` quanto `interpolation_enabled` estiverem definidos como `False`. O vídeo de entrada deve estar no formato MP4.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `vídeo` | O arquivo de vídeo de saída aprimorado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
