# PerturbedAttentionGuidance

O nó PerturbedAttentionGuidance aplica orientação de atenção perturbada a um modelo de difusão para melhorar a qualidade da geração. Ele ajusta o processo de remoção de ruído do modelo durante a amostragem, comparando a previsão condicional normal com uma feita usando um mecanismo de atenção simplificado que utiliza apenas projeções de valor, e então adiciona a diferença escalada de volta ao resultado. Quando a escala é definida como 0, o nó não tem efeito.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de difusão ao qual a orientação de atenção perturbada será aplicada | MODEL | Sim | - |
| `scale` | A intensidade do efeito da orientação de atenção perturbada (padrão: 3.0). Quando definida como 0, o nó não tem efeito e retorna o resultado original após a remoção de ruído. | FLOAT | Sim | 0.0 - 100.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo modificado com a orientação de atenção perturbada aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
