# FreeU

O nó FreeU aplica modificações no domínio da frequência aos blocos de saída de um modelo para melhorar a qualidade da geração de imagens. Ele funciona escalando diferentes grupos de canais e aplicando filtragem de Fourier a mapas de características específicos, permitindo controle ajustado sobre o comportamento do modelo durante o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar as modificações do FreeU | MODEL | Sim | - |
| `b1` | Fator de escala do backbone aplicado a mapas de características com model_channels × 4 canais (padrão: 1.1). Marcado como configuração avançada. | FLOAT | Sim | 0.0 - 10.0 |
| `b2` | Fator de escala do backbone aplicado a mapas de características com model_channels × 2 canais (padrão: 1.2). Marcado como configuração avançada. | FLOAT | Sim | 0.0 - 10.0 |
| `s1` | Fator de escala da conexão de salto aplicado a mapas de características com model_channels × 4 canais (padrão: 0.9). Marcado como configuração avançada. | FLOAT | Sim | 0.0 - 10.0 |
| `s2` | Fator de escala da conexão de salto aplicado a mapas de características com model_channels × 2 canais (padrão: 0.2). Marcado como configuração avançada. | FLOAT | Sim | 0.0 - 10.0 |

Nota: Os ajustes do FreeU são aplicados apenas a mapas de características cuja contagem de canais seja igual a model_channels × 4 (usando `b1` e `s1`) ou model_channels × 2 (usando `b2` e `s2`). O filtro de Fourier escala apenas a região central de baixa frequência (limiar de 1) dos mapas de características da conexão de salto; todos os outros componentes de frequência permanecem inalterados. Todos os quatro parâmetros de escala aceitam valores entre 0.0 e 10.0 em passos de 0.01.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com patches do FreeU aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
