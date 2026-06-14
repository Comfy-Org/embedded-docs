# Executar Depth Anything 3

Este nó executa o modelo Depth Anything 3 em uma imagem para estimar informações de profundidade e geometria. No modo multivisão, múltiplas imagens são processadas em conjunto como visões separadas da mesma cena para produzir mapas de profundidade geometricamente consistentes e poses de câmera.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `da3_model` | O modelo Depth Anything 3 a ser usado para inferência | DA3_MODEL | Sim | - |
| `image` | Imagem ou imagens de entrada para processar | IMAGE | Sim | - |
| `resolution` | Resolução na qual o modelo opera (lado mais longo, múltiplo de 14). Valores menores são mais rápidos e usam menos VRAM. Valores maiores produzem mais detalhes. A saída é redimensionada de volta ao tamanho original (padrão: 504) | INT | Sim | 140 a 2520 (passo: 14) |
| `resize_method` | upper_bound_resize: redimensiona para que o lado mais longo seja igual à resolução (limita memória, padrão). lower_bound_resize: redimensiona para que o lado mais curto seja igual à resolução (preserva mais detalhes em imagens altas/largas, usa mais memória) | COMBO | Sim | `"upper_bound_resize"`<br>`"lower_bound_resize"` |
| `mode` | mono: processamento de imagem de visão única (funciona com qualquer variante do modelo). multiview: todas as imagens processadas em conjunto para consistência geométrica e estimativa de pose de câmera (apenas para modelos Small e Base) | COMBO | Sim | `"mono"`<br>`"multiview"` |
| `ref_view_strategy` | Qual visão atua como âncora geométrica no modo multivisão. saddle_balanced: a visão mais média entre todas as outras (melhor escolha geral). saddle_sim_range: a visão mais visualmente distinta das demais. first / middle: seleções posicionais fixas | COMBO | Não (condicional) | `"saddle_balanced"`<br>`"saddle_sim_range"`<br>`"first"`<br>`"middle"` |
| `pose_method` | Como o campo de visão da câmera é estimado (apenas para modelos Small e Base). cam_dec: aprendido a partir das características da imagem. ray_pose: derivado geometricamente da saída de raios 3D do modelo. Afeta a correção de perspectiva da saída 3D | COMBO | Não (condicional) | `"cam_dec"`<br>`"ray_pose"` |

**Observações sobre restrições de parâmetros:**
- Os parâmetros `ref_view_strategy` e `pose_method` estão disponíveis apenas quando `mode` está definido como `"multiview"`
- O modo multivisão requer uma variante de modelo Small ou Base. Modelos com outros tipos de cabeçote (como Metric ou Mono) não suportam atenção entre visões ou estimativa de pose de câmera
- Quando `pose_method` está definido como `"cam_dec"`, o modelo deve ter um decodificador de câmera. Se definido como `"ray_pose"`, o modelo deve ter um cabeçote DualDPT
- Se o `pose_method` selecionado não for compatível com o modelo carregado, um erro será gerado

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `da3_geometry` | Dicionário de tensores não normalizados. Sempre contém as chaves: depth, image, mode. Chaves opcionais incluem: sky (para modelos Mono/Metric), confidence (para modelos Small/Base), extrinsics e intrinsics (para modo multivisão) | DA3_GEOMETRY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Inference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e91dd47e6a01719cdd6b6ce8a9bcc45933cac72c5e147ac42906d2f83ab7c250`
