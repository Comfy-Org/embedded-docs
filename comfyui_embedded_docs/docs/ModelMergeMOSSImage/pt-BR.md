# ModelMergeMOSSImage

O nó ModelMergeMOSSImage mescla dois modelos de imagem MOSS combinando seus pesos correspondentes bloco a bloco, de modo que uma parte do resultado possa vir de um modelo base e o restante de um ajuste fino ou de um segundo modelo. Cada componente principal da arquitetura tem sua própria proporção: o embedder de vídeo, o embedder de texto, o embedding de tempo, a modulação compartilhada do bloco, todas as 42 camadas transformer e as cabeças de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado. Tudo o que não vier do segundo modelo é mantido deste modelo | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado. Seus pesos são misturados conforme as proporções abaixo | MODEL | Sim | - |
| `video_embedder.` | Proporção de mistura para o bloco do embedder de vídeo (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `text_embedder.proj.` | Proporção de mistura para a camada de projeção do embedder de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `text_embedder.blocks.0.` e `text_embedder.blocks.1.` | Proporção de mistura para cada um dos dois blocos do embedder de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `time_embedding.` | Proporção de mistura para o bloco de embedding de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `shared_block_modulation.` | Proporção de mistura para a camada de modulação compartilhada usada pelos blocos transformer (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `layers.0.` até `layers.41.` | Proporção de mistura para cada uma das 42 camadas transformer (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `final_norm_video.` | Proporção de mistura para a normalização final do fluxo de vídeo (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `final_linear_video.` | Proporção de mistura para a camada linear final do fluxo de vídeo (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `video_head_modulation.` | Proporção de mistura para a camada de modulação da cabeça de saída de vídeo (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

Uma proporção de 0.0 mantém esse componente como está em `model1`; uma proporção de 1.0 o obtém inteiramente de `model2`; e valores intermediários produzem uma mistura ponderada. Ambas as entradas devem ser modelos de imagem MOSS com a mesma arquitetura; pesos que não correspondem a nenhum dos prefixos acima usam a proporção de `video_embedder.`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo mesclado, combinando ambas as entradas de acordo com as proporções especificadas | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMOSSImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3b7d9c806a8d53ad00044bf30f5e63431fea7ee565414acb70a56e3059164288`
