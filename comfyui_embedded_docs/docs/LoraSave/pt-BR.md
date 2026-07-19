# Extrair e Salvar Lora

O nó LoraSave extrai e salva arquivos LoRA (Adaptação de Baixo Posto) a partir de diferenças de modelos. Ele pode processar diferenças de modelos de difusão, diferenças de codificadores de texto ou ambos, convertendo-os no formato LoRA com posto e tipo especificados. O arquivo LoRA resultante é salvo no diretório de saída para uso posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `filename_prefix` | O prefixo para o nome do arquivo de saída (padrão: "loras/ComfyUI_extracted_lora") | STRING | Sim | - |
| `rank` | O valor do posto para o LoRA, controlando o tamanho e a complexidade (padrão: 8) | INT | Sim | 1-4096 |
| `lora_type` | O tipo de LoRA a ser criado (padrão: "standard") | COMBO | Sim | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` |
| `bias_diff` | Se deve incluir diferenças de viés no cálculo do LoRA (padrão: True) | BOOLEAN | Sim | - |
| `model_diff` | A saída do ModelSubtract a ser convertida em um lora | MODEL | Não | - |
| `text_encoder_diff` | A saída do CLIPSubtract a ser convertida em um lora | CLIP | Não | - |

**Nota:** Pelo menos um dos `model_diff` ou `text_encoder_diff` deve ser fornecido para o nó funcionar. Se ambos forem omitidos, o nó não produzirá saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| - | Este nó salva um arquivo LoRA no diretório de saída, mas não retorna nenhum dado através do fluxo de trabalho | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
