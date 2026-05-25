> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/en.md)

## Visão Geral

Execute o MoGe em uma única imagem para estimar profundidade e geometria. Este nó processa uma imagem de entrada através do modelo MoGe para gerar uma nuvem de pontos 3D, mapa de profundidade, parâmetros intrínsecos da câmera, uma máscara e normais de superfície.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `moge_model` | MOGE_MODEL | Sim | N/A | O modelo MoGe a ser usado para inferência. |
| `image` | IMAGE | Sim | N/A | A imagem de entrada para estimativa de profundidade e geometria. |
| `resolution_level` | INT | Sim | 0 a 9 | Controla a resolução de processamento. 0 é o mais rápido, 9 fornece o maior nível de detalhe. (padrão: 9) |
| `fov_x_degrees` | FLOAT | Sim | 0.0 a 170.0 | Campo de visão horizontal da câmera de origem em graus. Define a distância focal usada para reprojetar o mapa de profundidade em 3D. Defina como 0.0 para recuperar automaticamente o campo de visão a partir dos pontos previstos. (padrão: 0.0) |
| `batch_size` | INT | Sim | 1 a 64 | Número de imagens processadas por chamada de inferência. Reduza este valor se ficar sem memória ao processar vídeos longos ou conjuntos grandes de imagens. (padrão: 4) |
| `force_projection` | BOOLEAN | Sim | Verdadeiro/Falso | (Avançado) Força a projeção dos pontos previstos. (padrão: Verdadeiro) |
| `apply_mask` | BOOLEAN | Sim | Verdadeiro/Falso | Quando ativado, define pixels mascarados (céu ou inválidos) como infinito nas saídas de pontos e profundidade. Isso ajuda ferramentas de malhagem a ignorar essas áreas. Desative para manter a geometria bruta prevista em toda parte; a máscara ainda é retornada separadamente. (padrão: Verdadeiro) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `moge_geometry` | MOGE_GEOMETRY | Um dicionário contendo a geometria estimada. Inclui a `image` original e pode conter `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `intrinsics` (matriz de parâmetros intrínsecos da câmera), `mask` (máscara identificando pixels válidos) e `normal` (normais de superfície). |

---
**Source fingerprint (SHA-256):** `5213b280513850eeef2e22ae723ebb015789109435e28ddd79f91f9a4b4a1e79`
