# Inferência MoGe

Execute o MoGe em imagens para estimar profundidade e geometria. Este nó processa uma imagem de entrada através do modelo MoGe para gerar uma nuvem de pontos 3D, mapa de profundidade, intrínsecos da câmera, uma máscara e normais de superfície.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `moge_model` | O modelo MoGe a ser usado para inferência. | MOGE_MODEL | Sim | N/A |
| `image` | A imagem de entrada para estimativa de profundidade e geometria. Apenas os três primeiros canais de cor (RGB) são usados. | IMAGE | Sim | N/A |
| `resolution_level` | Controla a resolução de processamento. 0 = mais rápido, 9 = mais detalhe. (padrão: 9) | INT | Sim | 0 a 9 |
| `fov_x_degrees` | (Avançado) Campo de visão horizontal da câmera de origem. Define a distância focal usada para desprojetar o mapa de profundidade em 3D. 0 = recuperação automática a partir dos pontos previstos. (padrão: 0.0) | FLOAT | Sim | 0.0 a 170.0 (passo 0.1) |
| `batch_size` | Imagens por chamada de inferência. Reduza se você ficar sem memória (OOM) em um vídeo longo / conjunto de imagens. (padrão: 4) | INT | Sim | 1 a 64 |
| `force_projection` | (Avançado) Força a projeção dos pontos previstos. (padrão: True) | BOOLEAN | Sim | True/False |
| `apply_mask` | (Avançado) Define pixels mascarados (céu / inválidos) como inf em points e depth para que a geração de malha os descarte. Desative para manter a geometria bruta prevista em todos os lugares; a máscara ainda é retornada separadamente. (padrão: True) | BOOLEAN | Sim | True/False |
| `refine_steps` | (Avançado) Somente MoGe-3: passagens de refinamento volumétrico esparso sobre a profundidade prevista. Mais passagens aguçam detalhes finos e bordas com custo aproximadamente linear. 0 desativa o refinamento. Ignorado por MoGe-1 / MoGe-2. (padrão: 3) | INT | Sim | 0 a 8 |

Observação: Quando a `image` de entrada contém mais quadros do que `batch_size`, o nó os processa em várias chamadas de inferência e combina os resultados em uma única geometria de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `moge_geometry` | Um dicionário contendo a geometria estimada. Inclui a `image` original e pode conter `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `intrinsics` (matriz de intrínsecos da câmera), `mask` (máscara que identifica pixels válidos) e `normal` (normais de superfície). | MOGE_GEOMETRY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `10f3399d9b6bc4ff8a940c940f538a8ec8f38a15e7d65f162499c5ab264fad65`
