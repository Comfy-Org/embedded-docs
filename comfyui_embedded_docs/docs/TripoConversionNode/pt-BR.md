# Tripo: Converter modelo

This node converts an existing Tripo 3D model into another 3D file format. It takes the task ID of a model previously created or processed by a Tripo operation (such as model generation, rigging, retargeting, or segmentation), submits a conversion task to the Tripo API, waits for that task to finish, and then returns the converted model file.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | ID da tarefa do modelo Tripo a ser convertido. Deve vir de uma tarefa anterior de geração de modelo, rigging, retargeting ou segmentação do Tripo. Se o ID estiver ausente ou vazio, o nó gera um erro. | STRING | Sim | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `formato` | Formato de arquivo de destino para o modelo 3D convertido. | COMBO | Sim | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Converte triângulos em quads quando habilitado (padrão: False). | BOOLEAN | Não | True or False |
| `limite_de_faces` | Número máximo de faces no modelo convertido. Defina como -1 para não haver limite (padrão: -1). | INT | Não | -1 a 2000000 |
| `tamanho_da_textura` | Resolução das texturas de saída em pixels (padrão: 4096). | INT | Não | 128 a 8192 |
| `formato_da_textura` | Formato de arquivo usado para as texturas exportadas (padrão: JPEG). | COMBO | Não | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `forçar_simetria` | Força o modelo a ser simétrico quando habilitado (padrão: False). | BOOLEAN | Não | True or False |
| `achatar_base` | Achata a base do modelo quando habilitado (padrão: False). | BOOLEAN | Não | True or False |
| `limite_achatamento_base` | Profundidade de achatamento usada com `flatten_bottom` (padrão: 0.01). Este valor só é aplicado quando `flatten_bottom` está habilitado. | FLOAT | Não | 0.01 a 1.0 |
| `pivô_para_centro_base` | Move o ponto de pivô para a base central do modelo quando habilitado (padrão: False). | BOOLEAN | Não | True or False |
| `fator_de_escala` | Fator de escala aplicado ao modelo convertido (padrão: 1.0). | FLOAT | Não | 0.01 and above |
| `com_animação` | Mantém o esqueleto e a animação de modelos com rigging ou retargeting (padrão: True). | BOOLEAN | Não | True or False |
| `empacotar_uv` | Reempacota as coordenadas UV quando habilitado (padrão: False). | BOOLEAN | Não | True or False |
| `bake` | Aplica materiais avançados nas texturas base para maior compatibilidade (padrão: True). | BOOLEAN | Não | True or False |
| `nomes_das_partes` | Lista de nomes de partes do modelo separados por vírgula a serem enviados para a conversão. Entradas vazias são ignoradas e nomes duplicados são removidos. Deixe vazio para omitir esta opção (padrão: vazio). | STRING | Não | Comma-separated list of part names |
| `preset_fbx` | Predefinição de compatibilidade do FBX. bake_scale aplica a transformação de escala na geometria (padrão: blender). | COMBO | Não | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `exportar_cores_dos_vértices` | Exporta as cores dos vértices quando habilitado (padrão: False). | BOOLEAN | Não | True or False |
| `exportar_orientação` | Eixo frontal do modelo exportado. default mantém o +x do Tripo (padrão: default). | COMBO | Não | default<br>+x<br>-x<br>+y<br>-y |
| `animar_no_local` | Anima o modelo no local quando habilitado (padrão: False). | BOOLEAN | Não | True or False |

**Nota:** Exceto por `original_model_task_id` e `format`, todas as entradas são configurações avançadas opcionais. A maioria das configurações deixadas em seus valores padrão é omitida da solicitação de conversão para que a API do Tripo possa usar seu comportamento padrão. As opções `with_animation` e `bake` são sempre enviadas. `flatten_bottom_threshold` só é aplicado quando `flatten_bottom` está habilitado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_3d` | Modelo convertido no formato solicitado. O OBJ é entregue pelo Tripo como um arquivo ZIP (malha, material e texturas). | FILE_3D |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`
