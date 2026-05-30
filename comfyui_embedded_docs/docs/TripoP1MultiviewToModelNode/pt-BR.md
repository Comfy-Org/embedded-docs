> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/pt-BR.md)

## Visão Geral

Este nó gera um modelo 3D a partir de 2 a 4 imagens de referência de um objeto ou personagem. Você fornece imagens de diferentes ângulos (frente, esquerda, costas, direita), e o nó cria uma malha 3D no formato GLB. A vista frontal é obrigatória, e você pode adicionar opcionalmente qualquer combinação das outras três vistas para obter melhores resultados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | Vista frontal (0°). Obrigatória. |
| `image_left` | IMAGE | Não | - | Vista esquerda (90°), ou seja, o lado esquerdo do objeto. |
| `image_back` | IMAGE | Não | - | Vista traseira (180°). |
| `image_right` | IMAGE | Não | - | Vista direita (270°), ou seja, o lado direito do objeto. |
| `output_mode` | COMBO | Sim | `"geometry"`<br>`"textured"`<br>`"detailed"` | O modo de saída para o modelo gerado. `"geometry"` produz uma malha bruta, `"textured"` adiciona uma textura padrão e `"detailed"` cria um modelo texturizado de alto detalhe (padrão: `"textured"`). |
| `face_limit` | INT | Não | -1 a 100000 | Número máximo de faces para a malha de saída. Defina como -1 para sem limite (padrão: -1). |
| `model_seed` | INT | Não | 0 a 2147483647 | Semente para geração reproduzível do modelo. Defina como 0 para aleatório (padrão: 0). |
| `auto_size` | BOOLEAN | Não | True / False | Dimensiona automaticamente o modelo para caber dentro de uma caixa delimitadora padrão (padrão: False). |
| `export_uv` | BOOLEAN | Não | True / False | Exporta coordenadas UV com o modelo (padrão: True). |
| `compress_geometry` | BOOLEAN | Não | True / False | Comprime os dados de geometria para reduzir o tamanho do arquivo (padrão: False). |

**Nota:** Você deve fornecer pelo menos 2 imagens: a vista frontal (`image`) mais pelo menos uma das outras vistas (`image_left`, `image_back` ou `image_right`). Se menos de 2 imagens forem fornecidas, o nó gerará um erro.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model_file` | STRING | O nome do arquivo do modelo GLB gerado (apenas para compatibilidade reversa). |
| `model_task_id` | MODEL_TASK_ID | O ID único da tarefa para esta solicitação de geração de modelo. |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB. |

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
