# Tripo P1: Multivisual para Modelo

## Visão Geral

Este nó gera um modelo 3D a partir de 2 a 4 imagens de referência de um objeto ou personagem. Você fornece imagens de diferentes ângulos (frente, esquerda, costas, direita), e o nó cria uma malha 3D no formato GLB. A vista frontal é obrigatória, e você pode adicionar opcionalmente qualquer combinação das outras três vistas para obter melhores resultados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | Vista frontal (0°). Obrigatória. | IMAGE | Sim | - |
| `imagem_esquerda` | Vista esquerda (90°), ou seja, o lado esquerdo do objeto. | IMAGE | Não | - |
| `imagem_traseira` | Vista traseira (180°). | IMAGE | Não | - |
| `imagem_direita` | Vista direita (270°), ou seja, o lado direito do objeto. | IMAGE | Não | - |
| `modo_de_saida` | O modo de saída para o modelo gerado. `"geometry"` produz uma malha bruta, `"textured"` adiciona uma textura padrão e `"detailed"` cria um modelo texturizado de alto detalhe (padrão: `"textured"`). | COMBO | Sim | `"geometry"`<br>`"textured"`<br>`"detailed"` |
| `limite_de_faces` | Número máximo de faces para a malha de saída. Defina como -1 para sem limite (padrão: -1). | INT | Não | -1 a 100000 |
| `semente_do_modelo` | Semente para geração reproduzível do modelo. Defina como 0 para aleatório (padrão: 0). | INT | Não | 0 a 2147483647 |
| `tamanho_automático` | Dimensiona automaticamente o modelo para caber dentro de uma caixa delimitadora padrão (padrão: False). | BOOLEAN | Não | True / False |
| `exportar_uv` | Exporta coordenadas UV com o modelo (padrão: True). | BOOLEAN | Não | True / False |
| `comprimir_geometria` | Comprime os dados de geometria para reduzir o tamanho do arquivo (padrão: False). | BOOLEAN | Não | True / False |

**Nota:** Você deve fornecer pelo menos 2 imagens: a vista frontal (`image`) mais pelo menos uma das outras vistas (`image_left`, `image_back` ou `image_right`). Se menos de 2 imagens forem fornecidas, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model_file` | O nome do arquivo do modelo GLB gerado (apenas para compatibilidade reversa). | STRING |
| `model_task_id` | O ID único da tarefa para esta solicitação de geração de modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
