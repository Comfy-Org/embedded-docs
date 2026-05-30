> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/en.md)

## Visão Geral

Este nó converte uma única imagem 2D em um modelo 3D usando a API Tripo P1. Ele é otimizado para gerar malhas de baixa poligonização, prontas para uso em jogos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada para converter em um modelo 3D. |
| `output_mode` | DICT | Sim | Ver descrição | Um dicionário que especifica o modo de saída e as configurações de qualidade. Este parâmetro controla o tipo de modelo gerado e sua qualidade de textura. As opções disponíveis são definidas pela função auxiliar `_build_p1_output_mode` e incluem configurações para `texture_quality` (ex.: "standard", "high", "ultra") e `image_alignment`. |
| `enable_image_autofix` | BOOLEAN | Não | True<br>False | Pré-processa a imagem de entrada para melhor qualidade de geração. (padrão: False) |
| `face_limit` | INT | Não | - | Limita o número de faces na malha gerada. Um valor de -1 significa sem limite. (padrão: -1) |
| `model_seed` | INT | Não | - | Um valor de semente para geração reproduzível do modelo. Se não for fornecido, uma semente aleatória é usada. (padrão: None) |
| `auto_size` | BOOLEAN | Não | True<br>False | Determina automaticamente o tamanho ideal para o modelo gerado. (padrão: False) |
| `export_uv` | BOOLEAN | Não | True<br>False | Exporta coordenadas UV com o modelo. (padrão: True) |
| `compress_geometry` | BOOLEAN | Não | True<br>False | Comprime os dados geométricos para reduzir o tamanho do arquivo. (padrão: False) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | O caminho do arquivo para o modelo 3D gerado. Esta saída é fornecida apenas para compatibilidade com versões anteriores. |
| `model task_id` | MODEL_TASK_ID | O ID de tarefa único para a solicitação de geração do modelo. |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB. |

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
