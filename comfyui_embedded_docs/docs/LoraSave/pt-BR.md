> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/pt-BR.md)

O nó LoraSave extrai e salva arquivos LoRA (Low-Rank Adaptation) a partir de diferenças entre modelos. Ele pode processar diferenças do modelo de difusão, diferenças do codificador de texto ou ambos, convertendo-os para o formato LoRA com um *rank* e tipo especificados. O arquivo LoRA resultante é salvo no diretório de saída para uso posterior.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `filename_prefix` | STRING | Sim | - | O prefixo para o nome do arquivo de saída (padrão: "loras/ComfyUI_extracted_lora") |
| `rank` | INT | Sim | 1-4096 | O valor de *rank* para o LoRA, controlando o tamanho e a complexidade (padrão: 8) |
| `lora_type` | COMBO | Sim | Múltiplas opções disponíveis | O tipo de LoRA a ser criado, com várias opções disponíveis |
| `bias_diff` | BOOLEAN | Sim | - | Se deve incluir diferenças de *bias* no cálculo do LoRA (padrão: True) |
| `model_diff` | MODEL | Não | - | A saída de ModelSubtract a ser convertida em um LoRA |
| `text_encoder_diff` | CLIP | Não | - | A saída de CLIPSubtract a ser convertida em um LoRA |

**Observação:** Pelo menos uma das entradas `model_diff` ou `text_encoder_diff` deve ser fornecida para o nó funcionar. Se ambas forem omitidas, o nó não produzirá nenhuma saída.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| - | - | Este nó salva um arquivo LoRA no diretório de saída, mas não retorna nenhum dado através do fluxo de trabalho |
