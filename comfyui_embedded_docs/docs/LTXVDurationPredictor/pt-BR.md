# LTXV Duration Predictor

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo usado para pré-processar os embeddings de texto e executar a cabeça de duração. | MODEL | Sim | N/A |
| `positive` | O condicionamento que fornece os embeddings de texto do prompt e os metadados para a previsão de duração. | CONDITIONING | Sim | N/A |
| `duration_head` | Cabeça de duração LTX 2.4 carregada com ModelPatchLoader. Deve ser uma cabeça de duração LTX. | MODEL_PATCH | Sim | N/A |
| `frame_rate` | Taxa de quadros em quadros por segundo usada para converter segundos em quadros (padrão: 24.0). | FLOAT | Sim | 1.0 a 120.0 |
| `min_seconds` | Duração mínima em segundos usada ao converter a previsão em um número de quadros (padrão: 1.0). | FLOAT | Sim | 0.5 a 120.0 |
| `max_seconds` | Duração máxima em segundos usada ao converter a previsão em um número de quadros (padrão: 20.0). | FLOAT | Sim | 0.5 a 120.0 |

Nota: a entrada `duration_head` deve ser uma cabeça de duração LTX 2.4 carregada com ModelPatchLoader. Se o patch de modelo conectado não for uma cabeça de duração LTX, o nó gera um ValueError.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `num_frames` | A duração prevista convertida em um número de quadros e ajustada à grade de quadros 8k+1 da VAE. | INT |
| `seconds` | Duração prevista bruta (sem restrição). Este é o valor antes do ajuste à grade de quadros. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ebbf6a2601a955122ab9862142aa475524c1f38403f4ef8dc9ffee6456ee8ce5`
