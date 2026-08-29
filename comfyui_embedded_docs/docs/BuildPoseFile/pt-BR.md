# Criar Arquivo de Animação 3D

Este nó cria um arquivo de animação 3D pronto para salvar a partir de dados de pose. Você pode exportar um GLB animado em vários estilos visuais — malha de corpo inteiro, pré-visualização apenas de articulações, esqueleto OpenPose ou rig de cápsulas SCAIL — ou salvar um clipe de captura de movimento BVH em vez disso. A saída se conecta a um nó de salvamento de arquivo, como o Save 3D Model, para gravar o arquivo em disco.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pose_data` | Dados de pose 3D. Aceita dados de pose MHR (parâmetros de modelo/formato/expressão, keypoints MHR70, cores canônicas, máscara de vértices das mãos) ou dados de pose Kimodo (rig externo com Y para cima, com vértices previstos por quadro e câmera). | MHR_POSE_DATA / KIMODO_POSE_DATA | Sim | — |
| `format` | Formato de saída; ambos os formatos alimentam o Save 3D Model para gravar em disco. 'glb' = GLB animado (malha / ossos / openpose / scail). 'bvh' = clipe de mocap BVH (um esqueleto; precisa do modelo corporal). (padrão: glb) | DYNAMIC_COMBO | Sim | "glb"<br>"bvh" |
| `sam3d_body_model` | Modelo corporal SAM3D opcional. Necessário para os formatos 'bvh', 'body_mesh' e 'bones_only', a menos que os dados de pose contenham uma substituição de esqueleto. | SAM3D_BODY_MODEL | Não | — |
| `fps` | Taxa de quadros da animação. (padrão: 24.0) | FLOAT | Sim | 1.0-240.0 |
| `camera_translation` | Grava `pred_cam_t` na translação da raiz: 'off' = posição de vínculo; 'centered' = delta em relação ao quadro 0; 'absolute' = bruto (Z é a profundidade da câmera — geralmente a distância em metros). (padrão: off) | COMBO | Sim | "off"<br>"centered"<br>"absolute" |
| `track_index` | Seleção de trilha: -1 = todas as trilhas; ≥0 = trilha única. (padrão: -1) | INT | Sim | -1 a 15 |

### Entradas do GLB

Estas entradas aparecem quando `format` está definido como "glb".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh_style` | Estilo visual do GLB: 'body_mesh' = Armature real (127 ossos, skinning, keyframes TRS, 72 morphs faciais; precisa do modelo corporal). 'bones_only' = primitivas em formato de osso em cada articulação (pré-visualização da armature). 'openpose' = esqueleto 3D OpenPose-18 a partir dos keypoints. 'scail' = rig de cápsulas SCAIL 3D (cilindros abertos com as extremidades tampadas por esferas de articulação). (padrão: body_mesh) | DYNAMIC_COMBO | Sim | "body_mesh"<br>"bones_only"<br>"openpose"<br>"scail" |
| `bone_smooth_window` | Janela de suavização gaussiana sobre keyframes de rotação por osso / trilhas de keypoints. 0 = desligado. 7-15 acalma giros/tremores onde o Smooth à montante deixa passar picos. (padrão: 0) | INT | Sim | 0-51, passo 2 |

#### Entradas do Body Mesh

Aparecem quando `mesh_style` é "body_mesh".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Forma de visualização dos ossos, com skinning rígido em cada articulação. 'off' = sem visualização de ossos; 'octahedrons' = ossos direcionais estilo Blender. (padrão: off) | DYNAMIC_COMBO | Sim | "off"<br>"octahedrons" |
| `bone_vis_radius_m` | Aparece quando `bone_vis` = "octahedrons". Raio em m (raio da esfera / meia largura do octaedro). (padrão: 0.02) | FLOAT | Sim | 0.005-0.5 |
| `bone_vis_color` | Aparece quando `bone_vis` = "octahedrons". Cores de vértice por osso (material sem iluminação). 'white' = nenhuma, 'rainbow_y' = gradiente jet da cabeça aos pés. (padrão: rainbow_y) | COMBO | Sim | "white"<br>"rainbow_y" |
| `shader` | Gravar cores por vértice que correspondem aos shaders do nó Render (COLOR_0 + KHR_materials_unlit). 'default' = sem cores. (padrão: default) | DYNAMIC_COMBO | Sim | "default"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic" |
| `rainbow_tilt_z` | Aparece quando `shader` é uma variante rainbow. Rotaciona o eixo do gradiente rainbow em torno de Z (para frente). Diferencia esquerda/direita. (padrão: -35.0) | FLOAT | Sim | -90.0 a 90.0 |
| `rainbow_tilt_x` | Aparece quando `shader` é uma variante rainbow. Rotaciona o eixo do gradiente rainbow em torno de X (direita). Diferencia frente/trás. (padrão: 0.0) | FLOAT | Sim | -90.0 a 90.0 |
| `person_palette_falloff` | Aparece quando `shader` é uma variante rainbow. Dessaturação por pessoa: cada trilha recebe uma mistura pastel de (1 - falloff^k). (padrão: 0.6) | FLOAT | Sim | 0.1-1.0 |

#### Entradas do Bones Only

Aparecem quando `mesh_style` é "bones_only".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Forma de visualização dos ossos, com skinning rígido em cada articulação. 'octahedrons' = ossos direcionais estilo Blender (articulação → filho primário). | DYNAMIC_COMBO | Sim | "octahedrons" |
| `bone_vis_radius_m` | Raio em m (raio da esfera / meia largura do octaedro). (padrão: 0.02) | FLOAT | Sim | 0.005-0.5 |
| `bone_vis_color` | Cores de vértice por osso (material sem iluminação). 'white' = nenhuma, 'rainbow_y' = gradiente jet da cabeça aos pés. (padrão: rainbow_y) | COMBO | Sim | "white"<br>"rainbow_y" |

#### Entradas do OpenPose

Aparecem quando `mesh_style` é "openpose".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_m` | Raio da esfera em m. (padrão: 0.010) | FLOAT | Sim | 0.005-0.1 |
| `stick_radius_m` | Meia largura do membro em m. Limitado automaticamente a `bone_length` × 0,1. (padrão: 0.008) | FLOAT | Sim | 0.002-0.05 |
| `include_hands` | Adicionar 21+21 mãos OpenPose (pulso + 5 dedos × 4 articulações, da base à ponta) originadas de pred_keypoints_3d. (padrão: False) | BOOLEAN | Sim | True / False |
| `hand_marker_radius_m` | Raio da esfera da mão em m. (padrão: 0.005) | FLOAT | Sim | 0.001-0.1 |
| `hand_stick_radius_m` | Meia largura do membro da mão em m. (padrão: 0.003) | FLOAT | Sim | 0.001-0.05 |
| `face_style` | Marcos de contorno facial amostrados de pred_vertices em IDs fixos de vértices da malha da cabeça (necessita de canonical_colors em pose_data). 'full' = todos os ~30 pontos; 'eyes_mouth' = olhos + lábios externos apenas. (padrão: disabled) | COMBO | Sim | "disabled"<br>"full"<br>"eyes_mouth" |
| `face_marker_radius_m` | Raio do ponto facial. 0 = automático = 0,3 × marker_radius_m. (padrão: 0.0) | FLOAT | Sim | 0.0-0.05 |

#### Entradas do SCAIL

Aparecem quando `mesh_style` é "scail".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `stick_radius_m` | Raio do cilindro em m. Ossos são cilindros abertos de raio constante; esferas de articulação (com tamanho automático para corresponder) tampam as extremidades abertas. Referência SCAIL = 0,0215 m. (padrão: 0.022) | FLOAT | Sim | 0.002-0.1 |
| `marker_radius_m` | Raio da esfera de articulação. 0 = automático = stick_radius_m (tampa rente). (padrão: 0.0) | FLOAT | Sim | 0.0-0.1 |
| `material_roughness` | Rugosidade PBR. Referência SCAIL = 0,3. 1 = fosco; 0 = cromado. (padrão: 0.3) | FLOAT | Sim | 0.0-1.0 |
| `include_hands` | Adicionar 21+21 keypoints de mãos + bastões de cápsula por trilha. (padrão: False) | BOOLEAN | Sim | True / False |
| `hand_marker_radius_m` | Raio da esfera da mão em m. (padrão: 0.005) | FLOAT | Sim | 0.001-0.05 |
| `hand_stick_radius_m` | Raio do cilindro da mão em m. (padrão: 0.003) | FLOAT | Sim | 0.001-0.05 |
| `face_style` | Marcos de contorno facial amostrados de pred_vertices (necessita de canonical_colors em pose_data). 'full' = todos os ~30 pontos; 'eyes_mouth' = olhos + lábios externos apenas. (padrão: disabled) | COMBO | Sim | "disabled"<br>"full"<br>"eyes_mouth" |

### Entradas do BVH

Aparecem quando `format` é "bvh".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `units` | Unidades de OFFSET/posição do BVH. 'cm' é o padrão de mocap. (padrão: cm) | COMBO | Sim | "cm"<br>"m" |

**Observações:**

- O formato `bvh` e os estilos de malha `body_mesh` e `bones_only` exigem a entrada `sam3d_body_model`, a menos que os próprios `pose_data` contenham uma substituição de esqueleto (um dicionário `_skeleton_override`, por exemplo, de um nó KimodoSample). O nó emite um erro se nenhum dos dois estiver disponível. Os estilos `openpose` e `scail` são independentes de rig e funcionam diretamente a partir dos keypoints, sem o modelo corporal.
- No formato `bvh`, a saída contém um único esqueleto. Quando `track_index` é -1 (todas as trilhas), a primeira trilha é usada.
- As opções `full` e `eyes_mouth` de `face_style` exigem `canonical_colors` nos dados de pose, o que está presente quando os dados de pose vêm do pipeline MHR juntamente com o modelo corporal.
- `bone_smooth_window` avança em passos de 2 entre 0 e 51.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_3d` | O arquivo de animação gerado: um GLB animado ou um clipe de mocap BVH, pronto para ser salvo em disco com um nó como o Save 3D Model. | 3D_FILE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildPoseFile/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f3672f0749c4f9affcc92da98198c5b142f6fcd9f5e317ab43dd7e53533c0fa3`
