O nó "Meshy: Refinar Modelo Bruto" recebe um modelo 3D bruto gerado anteriormente e melhora sua qualidade, adicionando texturas opcionalmente. Ele envia uma tarefa de refinamento para a API do Meshy e retorna os arquivos finais do modelo 3D assim que o processamento for concluído.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica o modelo de IA a ser usado para refinamento. Atualmente, apenas o modelo "latest" está disponível. | COMBO | Sim | `"latest"` |
| `meshy_task_id` | O ID de tarefa único do modelo bruto que você deseja refinar. | MESHY_TASK_ID | Sim | - |
| `habilitar_pbr` | Gera mapas PBR (metálico, rugosidade, normal) além da cor base. Nota: deve ser definido como falso ao usar o estilo Escultura, pois o estilo Escultura gera seu próprio conjunto de mapas PBR. (padrão: `Falso`) | BOOLEANO | Não | - |
| `prompt_de_textura` | Forneça um prompt de texto para orientar o processo de texturização. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `imagem_de_textura`. (padrão: string vazia) | STRING | Não | - |
| `imagem_de_textura` | Apenas um dos parâmetros `imagem_de_textura` ou `prompt_de_textura` pode ser usado por vez. | IMAGEM | Não | - |

**Nota:** As entradas `texture_prompt` e `texture_image` são mutuamente exclusivas. Você não pode fornecer um prompt de texto e uma imagem para texturização na mesma operação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O nome do arquivo do modelo GLB gerado. (Apenas para compatibilidade com versões anteriores) | STRING |
| `meshy_task_id` | O ID de tarefa único para o trabalho de refinamento enviado. | MESHY_TASK_ID |
| `GLB` | O modelo 3D final refinado no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D final refinado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
