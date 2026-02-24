> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/pt-BR.md)

O nó Topaz Video Enhance utiliza uma API externa para melhorar a qualidade de vídeo. Ele pode aumentar a resolução do vídeo (upscale), incrementar a taxa de quadros por meio de interpolação e aplicar compressão. O nó processa um vídeo de entrada no formato MP4 e retorna uma versão aprimorada com base nas configurações selecionadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | - | O arquivo de vídeo de entrada a ser aprimorado. |
| `upscaler_enabled` | BOOLEAN | Sim | - | Ativa ou desativa o recurso de aumento de resolução do vídeo (padrão: Verdadeiro). |
| `upscaler_model` | COMBO | Sim | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | O modelo de IA utilizado para aumentar a resolução do vídeo. |
| `upscaler_resolution` | COMBO | Sim | `"FullHD (1080p)"`<br>`"4K (2160p)"` | A resolução de destino para o vídeo com resolução aumentada. |
| `upscaler_creativity` | COMBO | Não | `"low"`<br>`"middle"`<br>`"high"` | Nível de criatividade (aplica-se apenas ao Starlight (Astra) Creative). (padrão: "low") |
| `interpolation_enabled` | BOOLEAN | Não | - | Ativa ou desativa o recurso de interpolação de quadros (padrão: Falso). |
| `interpolation_model` | COMBO | Não | `"apo-8"` | O modelo utilizado para interpolação de quadros (padrão: "apo-8"). |
| `interpolation_slowmo` | INT | Não | 1 a 16 | Fator de câmera lenta aplicado ao vídeo de entrada. Por exemplo, 2 torna a saída duas vezes mais lenta e dobra a duração. (padrão: 1) |
| `interpolation_frame_rate` | INT | Não | 15 a 240 | Taxa de quadros de saída. (padrão: 60) |
| `interpolation_duplicate` | BOOLEAN | Não | - | Analisa a entrada em busca de quadros duplicados e os remove. (padrão: Falso) |
| `interpolation_duplicate_threshold` | FLOAT | Não | 0.001 a 0.1 | Sensibilidade de detecção para quadros duplicados. (padrão: 0.01) |
| `dynamic_compression_level` | COMBO | Não | `"Low"`<br>`"Mid"`<br>`"High"` | Nível CQP. (padrão: "Low") |

**Observação:** Pelo menos um recurso de aprimoramento deve estar ativado. O nó gerará um erro se tanto `upscaler_enabled` quanto `interpolation_enabled` estiverem definidos como `False`. O vídeo de entrada deve estar no formato MP4.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O arquivo de vídeo de saída aprimorado. |
