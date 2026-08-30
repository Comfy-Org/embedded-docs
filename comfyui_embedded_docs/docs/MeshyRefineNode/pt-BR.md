# Meshy: Refinar Modelo Rascunho

O nó Meshy: Refine Draft Model recebe um modelo 3D de rascunho de uma tarefa Meshy anterior e o melhora, adicionando opcionalmente texturas usando um prompt de texto ou uma imagem de referência. Ele envia o trabalho de refinamento para a API Meshy e retorna o modelo finalizado como arquivos GLB e FBX assim que a tarefa estiver concluída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo de IA usado para refinar o modelo de rascunho. | COMBO | Sim | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | O ID exclusivo da tarefa do modelo de rascunho que você deseja refinar. | MESHY_TASK_ID | Sim | - |
| `habilitar_pbr` | Gera Mapas PBR (metálico, rugosidade, normal) além da cor base. Nota: isso deve ser definido como falso ao usar o estilo Sculpture, pois o estilo Sculpture gera seu próprio conjunto de mapas PBR. (padrão: False) | BOOLEAN | Sim | - |
| `prompt_de_textura` | Forneça um prompt de texto para orientar o processo de texturização. Máximo de 600 caracteres. Não pode ser usado ao mesmo tempo que `texture_image`. (padrão: string vazia) | STRING | Sim | - |
| `imagem_de_textura` | Apenas um de `texture_image` ou `texture_prompt` pode ser usado ao mesmo tempo. | IMAGE | Não | - |
| `texture_resolution` | Resolução da textura da cor base. Resoluções mais altas capturam mais detalhes de superfície. | COMBO | Sim | `"2k"`<br>`"4k"`<br>`"8k"` |

**Nota:** As entradas `texture_prompt` e `texture_image` são mutuamente exclusivas. Você não pode fornecer ao mesmo tempo um prompt de texto e uma imagem para a texturização na mesma operação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | O nome do arquivo do modelo GLB gerado. (Somente para compatibilidade com versões anteriores) | STRING |
| `meshy_task_id` | O ID exclusivo da tarefa para o trabalho de refinamento enviado. | MESHY_TASK_ID |
| `GLB` | O modelo 3D refinado final no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D refinado final no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `73c9d712c4fd9fdd2792600ce874916ce9447d386407353c886f624641fa0e0f`
