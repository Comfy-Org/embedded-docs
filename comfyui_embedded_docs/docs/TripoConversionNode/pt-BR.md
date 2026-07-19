# Tripo: Converter modelo

O TripoConversionNode converte modelos 3D entre diferentes formatos de arquivo usando a API Tripo. Ele recebe um ID de tarefa de uma operação Tripo anterior (geração de modelo, rigging ou retargeting) e converte o modelo resultante para o formato desejado com várias opções de exportação.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `original_model_task_id` | O ID da tarefa de uma operação Tripo anterior (geração de modelo, rigging ou retargeting) | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Sim | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID |
| `formato` | O formato de arquivo de destino para o modelo 3D convertido | COMBO | Sim | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Se deve converter triângulos em quads (padrão: False) | BOOLEAN | Não | True/False |
| `limite_de_faces` | Número máximo de faces no modelo de saída, use -1 para sem limite (padrão: -1) | INT | Não | -1 a 2000000 |
| `tamanho_da_textura` | Tamanho das texturas de saída em pixels (padrão: 4096) | INT | Não | 128 a 4096 |
| `formato_da_textura` | Formato para texturas exportadas (padrão: JPEG) | COMBO | Não | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `forçar_simetria` | Se deve forçar simetria no modelo (padrão: False) | BOOLEAN | Não | True/False |
| `achatar_base` | Se deve achatar a parte inferior do modelo (padrão: False) | BOOLEAN | Não | True/False |
| `limite_achatamento_base` | Limiar para achatamento inferior (padrão: 0.0) | FLOAT | Não | 0.0 a 1.0 |
| `pivô_para_centro_base` | Se deve mover o ponto de pivô para o centro inferior do modelo (padrão: False) | BOOLEAN | Não | True/False |
| `fator_de_escala` | Fator de escala a ser aplicado ao modelo (padrão: 1.0) | FLOAT | Não | 0.0 e acima |
| `com_animação` | Se deve incluir dados de animação na exportação (padrão: False) | BOOLEAN | Não | True/False |
| `empacotar_uv` | Se deve empacotar coordenadas UV (padrão: False) | BOOLEAN | Não | True/False |
| `bake` | Se deve assar texturas (padrão: False) | BOOLEAN | Não | True/False |
| `nomes_das_partes` | Lista separada por vírgulas de nomes de partes a serem incluídas na exportação (padrão: "") | STRING | Não | Lista separada por vírgulas |
| `preset_fbx` | Predefinição de exportação FBX a ser usada (padrão: blender) | COMBO | Não | blender<br>mixamo<br>3dsmax |
| `exportar_cores_dos_vértices` | Se deve exportar cores de vértice (padrão: False) | BOOLEAN | Não | True/False |
| `exportar_orientação` | Modo de orientação de exportação (padrão: default) | COMBO | Não | align_image<br>default |
| `animar_no_local` | Se deve animar o modelo no lugar (padrão: False) | BOOLEAN | Não | True/False |

**Nota:** O `original_model_task_id` deve ser um ID de tarefa válido de uma operação Tripo anterior (geração de modelo, rigging ou retargeting). Parâmetros marcados como "avançados" são opcionais e só precisam ser configurados para requisitos específicos de exportação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| *Sem saídas nomeadas* | Este nó processa a conversão de forma assíncrona e retorna o resultado através do sistema da API Tripo | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
