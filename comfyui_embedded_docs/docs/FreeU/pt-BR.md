> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/pt-BR.md)

O nó FreeU aplica modificações no domínio da frequência aos blocos de saída de um modelo para melhorar a qualidade da geração de imagens. Ele funciona escalando diferentes grupos de canais e aplicando filtragem de Fourier a mapas de características específicos, permitindo um controle refinado sobre o comportamento do modelo durante o processo de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar as modificações FreeU |
| `b1` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala do backbone para características de model_channels × 4 (padrão: 1,1) |
| `b2` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala do backbone para características de model_channels × 2 (padrão: 1,2) |
| `s1` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala da conexão skip para características de model_channels × 4 (padrão: 0,9) |
| `s2` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala da conexão skip para características de model_channels × 2 (padrão: 0,2) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo modificado com os patches FreeU aplicados |

---
**Source fingerprint (SHA-256):** `449a02a4bb5b42eb37fab394bcdc6375e08e369961d633618211ebc5f737ab51`
