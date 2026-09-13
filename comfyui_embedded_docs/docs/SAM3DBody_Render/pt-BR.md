# Renderizar Pose de Corpo 3D

Renderiza dados de pose corporal 3D em uma imagem usando um estilo selecionável. O nó aceita dados de pose do rastreador corporal SAM3D (MHR) ou de um rig Y-up externo, como Kimodo, e pode compor o resultado sobre uma imagem de fundo opcional (ou um canvas preto quando nenhum é fornecido). Os estilos de renderização disponíveis incluem uma malha 3D sombreada, uma silhueta binária, esqueletos no estilo OpenPose 2D e 3D e cápsulas corporais no estilo SCAIL.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `render_style` | Modo de renderização. 'mesh' = malha MHR 3D rasterizada através da câmera. 'silhouette' = máscara binária da malha. 'openpose_2d' = esqueleto 2D plano. 'openpose_3d' = esqueleto OpenPose como modelo 3D com sombreamento plano. 'scail' = cápsulas 3D SCAIL. (padrão: "mesh") | DYNAMIC_COMBO | Sim | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | Dados de pose MHR, ou dados de pose de rig Y-up externo (KimodoSample). Todos os estilos de renderização funcionam para rigs externos que carregam mapas de articulações OpenPose em seu `_skeleton_override` (KimodoSample faz isso). | MHR_POSE_DATA ou KIMODO_POSE_DATA | Sim | — |
| `background` | Fundo por quadro. Omitido = canvas preto. | IMAGE | Não | — |
| `width` | Largura de saída em pixels. 0 = usar o image_size nativo dos dados de pose. Se apenas um entre width/height for definido, o outro será derivado preservando a proporção original. (padrão: 0) | INT | Não | 0 a 16384, passo 8 |
| `height` | Altura de saída em pixels. 0 = usar o image_size nativo dos dados de pose. Se apenas um entre width/height for definido, o outro será derivado preservando a proporção original. (padrão: 0) | INT | Não | 0 a 16384, passo 8 |
| `camera_info` | Substituição de câmera 6DOF livre. Quando conectada, a pose é reprojetada através desta câmera (posição/alvo/zoom/rotação/FoV) em vez da prevista. | LOAD_3D_CAMERA | Não | — |

### Entradas de malha

Estes parâmetros aparecem quando `render_style` é "mesh".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `shader` | Shader predefinido. 'normals' = normal da superfície atual no espaço da câmera (convenção de normal map do OpenGL Y+: +X→R, +Y→G, +Z→B). 'rainbow' = jet body-Y no estilo RealisDance; as variantes 'rainbow_face_*' substituem os vértices da face por cores de normal/por região; 'depth' = cinza linear. (padrão: "default") | DYNAMIC_COMBO | Não | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Rotaciona o eixo do jet rainbow em torno de Z (para frente). Diferencia esquerda/direita. Disponível apenas quando `shader` é "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic". (padrão: -35.0) | FLOAT | Não | -90.0 a 90.0, passo 0.5 |
| `rainbow_tilt_x` | Rotaciona o eixo do jet rainbow em torno de X (para a direita). Diferencia frente/trás. Disponível apenas quando `shader` é "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic". (padrão: 0.0) | FLOAT | Não | -90.0 a 90.0, passo 0.5 |
| `opacity` | Alfa da malha sobre a imagem de fundo, ou sobre preto quando nenhuma está conectada. (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0, passo 0.01 |
| `person_palette_falloff` | Dessaturação por pessoa em direção ao branco: a track k recebe uma mistura pastel (1 - falloff^k) (o 'segundo personagem mais suave' do SCAIL). 1.0 = desativado. (padrão: 0.6) | FLOAT | Não | 0.1 a 1.0, passo 0.05 |
| `region` | 'hands_only' filtra faces por meio do `hand_vert_mask` pré-computado (pesos LBS contra KPs canônicos da mão) — isola a malha da mão para depuração. Recorre à malha completa se a máscara estiver ausente. (padrão: "full_body") | COMBO | Não | "full_body"<br>"hands_only" |

### Entradas de silhueta

Quando `render_style` é "silhouette", o nó renderiza uma máscara binária da malha 3D. Este modo não tem parâmetros adicionais.

### Entradas do OpenPose 2D

Estes parâmetros aparecem quando `render_style` é "openpose_2d".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `marker_radius_px` | Raio do ponto de keypoint corporal (px). (padrão: 4) | INT | Não | 1 a 32, passo 1 |
| `stick_width_px` | Meia-largura da elipse do membro corporal (px). Padrão do DWPose = 4. (padrão: 4) | INT | Não | 1 a 32, passo 1 |
| `limb_alpha` | Alfa por membro. Padrão do DWPose = 0.6. (padrão: 0.6) | FLOAT | Não | 0.0 a 1.0, passo 0.05 |
| `face_style` | 'full' = todos os landmarks faciais (sapiens-238 se presente, senão fallback do rig ~30). 'eyes_mouth' = subconjunto do fallback do rig (~12 pontos: apenas olhos + lábios externos). 'disabled' = sem pontos faciais. (padrão: "disabled") | COMBO | Não | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | Desenha 21+21 keypoints de mão + sticks. 'disabled' = sem mãos. 'dwpose' = pontos azul sólido; 'openpose' = pontos rainbow. (padrão: "disabled") | COMBO | Não | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Dessaturação por pessoa: a track k se mistura com branco por 1 - falloff^k. A track 0 permanece vívida; 1.0 desativa o falloff. (padrão: 0.6) | FLOAT | Não | 0.1 a 1.0, passo 0.05 |

### Entradas do OpenPose 3D

Estes parâmetros aparecem quando `render_style` é "openpose_3d".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `radius_m` | Raio da cápsula do membro em metros (fino = semelhante a um bastão). (padrão: 0.015) | FLOAT | Não | 0.004 a 0.1, passo 0.001 |
| `include_hands` | Desenha 21+21 keypoints de mão como cápsulas 3D. (padrão: True) | BOOLEAN | Não | True ou False |
| `person_palette_falloff` | Dessaturação por pessoa: a track k se mistura com branco por 1 - falloff^k. A track 0 permanece vívida; 1.0 desativa o falloff. (padrão: 0.6) | FLOAT | Não | 0.1 a 1.0, passo 0.05 |

### Entradas do SCAIL

Estes parâmetros aparecem quando `render_style` é "scail".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `radius_m` | Raio da cápsula em metros (referência SCAIL: ~0.022 m). (padrão: 0.022) | FLOAT | Não | 0.005 a 0.2, passo 0.001 |
| `hand_style` | Compõe mãos OpenPose 2D sobre o corpo de cápsulas 3D (corresponde ao SCAIL — sem cápsulas de mão 3D). 'disabled' = sem mãos. 'dwpose' = pontos de mão azul sólido; 'openpose' = pontos rainbow. Os sticks permanecem rainbow por dedo de qualquer forma. (padrão: "dwpose") | COMBO | Não | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = todos os landmarks faciais (sapiens-238 se presente, senão fallback do rig ~30). 'eyes_mouth' = subconjunto do fallback do rig (~12 pontos: apenas olhos + lábios externos). 'disabled' = sem pontos faciais. (padrão: "disabled") | COMBO | Não | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Dessaturação por pessoa: a track k se mistura com branco por 1 - falloff^k. A track 0 permanece vívida; 1.0 desativa o falloff. (padrão: 0.6) | FLOAT | Não | 0.1 a 1.0, passo 0.05 |

### Notas

- Se ambos `width` e `height` forem 0, a saída usa o tamanho de imagem nativo dos dados de pose. Se apenas um deles for definido, o outro será derivado preservando a proporção original. Um `background` conectado é redimensionado para corresponder à resolução da renderização.
- Quando `camera_info` está conectado, a pose é reprojetada através dessa câmera em vez da prevista.
- No modo mesh, `rainbow_tilt_z` e `rainbow_tilt_x` estão disponíveis apenas quando `shader` está definido como "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic".
- No modo mesh, quando `region` é "hands_only", o filtro de região da mão exige que os dados de pose contenham uma máscara de vértices da mão; se a máscara estiver ausente, a malha completa é renderizada em vez disso.
- No modo scail, as mãos são desenhadas como sobreposições OpenPose 2D sobre o corpo de cápsulas 3D, em vez de cápsulas 3D; definir `hand_style` como "disabled" as remove completamente.
- Quando a resolução de saída difere da resolução nativa dos dados de pose, os tamanhos do marcador e do stick do openpose_2d são escalados proporcionalmente.
- Se o fundo tiver menos quadros que os dados de pose, o último quadro do fundo será reutilizado para os quadros restantes.
- A saída contém um quadro para cada quadro de pose de entrada. Se os dados de pose não contiverem quadros, uma única imagem preta será retornada.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `image` | Os quadros renderizados: os dados de pose desenhados no estilo de renderização selecionado, compostos sobre o fundo quando um está conectado, ou sobre preto caso contrário. Um quadro para cada quadro de pose de entrada, retornado como uma única imagem em lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/pt-BR.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`
