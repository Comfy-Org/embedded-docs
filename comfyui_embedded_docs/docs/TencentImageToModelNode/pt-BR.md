Este nó utiliza a API Hunyuan3D Pro da Tencent para gerar um modelo 3D a partir de uma ou mais imagens de entrada. Ele processa as imagens, as envia para a API e retorna os arquivos do modelo 3D gerado nos formatos GLB e OBJ, juntamente com mapas de textura opcionais.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | A versão do modelo Hunyuan3D a ser utilizada. A opção LowPoly não está disponível para o modelo `3.1`. | COMBO | Sim | `"3.0"`<br>`"3.1"` |
| `imagem` | A imagem de entrada principal usada para gerar o modelo 3D. Deve ter pelo menos 128x128 pixels. | IMAGE | Sim | - |
| `imagem_esquerda` | Uma imagem opcional do lado esquerdo do objeto para geração multivista. Deve ter pelo menos 128x128 pixels. | IMAGE | Não | - |
| `imagem_direita` | Uma imagem opcional do lado direito do objeto para geração multivista. Deve ter pelo menos 128x128 pixels. | IMAGE | Não | - |
| `imagem_traseira` | Uma imagem opcional da parte traseira do objeto para geração multivista. Deve ter pelo menos 128x128 pixels. | IMAGE | Não | - |
| `número_de_faces` | O número alvo de faces para o modelo 3D gerado (padrão: 500000). | INT | Sim | 3000 - 1500000 |
| `tipo_de_geração` | O tipo de modelo 3D a ser gerado. Selecionar uma opção revela parâmetros adicionais relacionados. | DYNAMICCOMBO | Sim | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `generate_type.pbr` | Ativa a geração de materiais com Renderização Baseada em Física (PBR). Este parâmetro só fica visível quando `tipo_de_geração` está definido como "Normal" ou "LowPoly" (padrão: False). | BOOLEAN | Não | - |
| `generate_type.polygon_type` | O tipo de polígono a ser usado para a malha. Este parâmetro só fica visível quando `tipo_de_geração` está definido como "LowPoly". | COMBO | Não | `"triangle"`<br>`"quadrilateral"` |
| `semente` | Um valor de semente para o processo de geração. A semente controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 - 2147483647 |

**Nota:** Todas as imagens de entrada devem ter largura e altura mínimas de 128 pixels. As imagens são redimensionadas automaticamente se excederem 4900 pixels no lado mais longo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model_file` | Uma saída legada para compatibilidade com versões anteriores. | STRING |
| `GLB` | O modelo 3D gerado no formato de arquivo GLB (Formato de Transmissão GL Binário). | FILE3DGLB |
| `OBJ` | O modelo 3D gerado no formato de arquivo OBJ (Wavefront). | FILE3DOBJ |
| `texture_image` | A imagem de textura para o modelo 3D gerado. | IMAGE |
| `optional_metallic` | O mapa de metalicidade para materiais PBR. Retorna uma imagem preta se não estiver disponível. | IMAGE |
| `optional_normal` | O mapa normal para materiais PBR. Retorna uma imagem preta se não estiver disponível. | IMAGE |
| `optional_roughness` | O mapa de rugosidade para materiais PBR. Retorna uma imagem preta se não estiver disponível. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
