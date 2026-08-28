# Orientação Projetada Adaptativa

O nó APG (Adaptive Projected Guidance) modifica o processo de amostragem ao ajustar como a orientação (guidance) é aplicada durante a difusão. Ele separa o vetor de orientação em componentes paralela e ortogonal em relação à saída condicional, permitindo uma geração de imagem mais controlada. O nó fornece parâmetros para escalar a orientação, normalizar sua magnitude e aplicar momentum para transições mais suaves entre as etapas de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a orientação projetada adaptativa | MODEL | Sim | - |
| `eta` | Controla a escala do vetor de orientação paralelo. Comportamento padrão de CFG em uma configuração de 1 (padrão: 1.0). | FLOAT | Sim | -10.0 a 10.0 |
| `limite_normalização` | Normaliza o vetor de orientação para este valor; a normalização é desativada em uma configuração de 0 (padrão: 5.0). | FLOAT | Sim | 0.0 a 50.0 |
| `momento` | Controla uma média móvel da orientação durante a difusão; desativado em uma configuração de 0 (padrão: 0.0). | FLOAT | Sim | -5.0 a 1.0 |

Observação: Quando o nível de ruído (`sigma`) aumenta durante a amostragem, a média móvel do momentum é redefinida para zero. Se o modelo fornecer apenas uma saída condicional (sem condicionamento não condicional separado), o ajuste de orientação é ignorado e o condicionamento é mantido inalterado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | Retorna o modelo modificado com orientação projetada adaptativa aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
