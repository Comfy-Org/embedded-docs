# Orientação Projetada Adaptativa

O nó APG (Adaptive Projected Guidance) modifica o processo de amostragem ajustando como a orientação (guidance) é aplicada durante a difusão. Ele separa o vetor de orientação em componentes paralelas e ortogonais relativas à saída condicional, permitindo uma geração de imagem mais controlada. O nó fornece parâmetros para escalar a orientação, normalizar sua magnitude e aplicar momentum para transições mais suaves entre as etapas de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar a orientação projetada adaptativa | MODEL | Sim | - |
| `eta` | Controla a escala do vetor de orientação paralelo. Comportamento padrão de CFG em uma configuração de 1 (padrão: 1.0). | FLOAT | Sim | -10.0 a 10.0 |
| `norm_threshold` | Normaliza o vetor de orientação para este valor; a normalização é desativada em uma configuração de 0 (padrão: 5.0). | FLOAT | Sim | 0.0 a 50.0 |
| `momentum` | Controla uma média móvel da orientação durante a difusão; desativado em uma configuração de 0 (padrão: 0.0). | FLOAT | Sim | -5.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | Retorna o modelo modificado com orientação projetada adaptativa aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
