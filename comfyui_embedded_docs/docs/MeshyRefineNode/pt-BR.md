> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/pt-BR.md)

O nó "Meshy: Refinar Modelo Bruto" recebe um modelo 3D bruto gerado anteriormente e melhora sua qualidade, adicionando texturas opcionalmente. Ele envia uma tarefa de refinamento para a API do Meshy e retorna os arquivos finais do modelo 3D assim que o processamento for concluído.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `model` | COMBO | Sim | `"latest"` | Especifica o modelo de IA a ser usado para refinamento. Atualmente, apenas o modelo "latest" está disponível. |
| `meshy_task_id` | MESHY_TASK_ID | Sim | - | O ID de tarefa único do modelo bruto que você deseja refinar. |
| `enable_pbr` | BOOLEANO | Não | - | Gera mapas PBR (metálico, rugosidade, normal) além da cor base. Nota: deve ser definido como falso ao usar o estilo Escultura, pois o estilo Escultura gera seu próprio conjunto de mapas PBR. (padrão: `Falso`) |
| `texture_prompt` | STRING | Não | - | Forneça um prompt de texto para orientar o processo de texturização. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `texture_image`. (padrão: string vazia) |
| `texture_image` | IMAGEM | Não | - | Apenas um dos parâmetros `texture_image` ou `texture_prompt` pode ser usado por vez. |

**Nota:** As entradas `texture_prompt` e `texture_image` são mutuamente exclusivas. Você não pode fornecer um prompt de texto e uma imagem para texturização na mesma operação.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | O nome do arquivo do modelo GLB gerado. (Apenas para compatibilidade com versões anteriores) |
| `meshy_task_id` | MESHY_TASK_ID | O ID de tarefa único para o trabalho de refinamento enviado. |
| `GLB` | FILE3DGLB | O modelo 3D final refinado no formato GLB. |
| `FBX` | FILE3DFBX | O modelo 3D final refinado no formato FBX. |

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
