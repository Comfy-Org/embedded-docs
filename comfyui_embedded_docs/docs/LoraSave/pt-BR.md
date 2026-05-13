> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/pt-BR.md)

O nó LoraSave extrai e salva arquivos LoRA (Adaptação de Baixo Posto) a partir de diferenças de modelos. Ele pode processar diferenças de modelos de difusão, diferenças de codificadores de texto ou ambos, convertendo-os no formato LoRA com posto e tipo especificados. O arquivo LoRA resultante é salvo no diretório de saída para uso posterior.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `filename_prefix` | STRING | Sim | - | O prefixo para o nome do arquivo de saída (padrão: "loras/ComfyUI_extracted_lora") |
| `rank` | INT | Sim | 1-4096 | O valor do posto para o LoRA, controlando o tamanho e a complexidade (padrão: 8) |
| `lora_type` | COMBO | Sim | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` | O tipo de LoRA a ser criado (padrão: "standard") |
| `bias_diff` | BOOLEAN | Sim | - | Se deve incluir diferenças de viés no cálculo do LoRA (padrão: True) |
| `model_diff` | MODEL | Não | - | A saída do ModelSubtract a ser convertida em um lora |
| `text_encoder_diff` | CLIP | Não | - | A saída do CLIPSubtract a ser convertida em um lora |

**Nota:** Pelo menos um dos `model_diff` ou `text_encoder_diff` deve ser fornecido para o nó funcionar. Se ambos forem omitidos, o nó não produzirá saída.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| - | - | Este nó salva um arquivo LoRA no diretório de saída, mas não retorna nenhum dado através do fluxo de trabalho |

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
