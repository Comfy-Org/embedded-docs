# PerturbedAttentionGuidance

O nó PerturbedAttentionGuidance aplica orientação de atenção perturbada a um modelo de difusão para melhorar a qualidade da geração. Ele modifica o mecanismo de autoatenção do modelo durante a amostragem, substituindo-o por uma versão simplificada focada nas projeções de valor. Essa técnica ajuda a melhorar a coerência e a qualidade das imagens geradas, ajustando o processo de remoção condicional de ruído.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a orientação de atenção perturbada | MODEL | Sim | - |
| `scale` | A intensidade do efeito de orientação de atenção perturbada (padrão: 3.0). Quando definido como 0, o nó não tem efeito e retorna o resultado original da remoção de ruído. | FLOAT | Não | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com orientação de atenção perturbada aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8808aa3a3f7cfe306e17f8f4424779cb8e4565647bbcc9d4907da2215affe191`
