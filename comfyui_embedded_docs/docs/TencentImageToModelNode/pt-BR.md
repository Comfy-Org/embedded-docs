> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/pt-BR.md)

Este nó utiliza a API Hunyuan3D Pro da Tencent para gerar um modelo 3D a partir de uma ou mais imagens de entrada. Ele processa as imagens, as envia para a API e retorna os arquivos do modelo 3D gerado nos formatos GLB e OBJ, juntamente com mapas de textura opcionais.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | `"3.0"`<br>`"3.1"` | A versão do modelo Hunyuan3D a ser utilizada. A opção LowPoly não está disponível para o modelo `3.1`. |
| `imagem` | IMAGE | Sim | - | A imagem de entrada principal usada para gerar o modelo 3D. Deve ter pelo menos 128x128 pixels. |
| `imagem_esquerda` | IMAGE | Não | - | Uma imagem opcional do lado esquerdo do objeto para geração multivista. Deve ter pelo menos 128x128 pixels. |
| `imagem_direita` | IMAGE | Não | - | Uma imagem opcional do lado direito do objeto para geração multivista. Deve ter pelo menos 128x128 pixels. |
| `imagem_traseira` | IMAGE | Não | - | Uma imagem opcional da parte traseira do objeto para geração multivista. Deve ter pelo menos 128x128 pixels. |
| `número_de_faces` | INT | Sim | 3000 - 1500000 | O número alvo de faces para o modelo 3D gerado (padrão: 500000). |
| `tipo_de_geração` | DYNAMICCOMBO | Sim | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | O tipo de modelo 3D a ser gerado. Selecionar uma opção revela parâmetros adicionais relacionados. |
| `generate_type.pbr` | BOOLEAN | Não | - | Ativa a geração de materiais com Renderização Baseada em Física (PBR). Este parâmetro só fica visível quando `tipo_de_geração` está definido como "Normal" ou "LowPoly" (padrão: False). |
| `generate_type.polygon_type` | COMBO | Não | `"triangle"`<br>`"quadrilateral"` | O tipo de polígono a ser usado para a malha. Este parâmetro só fica visível quando `tipo_de_geração` está definido como "LowPoly". |
| `semente` | INT | Sim | 0 - 2147483647 | Um valor de semente para o processo de geração. A semente controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da semente (padrão: 0). |

**Nota:** Todas as imagens de entrada devem ter largura e altura mínimas de 128 pixels. As imagens são redimensionadas automaticamente se excederem 4900 pixels no lado mais longo.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model_file` | STRING | Uma saída legada para compatibilidade com versões anteriores. |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato de arquivo GLB (Formato de Transmissão GL Binário). |
| `OBJ` | FILE3DOBJ | O modelo 3D gerado no formato de arquivo OBJ (Wavefront). |
| `texture_image` | IMAGE | A imagem de textura para o modelo 3D gerado. |
| `optional_metallic` | IMAGE | O mapa de metalicidade para materiais PBR. Retorna uma imagem preta se não estiver disponível. |
| `optional_normal` | IMAGE | O mapa normal para materiais PBR. Retorna uma imagem preta se não estiver disponível. |
| `optional_roughness` | IMAGE | O mapa de rugosidade para materiais PBR. Retorna uma imagem preta se não estiver disponível. |

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
