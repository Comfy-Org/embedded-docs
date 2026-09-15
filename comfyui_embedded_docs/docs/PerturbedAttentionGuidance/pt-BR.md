# PerturbedAttentionGuidance

O nó PerturbedAttentionGuidance aplica orientação de atenção perturbada a um modelo de difusão para melhorar a qualidade da geração. Durante a amostragem, ele faz uma previsão extra na qual a autoatenção do bloco intermediário é substituída por uma versão simplificada que repassa as projeções de valor diretamente, e então adiciona ao resultado desruidoso a diferença, multiplicada pela escala, entre a previsão condicional normal e essa previsão perturbada. Definir `scale` como 0 desativa completamente o efeito.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de difusão ao qual aplicar a orientação de atenção perturbada | MODEL | Sim | - |
| `scale` | A intensidade do efeito de orientação de atenção perturbada (padrão: 3.0). Quando definido como 0, o nó não tem efeito e retorna o resultado desruidoso original inalterado. | FLOAT | Sim | 0.0 - 100.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo modificado com o patch de orientação de atenção perturbada anexado ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
