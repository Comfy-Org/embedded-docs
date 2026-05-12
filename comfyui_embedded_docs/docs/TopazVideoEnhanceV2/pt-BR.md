> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/pt-BR.md)

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/en.md)

# Topaz Video Enhance V2

O nó **Topaz Video Enhance V2** permite aumentar a resolução e aprimorar vídeos usando os modelos de IA da Topaz Labs. Ele pode aumentar a resolução, ajustar a taxa de quadros por meio de interpolação e aplicar aprimoramentos criativos ou realistas para dar nova vida aos seus arquivos de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `video` | VIDEO | Sim | - | O vídeo de entrada a ser processado. Deve estar no formato de contêiner MP4. |
| `upscaler_model` | COMBO | Sim | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Desabilitado"` | O modelo de IA usado para aumentar a resolução do vídeo. Selecionar "Desabilitado" significa que nenhum aumento de resolução será aplicado. |
| `upscaler_model.upscaler_resolution` | COMBO | Condicional | `"FullHD (1080p)"`<br>`"4K (2160p)"` | A resolução de saída desejada para o upscaler. Este parâmetro é obrigatório quando um modelo de upscaler é selecionado (não "Desabilitado"). |
| `upscaler_model.creativity` | FLOAT | Condicional | 0.0 a 1.0 (passo 0.1) | Intensidade criativa do aumento de resolução. Disponível apenas para os modelos "Astra 2" e "Starlight (Astra) Creative". Padrão: 0.5 para Astra 2, "baixo" para Starlight Creative. |
| `upscaler_model.prompt` | STRING | Não | - | Prompt de cena descritivo (não instrutivo) opcional. Disponível apenas para o modelo "Astra 2". Limitado a 500 quadros de entrada (~15s a 30fps) quando definido. Padrão: vazio. |
| `upscaler_model.sharp` | FLOAT | Não | 0.0 a 1.0 (passo 0.01) | Nitidez de pré-aprimoramento: 0.0=desfoque Gaussiano, 0.5=passagem direta (padrão), 1.0=nitidez USM. Disponível apenas para o modelo "Astra 2". Padrão: 0.5. |
| `upscaler_model.realism` | FLOAT | Não | 0.0 a 1.0 (passo 0.01) | Direciona a saída para o realismo fotográfico. Mantenha em 0 para o padrão do modelo. Disponível apenas para o modelo "Astra 2". Padrão: 0.0. |
| `interpolation_model` | COMBO | Sim | `"Desabilitado"`<br>`"apo-8"` | O modelo de IA usado para interpolação de quadros. Selecionar "Desabilitado" significa que nenhuma interpolação será aplicada. |
| `interpolation_model.interpolation_frame_rate` | INT | Condicional | 15 a 240 | Taxa de quadros de saída. Obrigatório quando o modelo de interpolação é "apo-8". Padrão: 60. |
| `interpolation_model.interpolation_slowmo` | INT | Não | 1 a 16 | Fator de câmera lenta aplicado ao vídeo de entrada. Por exemplo, 2 faz a saída ser duas vezes mais lenta e dobra a duração. Padrão: 1. |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | Não | Verdadeiro/Falso | Analisa a entrada em busca de quadros duplicados e os remove. Padrão: Falso. |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | Não | 0.001 a 0.1 (passo 0.001) | Sensibilidade de detecção para quadros duplicados. Padrão: 0.01. |
| `dynamic_compression_level` | COMBO | Não | `"Baixo"`<br>`"Médio"`<br>`"Alto"` | Nível CQP para compressão de vídeo. Padrão: "Baixo". |

**Restrições Importantes:**
- Pelo menos um dos parâmetros `upscaler_model` ou `interpolation_model` deve estar habilitado (não "Desabilitado"), caso contrário, um erro será gerado.
- O vídeo de entrada deve estar no formato de contêiner MP4.
- O modelo "Astra 2" com um prompt é limitado a 500 quadros de entrada (~15 segundos a 30fps). Sem um prompt, é limitado a um número maior de quadros.
- Quando `upscaler_model` não é "Desabilitado", o subparâmetro `upscaler_resolution` é obrigatório.
- Quando `interpolation_model` não é "Desabilitado", o subparâmetro `interpolation_frame_rate` é obrigatório.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `video` | VIDEO | A saída de vídeo aprimorada após aplicar os filtros de aumento de resolução e/ou interpolação selecionados. |