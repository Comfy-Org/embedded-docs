# Tripo P1: Imagem para Modelo

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/en.md)

## Visão Geral

Este nó converte uma única imagem 2D em um modelo 3D usando a API Tripo P1. Ele é otimizado para gerar malhas de baixa poligonização, prontas para uso em jogos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada para converter em um modelo 3D. | IMAGE | Sim | - |
| `modo_de_saida` | Um dicionário que especifica o modo de saída e as configurações de qualidade. Este parâmetro controla o tipo de modelo gerado e sua qualidade de textura. As opções disponíveis são definidas pela função auxiliar `_build_p1_output_mode` e incluem configurações para `texture_quality` (ex.: "standard", "high", "ultra") e `image_alignment`. | DICT | Sim | Ver descrição |
| `habilitar_autoajuste_imagem` | Pré-processa a imagem de entrada para melhor qualidade de geração. (padrão: False) | BOOLEAN | Não | True<br>False |
| `limite_de_faces` | Limita o número de faces na malha gerada. Um valor de -1 significa sem limite. (padrão: -1) | INT | Não | - |
| `semente_do_modelo` | Um valor de semente para geração reproduzível do modelo. Se não for fornecido, uma semente aleatória é usada. (padrão: None) | INT | Não | - |
| `tamanho_automático` | Determina automaticamente o tamanho ideal para o modelo gerado. (padrão: False) | BOOLEAN | Não | True<br>False |
| `exportar_uv` | Exporta coordenadas UV com o modelo. (padrão: True) | BOOLEAN | Não | True<br>False |
| `comprimir_geometria` | Comprime os dados geométricos para reduzir o tamanho do arquivo. (padrão: False) | BOOLEAN | Não | True<br>False |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O caminho do arquivo para o modelo 3D gerado. Esta saída é fornecida apenas para compatibilidade com versões anteriores. | STRING |
| `model task_id` | O ID de tarefa único para a solicitação de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
