# Inferência MoGe

Execute o MoGe em uma única imagem para estimar profundidade e geometria. Este nó processa uma imagem de entrada por meio do modelo MoGe para gerar uma nuvem de pontos 3D, um mapa de profundidade, parâmetros intrínsecos da câmera, uma máscara e normais de superfície.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `moge_model` | O modelo MoGe a ser usado para inferência. | MOGE_MODEL | Sim | N/A |
| `image` | A imagem de entrada para estimativa de profundidade e geometria. Apenas os três primeiros canais de cor (RGB) são usados. | IMAGE | Sim | N/A |
| `resolution_level` | Controla a resolução de processamento. 0 é o mais rápido, 9 fornece o maior nível de detalhe. (padrão: 9) | INT | Sim | 0 a 9 |
| `fov_x_degrees` | (Avançado) Campo de visão horizontal da câmera de origem em graus. Define a distância focal usada para desprojetar o mapa de profundidade em 3D. Defina como 0.0 para recuperar automaticamente o campo de visão a partir dos pontos previstos. (padrão: 0.0) | FLOAT | Sim | 0.0 a 170.0 |
| `batch_size` | Imagens por chamada de inferência. Reduza este valor se você ficar sem memória em um vídeo longo ou conjunto de imagens. (padrão: 4) | INT | Sim | 1 a 64 |
| `force_projection` | (Avançado) Força a projeção dos pontos previstos. (padrão: True) | BOOLEAN | Sim | True/False |
| `apply_mask` | (Avançado) Define pixels mascarados (céu ou inválidos) como infinito nas saídas de pontos e profundidade para que ferramentas de malha possam ignorá-los. Desative para manter a geometria bruta prevista em todos os lugares; a máscara ainda é retornada separadamente. (padrão: True) | BOOLEAN | Sim | True/False |

Nota: Quando a `image` de entrada contém mais quadros do que `batch_size`, o nó os processa em múltiplas chamadas de inferência e combina os resultados em uma única geometria de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `moge_geometry` | Um dicionário contendo a geometria estimada. Inclui a `image` original e pode conter `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `intrinsics` (matriz de parâmetros intrínsecos da câmera), `mask` (máscara que identifica pixels válidos) e `normal` (normais de superfície). | MOGE_GEOMETRY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
