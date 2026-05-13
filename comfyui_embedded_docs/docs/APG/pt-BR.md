> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/pt-BR.md)

O nó APG (Adaptive Projected Guidance) modifica o processo de amostragem ajustando como a orientação é aplicada durante a difusão. Ele separa o vetor de orientação em componentes paralelos e ortogonais em relação à saída condicionada, permitindo uma geração de imagem mais controlada. O nó fornece parâmetros para escalar a orientação, normalizar sua magnitude e aplicar momentum para transições mais suaves entre as etapas de difusão.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a orientação projetada adaptativa |
| `eta` | FLOAT | Sim | -10.0 a 10.0 | Controla a escala do vetor de orientação paralelo. Comportamento CFG padrão na configuração 1 (padrão: 1.0). |
| `limite_normalização` | FLOAT | Sim | 0.0 a 50.0 | Normaliza o vetor de orientação para este valor; a normalização é desativada na configuração 0 (padrão: 5.0). |
| `momento` | FLOAT | Sim | -5.0 a 1.0 | Controla uma média móvel da orientação durante a difusão; desativado na configuração 0 (padrão: 0.0). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | Retorna o modelo modificado com a orientação projetada adaptativa aplicada ao seu processo de amostragem |

---
**Source fingerprint (SHA-256):** `89e2486bf08f750f82608db93c389f0b25ce0be766f62faa8704d19bd7e41654`
