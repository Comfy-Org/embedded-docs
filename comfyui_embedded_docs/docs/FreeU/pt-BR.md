# FreeU

O nó FreeU aplica modificações no domínio de frequência aos blocos de saída de um modelo para melhorar a qualidade da geração de imagens. Ele funciona dimensionando diferentes grupos de canais e aplicando filtragem de Fourier a mapas de características específicos, permitindo um controle fino sobre o comportamento do modelo durante o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar as modificações do FreeU | MODEL | Sim | - |
| `b1` | Fator de escala do backbone para recursos de model_channels × 4 (padrão: 1.1) | FLOAT | Sim | 0.0 - 10.0 |
| `b2` | Fator de escala do backbone para recursos de model_channels × 2 (padrão: 1.2) | FLOAT | Sim | 0.0 - 10.0 |
| `s1` | Fator de escala da conexão de salto para recursos de model_channels × 4 (padrão: 0.9) | FLOAT | Sim | 0.0 - 10.0 |
| `s2` | Fator de escala da conexão de salto para recursos de model_channels × 2 (padrão: 0.2) | FLOAT | Sim | 0.0 - 10.0 |

Nota: As modificações são aplicadas apenas a mapas de características com canais model_channels × 4 e model_channels × 2; `b1`/`s1` afetam os primeiros e `b2`/`s2` afetam os últimos. Os demais mapas de características permanecem inalterados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com os patches FreeU aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
