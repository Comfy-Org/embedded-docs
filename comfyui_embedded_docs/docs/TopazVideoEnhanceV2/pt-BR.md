Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/en.md)

# Topaz Video Enhance V2

O nó **Topaz Video Enhance V2** permite aumentar a resolução e aprimorar vídeos usando os modelos de IA da Topaz Labs. Ele pode aumentar a resolução, ajustar a taxa de quadros por meio de interpolação e aplicar aprimoramentos criativos ou realistas para dar nova vida aos seus arquivos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo de entrada a ser processado. Deve estar no formato de contêiner MP4. | VIDEO | Sim | - |
| `modelo de upscaling` | O modelo de IA usado para aumentar a resolução do vídeo. Selecionar "Desabilitado" significa que nenhum aumento de resolução será aplicado. | COMBO | Sim | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Desabilitado"` |
| `upscaler_model.upscaler_resolution` | A resolução de saída alvo para o upscaler. Este parâmetro é obrigatório quando um modelo de upscaler é selecionado (não "Desabilitado"). | COMBO | Condicional | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Força criativa do aumento de resolução. Disponível apenas para os modelos "Astra 2" e "Starlight (Astra) Creative". Para Astra 2, é um controle deslizante (padrão: 0.5). Para Starlight Creative, é uma combinação (padrão: "baixa"). | FLOAT / COMBO | Condicional | Astra 2: 0.0 a 1.0 (passo 0.1)<br>Starlight Creative: `"baixa"`<br>`"média"`<br>`"alta"` |
| `upscaler_model.prompt` | Prompt de cena descritivo (não instrutivo) opcional. Disponível apenas para o modelo "Astra 2". Limitado a 500 quadros de entrada (~15s a 30fps) quando definido. Padrão: vazio. | STRING | Não | - |
| `upscaler_model.sharp` | Nitidez de pré-aprimoramento: 0.0=desfoque gaussiano, 0.5=passagem direta (padrão), 1.0=nitidez USM. Disponível apenas para o modelo "Astra 2". Padrão: 0.5. | FLOAT | Não | 0.0 a 1.0 (passo 0.01) |
| `upscaler_model.realism` | Direciona a saída para o realismo fotográfico. Deixe em 0 para o padrão do modelo. Disponível apenas para o modelo "Astra 2". Padrão: 0.0. | FLOAT | Não | 0.0 a 1.0 (passo 0.01) |
| `modelo de interpolação` | O modelo de IA usado para interpolação de quadros. Selecionar "Desabilitado" significa que nenhuma interpolação será aplicada. | COMBO | Sim | `"Desabilitado"`<br>`"apo-8"` |
| `interpolation_model.interpolation_frame_rate` | Taxa de quadros de saída. Obrigatório quando o modelo de interpolação é "apo-8". Padrão: 60. | INT | Condicional | 15 a 240 |
| `interpolation_model.interpolation_slowmo` | Fator de câmera lenta aplicado ao vídeo de entrada. Por exemplo, 2 torna a saída duas vezes mais lenta e dobra a duração. Padrão: 1. | INT | Não | 1 a 16 |
| `interpolation_model.interpolation_duplicate` | Analisar a entrada em busca de quadros duplicados e removê-los. Padrão: Falso. | BOOLEAN | Não | Verdadeiro/Falso |
| `interpolation_model.interpolation_duplicate_threshold` | Sensibilidade de detecção para quadros duplicados. Padrão: 0.01. | FLOAT | Não | 0.001 a 0.1 (passo 0.001) |
| `nível de compressão dinâmica` | Nível CQP para compressão de vídeo. Padrão: "Baixo". | COMBO | Não | `"Baixo"`<br>`"Médio"`<br>`"Alto"` |

**Restrições Importantes:**
- Pelo menos um dos parâmetros `upscaler_model` ou `interpolation_model` deve estar habilitado (não "Desabilitado"), caso contrário, um erro será gerado.
- O vídeo de entrada deve estar no formato de contêiner MP4.
- O modelo "Astra 2" com um prompt é limitado a 500 quadros de entrada (~15 segundos a 30fps). Sem um prompt, é limitado a um número maior de quadros.
- Quando `upscaler_model` não é "Desabilitado", o subparâmetro `upscaler_resolution` é obrigatório.
- Quando `interpolation_model` não é "Desabilitado", o subparâmetro `interpolation_frame_rate` é obrigatório.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `vídeo` | A saída de vídeo aprimorada após aplicar os filtros de aumento de resolução e/ou interpolação selecionados. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `29b7538206327c35866126c1862c1d1ccea872ba84fbb9c84126114a06e2b00f`
