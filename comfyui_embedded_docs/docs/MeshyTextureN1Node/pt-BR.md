# Meshy: Texture Model (N1)

Este nó texturiza um modelo 3D criado anteriormente com o modelo de texturização Meshy N1, usando de 1 a 4 vistas de referência do mesmo objeto. Conecte o ID da tarefa do modelo original e as vistas; o nó as envia ao Meshy, aguarda a conclusão do trabalho e retorna o modelo texturizado como arquivos GLB e FBX junto com o novo ID da tarefa.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA usado para o trabalho de texturização. Apenas `"meshy-n1"` está disponível no momento. | COMBO | Sim | `"meshy-n1"` |
| `meshy_task_id` | ID da tarefa do modelo 3D criado anteriormente que deve ser texturizado. | MESHY_TASK_ID, STRING | Sim | N/A |
| `front_view` | A vista que o Meshy trata como frontal. Uma imagem texturiza a frente e deixa a parte de trás sem textura; adicione vistas traseira e laterais em `extra_views` para uma traseira fiel. | IMAGE | Sim | Imagem única |
| `vistas_extras` | Outras vistas do mesmo objeto, em qualquer ordem. Slot expansível: conecte de 0 a 3 imagens (`view_1` ... `view_3`). Junto com `front_view`, no máximo 4 imagens. | IMAGE | Não | 0 a 3 imagens |
| `enable_original_uv` | Usar o UV original do modelo em vez de gerar novos UVs. Quando ativado, o Meshy preserva as texturas existentes do modelo enviado. Se o modelo não tiver UV original, a qualidade da saída pode não ser tão boa. (padrão: True; opção avançada) | BOOLEAN | Não | True / False |

**Nota:** `front_view` e `extra_views` podem conter no máximo 4 imagens juntas; o nó gera um erro quando mais imagens são conectadas. Se uma imagem conectada carregar um lote, cada imagem do lote conta para esse limite. A resolução da textura é fixada em 2K e nenhum mapa PBR é gerado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `meshy_task_id` | ID da tarefa do trabalho de texturização, utilizável por nós Meshy posteriores. | MESHY_TASK_ID, STRING |
| `GLB` | O modelo 3D texturizado baixado no formato GLB. | FILE3DGLB |
| `FBX` | O modelo 3D texturizado baixado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/pt-BR.md)

---
**Source fingerprint (SHA-256):** `be4191fd091839cfdce82b4f41fc6ae9e70f7b5b5504eb14a3c0d741d25ac8fd`
