# Executar Predição de Corpo SAM3D

SAM3D Body Prediction executa estimativa de pose corporal e de mãos em 3D em imagens de entrada, detectando uma ou mais pessoas por quadro. Dados de rastreamento ou caixas delimitadoras podem ser fornecidos para melhorar a detecção; quando nenhum deles é fornecido, o nó recorre à detecção de pessoa única em quadro completo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | O modelo de corpo SAM3D a ser usado para a predição. | SAM3D_BODY_MODEL | Sim | — |
| `image` | Imagem ou lote de imagens para executar a predição de corpo. | IMAGE | Sim | — |
| `track_data` | Dados de rastreamento do SAM3 Video Track, necessários para a detecção de múltiplas pessoas. | SAM3_TRACK_DATA | Não | — |
| `bboxes` | Caixas delimitadoras por quadro usadas para melhorar a detecção. Podem ser usadas como alternativa aos dados de rastreamento. | BBOX | Não | — |
| `run_hand_refinement` | Melhora a pose das mãos ao custo de tempo de inferência e uso de memória adicionais. Padrão: true. | BOOLEAN | Não | true<br>false |
| `fov` | FoV vertical em graus. Afeta a profundidade prevista e a escala absoluta. 0 = recorre a ~53° (16:9). Padrão: 0.0. | FLOAT | Não | 0.0 ou maior |
| `batch_size` | Número máximo de recortes de pessoas para processar como um lote. Valores maiores usam mais VRAM para inferência mais rápida. Padrão: 64. | INT | Não | 1 a 512 |

Nota: quando `track_data` é fornecido, ele tem precedência sobre `bboxes`. Se nem `track_data` nem `bboxes` forem fornecidos, o nó recorre à detecção de pessoa única em quadro completo. Caixas delimitadoras podem ser fornecidas para um único quadro (aplicadas a todos os quadros) ou por quadro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mhr_pose_data` | Pacote de dados de pose corporal contendo resultados de detecção de pose por quadro, geometria facial, tamanho da imagem de entrada, cores canônicas de vértices e uma máscara de vértices das mãos. | MHR_POSE_DATA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Predict/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f1039349cd2809423053bffde1c7d119c7c42f217327d23c608b1224d183770e`
