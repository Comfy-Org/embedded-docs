# Escalonamento Epsilon

Este nó implementa o método de Escalonamento Épsilon do artigo de pesquisa "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6). Ele funciona escalando o ruído previsto durante o processo de amostragem para ajudar a reduzir o viés de exposição, o que pode levar a uma melhoria na qualidade das imagens geradas. Esta implementação utiliza a "agenda uniforme" recomendada pelo artigo por sua praticidade e eficácia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual o patch de escalonamento épsilon será aplicado. | MODEL | Sim | - |
| `fator_de_escalonamento` | O fator pelo qual o ruído previsto é escalado. Um valor maior que 1.0 reduz o ruído, enquanto um valor menor que 1.0 o aumenta (padrão: 1.005). Este é um parâmetro avançado. | FLOAT | Não | 0.5 - 1.5 (passo: 0.001) |

Nota: Se `scaling_factor` for definido como 0, o nó automaticamente o substitui por um valor muito pequeno (1e-9) para evitar divisão por zero. O valor mínimo de 0.5 na interface normalmente evita que isso aconteça.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | Uma versão corrigida do modelo de entrada com a função de escalonamento épsilon aplicada ao seu processo de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
