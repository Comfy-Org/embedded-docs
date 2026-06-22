# Diffusão Diferencial

O nó Differential Diffusion modifica o processo de remoção de ruído aplicando uma máscara binária baseada em limites de passo de tempo. Ele cria uma máscara que faz uma mescla entre a máscara de remoção de ruído original e uma máscara binária baseada em limite, permitindo o ajuste controlado da intensidade do processo de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão a ser modificado | MODEL | Sim | - |
| `força` | Controla a intensidade da mescla entre a máscara de remoção de ruído original e a máscara binária de limite (padrão: 1.0) | FLOAT | Não | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo de difusão modificado com a função de máscara de remoção de ruído atualizada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3b1727baa6c546516f5dfb53e6e39f27fc7429cde2ac7fd7dfbab99eebb39816`
