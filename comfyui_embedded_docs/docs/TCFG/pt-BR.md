> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/pt-BR.md)

Aqui está a tradução da documentação para português brasileiro, seguindo todas as regras especificadas:

TCFG (Tangential Damping CFG) refina as previsões incondicionais (negativas) para melhor alinhá-las com as previsões condicionais (positivas) durante o processo de amostragem. Esta técnica melhora a qualidade da saída aplicando amortecimento tangencial à orientação incondicional, com base no artigo de pesquisa 2503.18137. O nó modifica o comportamento de amostragem do modelo ajustando como as previsões incondicionais são processadas durante a orientação livre de classificador.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar o CFG com amortecimento tangencial |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `patched_model` | MODEL | O modelo modificado com o CFG de amortecimento tangencial aplicado |

---
**Source fingerprint (SHA-256):** `de6b4deb8a42f05dff90e393bff1e0b4b8ed58887586ca81c236e1a780be5776`
