Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/en.md)

## Visão Geral

Execute o MoGe em uma única imagem para estimar profundidade e geometria. Este nó processa uma imagem de entrada através do modelo MoGe para gerar uma nuvem de pontos 3D, mapa de profundidade, parâmetros intrínsecos da câmera, uma máscara e normais de superfície.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `moge_model` | O modelo MoGe a ser usado para inferência. | MOGE_MODEL | Sim | N/A |
| `image` | A imagem de entrada para estimativa de profundidade e geometria. | IMAGE | Sim | N/A |
| `resolution_level` | Controla a resolução de processamento. 0 é o mais rápido, 9 fornece o maior nível de detalhe. (padrão: 9) | INT | Sim | 0 a 9 |
| `fov_x_degrees` | Campo de visão horizontal da câmera de origem em graus. Define a distância focal usada para reprojetar o mapa de profundidade em 3D. Defina como 0.0 para recuperar automaticamente o campo de visão a partir dos pontos previstos. (padrão: 0.0) | FLOAT | Sim | 0.0 a 170.0 |
| `batch_size` | Número de imagens processadas por chamada de inferência. Reduza este valor se ficar sem memória ao processar vídeos longos ou conjuntos grandes de imagens. (padrão: 4) | INT | Sim | 1 a 64 |
| `force_projection` | (Avançado) Força a projeção dos pontos previstos. (padrão: Verdadeiro) | BOOLEAN | Sim | Verdadeiro/Falso |
| `apply_mask` | Quando ativado, define pixels mascarados (céu ou inválidos) como infinito nas saídas de pontos e profundidade. Isso ajuda ferramentas de malhagem a ignorar essas áreas. Desative para manter a geometria bruta prevista em toda parte; a máscara ainda é retornada separadamente. (padrão: Verdadeiro) | BOOLEAN | Sim | Verdadeiro/Falso |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `moge_geometry` | Um dicionário contendo a geometria estimada. Inclui a `image` original e pode conter `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `intrinsics` (matriz de parâmetros intrínsecos da câmera), `mask` (máscara identificando pixels válidos) e `normal` (normais de superfície). | MOGE_GEOMETRY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5213b280513850eeef2e22ae723ebb015789109435e28ddd79f91f9a4b4a1e79`
