# Meshy: Texturizar modelo (múltiplas visualizações)

Este nó aplica textura a um modelo 3D criado anteriormente usando de 1 a 4 visualizações de referência do mesmo objeto. Você fornece o ID da tarefa do modelo original e as imagens de referência; o nó os envia para o serviço Meshy, aguarda a conclusão do trabalho e retorna o modelo com textura como arquivos GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA usado para o trabalho de texturização. Atualmente, apenas "meshy-7" está disponível. | COMBO | Sim | `"meshy-7"` |
| `meshy_task_id` | O ID da tarefa do modelo 3D criado anteriormente para ser texturizado. | MESHY_TASK_ID | Sim | — |
| `multiview_images` | Visualizações de referência do mesmo objeto. A primeira imagem é a visualização principal (frontal); a ordem das demais não importa. Slot expansível: conecte de 1 a 4 imagens (`image_1` a `image_4`). | IMAGE | Sim | 1 a 4 imagens |
| `enable_original_uv` | Usar a UV original do modelo em vez de gerar novas UVs. Quando ativado, o Meshy preserva as texturas existentes do modelo enviado. Se o modelo não tiver UV original, a qualidade da saída pode não ser tão boa. (padrão: True) | BOOLEAN | Não | True / False |
| `pbr` | Ativa a geração de textura PBR (renderização baseada em física). (padrão: False) | BOOLEAN | Não | True / False |
| `texture_resolution` | Resolução da textura de cor base. Resoluções maiores capturam mais detalhes da superfície. | COMBO | Sim | `"2k"`<br>`"4k"`<br>`"8k"` |

**Observação:** `multiview_images` deve conter entre 1 e 4 imagens. O nó valida isso em tempo de execução e gera um erro se a quantidade estiver fora desse intervalo. Se uma imagem conectada contiver um lote de várias imagens, cada imagem do lote conta para o limite. A primeira imagem é usada como visualização principal (frontal); a ordem das demais não importa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model_file` | Nome do arquivo do modelo. Esta saída é mantida apenas para compatibilidade com versões anteriores. | STRING |
| `meshy_task_id` | ID da tarefa do trabalho de texturização. | MESHY_TASK_ID |
| `GLB` | O modelo 3D texturizado baixado no formato GLB. | GLB |
| `FBX` | O modelo 3D texturizado baixado no formato FBX. | FBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`
