> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/pt-BR.md)

O TripoConversionNode converte modelos 3D entre diferentes formatos de arquivo usando a API Tripo. Ele recebe um ID de tarefa de uma operação Tripo anterior (geração de modelo, rigging ou retargeting) e converte o modelo resultante para o formato desejado com várias opções de exportação.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Sim | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | O ID da tarefa de uma operação Tripo anterior (geração de modelo, rigging ou retargeting) |
| `format` | COMBO | Sim | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | O formato de arquivo de destino para o modelo 3D convertido |
| `quad` | BOOLEAN | Não | True/False | Se deve converter triângulos em quads (padrão: False) |
| `face_limit` | INT | Não | -1 a 2000000 | Número máximo de faces no modelo de saída, use -1 para sem limite (padrão: -1) |
| `texture_size` | INT | Não | 128 a 4096 | Tamanho das texturas de saída em pixels (padrão: 4096) |
| `texture_format` | COMBO | Não | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Formato para texturas exportadas (padrão: JPEG) |
| `force_symmetry` | BOOLEAN | Não | True/False | Se deve forçar simetria no modelo (padrão: False) |
| `flatten_bottom` | BOOLEAN | Não | True/False | Se deve achatar a parte inferior do modelo (padrão: False) |
| `flatten_bottom_threshold` | FLOAT | Não | 0.0 a 1.0 | Limiar para achatamento inferior (padrão: 0.0) |
| `pivot_to_center_bottom` | BOOLEAN | Não | True/False | Se deve mover o ponto de pivô para o centro inferior do modelo (padrão: False) |
| `scale_factor` | FLOAT | Não | 0.0 e acima | Fator de escala a ser aplicado ao modelo (padrão: 1.0) |
| `with_animation` | BOOLEAN | Não | True/False | Se deve incluir dados de animação na exportação (padrão: False) |
| `pack_uv` | BOOLEAN | Não | True/False | Se deve empacotar coordenadas UV (padrão: False) |
| `bake` | BOOLEAN | Não | True/False | Se deve assar texturas (padrão: False) |
| `part_names` | STRING | Não | Lista separada por vírgulas | Lista separada por vírgulas de nomes de partes a serem incluídas na exportação (padrão: "") |
| `fbx_preset` | COMBO | Não | blender<br>mixamo<br>3dsmax | Predefinição de exportação FBX a ser usada (padrão: blender) |
| `export_vertex_colors` | BOOLEAN | Não | True/False | Se deve exportar cores de vértice (padrão: False) |
| `export_orientation` | COMBO | Não | align_image<br>default | Modo de orientação de exportação (padrão: default) |
| `animate_in_place` | BOOLEAN | Não | True/False | Se deve animar o modelo no lugar (padrão: False) |

**Nota:** O `original_model_task_id` deve ser um ID de tarefa válido de uma operação Tripo anterior (geração de modelo, rigging ou retargeting). Parâmetros marcados como "avançados" são opcionais e só precisam ser configurados para requisitos específicos de exportação.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| *Sem saídas nomeadas* | - | Este nó processa a conversão de forma assíncrona e retorna o resultado através do sistema da API Tripo |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
