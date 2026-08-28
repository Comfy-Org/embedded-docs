# FreeU

O nó FreeU aplica modificações no domínio da frequência aos blocos de saída de um modelo para melhorar a qualidade da geração de imagens. Ele funciona escalando diferentes grupos de canais e aplicando filtragem de Fourier a mapas de características específicos, permitindo um controle fino sobre o comportamento do modelo durante o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar as modificações FreeU | MODEL | Sim | - |
| `b1` | Fator de escala do backbone para características de model_channels × 4 (padrão: 1.1) | FLOAT | Sim | 0.0 - 10.0 |
| `b2` | Fator de escala do backbone para características de model_channels × 2 (padrão: 1.2) | FLOAT | Sim | 0.0 - 10.0 |
| `s1` | Fator de escala da conexão de salto para características de model_channels × 4 (padrão: 0.9) | FLOAT | Sim | 0.0 - 10.0 |
| `s2` | Fator de escala da conexão de salto para características de model_channels × 2 (padrão: 0.2) | FLOAT | Sim | 0.0 - 10.0 |

Nota: Os ajustes FreeU são aplicados apenas a mapas de características cujo número de canais seja igual a model_channels × 4 (usando `b1` e `s1`) ou model_channels × 2 (usando `b2` e `s2`). O filtro de Fourier escala apenas a região central de baixa frequência dos mapas de características da conexão de salto; todos os outros componentes de frequência permanecem inalterados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com os patches FreeU aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
