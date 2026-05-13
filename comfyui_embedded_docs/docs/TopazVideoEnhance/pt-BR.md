> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/pt-BR.md)

O nó Topaz Video Enhance utiliza uma API externa para melhorar a qualidade do vídeo. Ele pode aumentar a resolução do vídeo, elevar a taxa de quadros por meio de interpolação e aplicar compressão. O nó processa um vídeo MP4 de entrada e retorna uma versão aprimorada com base nas configurações selecionadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `vídeo` | VIDEO | Sim | - | O arquivo de vídeo de entrada a ser aprimorado. |
| `upscaler_enabled` | BOOLEAN | Sim | - | Ativa ou desativa o recurso de aumento de resolução do vídeo (padrão: True). |
| `upscaler_model` | COMBO | Sim | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` | O modelo de IA usado para aumentar a resolução do vídeo. |
| `upscaler_resolution` | COMBO | Sim | `"FullHD (1080p)"`<br>`"4K (2160p)"` | A resolução alvo para o vídeo com resolução aumentada. |
| `upscaler_creativity` | COMBO | Não | `"low"`<br>`"middle"`<br>`"high"` | Nível de criatividade (aplica-se apenas ao Starlight (Astra) Creative). (padrão: "low") |
| `interpolation_enabled` | BOOLEAN | Não | - | Ativa ou desativa o recurso de interpolação de quadros (padrão: False). |
| `interpolation_model` | COMBO | Não | `"apo-8"` | O modelo usado para interpolação de quadros (padrão: "apo-8"). |
| `interpolation_slowmo` | INT | Não | 1 a 16 | Fator de câmera lenta aplicado ao vídeo de entrada. Por exemplo, 2 faz com que a saída seja duas vezes mais lenta e dobre a duração. (padrão: 1) |
| `interpolation_frame_rate` | INT | Não | 15 a 240 | Taxa de quadros de saída. (padrão: 60) |
| `interpolation_duplicate` | BOOLEAN | Não | - | Analisa a entrada em busca de quadros duplicados e os remove. (padrão: False) |
| `interpolation_duplicate_threshold` | FLOAT | Não | 0,001 a 0,1 | Sensibilidade de detecção para quadros duplicados. (padrão: 0,01) |
| `dynamic_compression_level` | COMBO | Não | `"Low"`<br>`"Mid"`<br>`"High"` | Nível CQP. (padrão: "Low") |

**Observação:** Pelo menos um recurso de aprimoramento deve estar ativado. O nó gerará um erro se tanto `upscaler_enabled` quanto `interpolation_enabled` estiverem definidos como `False`. O vídeo de entrada deve estar no formato MP4.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `vídeo` | VIDEO | O arquivo de vídeo de saída aprimorado. |

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
