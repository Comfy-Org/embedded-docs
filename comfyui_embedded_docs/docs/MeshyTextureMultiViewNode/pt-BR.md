# Meshy: Texturizar modelo (múltiplas visualizações)

Este nó texturiza um modelo 3D criado anteriormente usando de 1 a 4 vistas de referência do mesmo objeto. Você fornece o ID da tarefa do modelo original e as imagens de referência; o nó as envia ao serviço Meshy, aguarda a conclusão do trabalho e retorna o modelo texturizado como arquivos GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA usado para o trabalho de texturização. Apenas "meshy-7" está disponível no momento. | COMBO | Sim | `"meshy-7"` |
| `meshy_task_id` | O ID da tarefa do modelo 3D criado anteriormente a ser texturizado. | MESHY_TASK_ID | Sim | — |
| `multiview_images` | Vistas de referência do mesmo objeto. A primeira imagem é a vista principal (frontal); a ordem das imagens restantes não importa. Slot expansível: conecte de 1 a 4 imagens (`image_1` a `image_4`). | IMAGE | Sim | 1 a 4 imagens |
| `enable_original_uv` | Usa a UV original do modelo em vez de gerar novas UVs. Quando habilitado, o Meshy preserva as texturas existentes do modelo enviado. Se o modelo não tiver UV original, a qualidade da saída pode não ser tão boa. (padrão: True; opção avançada) | BOOLEAN | Não | True / False |
| `pbr` | Habilita a geração de texturas PBR (renderização baseada em física). (padrão: False; opção avançada) | BOOLEAN | Não | True / False |
| `texture_resolution` | Resolução da textura de cor base. Resoluções mais altas capturam mais detalhes da superfície. | COMBO | Sim | `"2k"`<br>`"4k"`<br>`"8k"` |

**Nota:** `multiview_images` deve conter entre 1 e 4 imagens. O nó valida isso em tempo de execução e lança um erro se a contagem estiver fora desse intervalo. Se uma imagem conectada contiver um lote de várias imagens, cada imagem do lote conta para o limite. A primeira imagem é usada como a vista principal (frontal); a ordem das imagens restantes não importa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | Nome do arquivo do modelo. Esta saída é mantida apenas para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | ID da tarefa do trabalho de texturização. | MESHY_TASK_ID |
| `GLB` | O modelo 3D texturizado baixado no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D texturizado baixado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`
