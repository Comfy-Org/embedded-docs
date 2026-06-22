# Orientação Projetada Adaptativa

O nó APG (Adaptive Projected Guidance) modifica o processo de amostragem ajustando como a orientação é aplicada durante a difusão. Ele separa o vetor de orientação em componentes paralelos e ortogonais em relação à saída condicionada, permitindo uma geração de imagem mais controlada. O nó fornece parâmetros para escalar a orientação, normalizar sua magnitude e aplicar momentum para transições mais suaves entre as etapas de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a orientação projetada adaptativa | MODEL | Sim | - |
| `eta` | Controla a escala do vetor de orientação paralelo. Comportamento CFG padrão na configuração 1 (padrão: 1.0). | FLOAT | Sim | -10.0 a 10.0 |
| `limite_normalização` | Normaliza o vetor de orientação para este valor; a normalização é desativada na configuração 0 (padrão: 5.0). | FLOAT | Sim | 0.0 a 50.0 |
| `momento` | Controla uma média móvel da orientação durante a difusão; desativado na configuração 0 (padrão: 0.0). | FLOAT | Sim | -5.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | Retorna o modelo modificado com a orientação projetada adaptativa aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `89e2486bf08f750f82608db93c389f0b25ce0be766f62faa8704d19bd7e41654`
