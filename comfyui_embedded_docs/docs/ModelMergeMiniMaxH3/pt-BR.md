# Model Merge MiniMax H3

Mescle dois modelos MiniMax H3 compatíveis por componente, com uma proporção separada para cada parte da arquitetura. Cada proporção é a fração de `model1`, então você pode manter as projeções de patch e os blocos de refinamento de um modelo enquanto substitui os blocos do transformer por outro.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model1` | Primeiro modelo MiniMax H3. Cada componente começa a partir dele, e cada proporção decide quanto desse componente vem de `model2` em vez disso. | MODEL | Sim | - |
| `model2` | Segundo modelo MiniMax H3 que fornece os componentes que você mescla. | MODEL | Sim | - |
| `video_patch_proj.` | Proporção de `model1` para a projeção de patch de vídeo (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `audio_patch_proj.` | Proporção de `model1` para a projeção de patch de áudio (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `condition_proj.` | Proporção de `model1` para a projeção de condicionamento (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `time_embedder.` | Proporção de `model1` para o incorporador de tempo (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `token_refiner.blocks.0.` | Proporção de `model1` para o primeiro bloco refinador de tokens (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `token_refiner.blocks.1.` | Proporção de `model1` para o segundo bloco refinador de tokens (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `token_refiner.final_norm.` | Proporção de `model1` para a normalização final do refinador de tokens (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `blocks.0.` até `blocks.49.` | Proporção de `model1` para cada um dos 50 blocos do transformer, um widget por bloco (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.norm.` | Proporção de `model1` para a normalização da camada final (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.adaln_proj.` | Proporção de `model1` para a projeção de normalização adaptativa final (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.video_out.` | Proporção de `model1` para a camada de saída de vídeo (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.audio_out.` | Proporção de `model1` para a camada de saída de áudio (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

Uma proporção de 1.0 (o padrão) mantém esse componente inteiramente vindo de `model1`, e 0.0 faz com que ele venha inteiramente de `model2`; valores intermediários mesclam os dois. Tensores que não possuem proporção, como estatísticas de normalização, sempre vêm de `model1`. Ambas as entradas devem ser modelos MiniMax H3 com a mesma arquitetura; caso contrário, a mesclagem produz um modelo que não executa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O modelo MiniMax H3 mesclado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
