# Topaz Video Enhance

O nó Topaz Video Enhance dá nova vida a vídeos com poderosa tecnologia de upscaling e recuperação, usando uma API externa para melhorar a qualidade do vídeo. Ele pode aumentar a resolução do vídeo, aumentar a taxa de quadros por meio de interpolação e aplicar compressão. O nó processa um vídeo MP4 de entrada e retorna uma versão aprimorada com base nas configurações selecionadas. Este nó está marcado como obsoleto (legado).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `vídeo` | O arquivo de vídeo de entrada a ser aprimorado. | VIDEO | Sim | - |
| `upscaler_enabled` | Ativa ou desativa o recurso de upscaling de vídeo (padrão: True). | BOOLEAN | Sim | - |
| `upscaler_model` | O modelo de IA usado para fazer upscaling do vídeo. | COMBO | Sim | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | A resolução alvo para o vídeo com upscaling. | COMBO | Sim | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Nível de criatividade (aplica-se apenas ao Starlight (Astra) Creative). (padrão: "low") | COMBO | Não | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | Ativa ou desativa o recurso de interpolação de quadros (padrão: False). | BOOLEAN | Não | - |
| `interpolation_model` | O modelo usado para interpolação de quadros (padrão: "apo-8"). | COMBO | Não | `"apo-8"` |
| `interpolation_slowmo` | Fator de câmera lenta aplicado ao vídeo de entrada. Por exemplo, 2 torna a saída duas vezes mais lenta e dobra a duração. (padrão: 1) | INT | Não | 1 a 16 |
| `interpolation_frame_rate` | Taxa de quadros de saída. (padrão: 60) | INT | Não | 15 a 240 |
| `interpolation_duplicate` | Analisa a entrada em busca de quadros duplicados e os remove. (padrão: False) | BOOLEAN | Não | - |
| `interpolation_duplicate_threshold` | Sensibilidade de detecção de quadros duplicados. (padrão: 0.01) | FLOAT | Não | 0.001 a 0.1 |
| `dynamic_compression_level` | Nível CQP. (padrão: "Low") | COMBO | Não | `"Low"`<br>`"Mid"`<br>`"High"` |

**Nota:** Pelo menos um recurso de aprimoramento deve estar ativado. O nó gerará um erro se `upscaler_enabled` e `interpolation_enabled` estiverem definidos como False. O vídeo de entrada deve estar no formato MP4. A configuração `upscaler_creativity` se aplica somente quando `upscaler_model` estiver definido como "Starlight (Astra) Creative". Arquivos de vídeo muito grandes que exigem uploads em múltiplas partes não são suportados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo de saída aprimorado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b3b14a301b529256ddf04b7e3a9b99814ad5bfa149366b2a5c51c396dbffb190`
