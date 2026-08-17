# Escalonamento Epsilon

Este nó implementa o método Epsilon Scaling do artigo de pesquisa "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6). Ele funciona escalando o ruído previsto durante o processo de amostragem para ajudar a reduzir o viés de exposição, o que pode levar a uma qualidade melhor nas imagens geradas. Esta implementação usa o "esquema uniforme" recomendado pelo artigo por sua praticidade e eficácia.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual o patch de escalonamento épsilon será aplicado. | MODEL | Sim | - |
| `scaling_factor` | O fator pelo qual o ruído previsto é escalado. Um valor maior que 1.0 reduz o ruído previsto, enquanto um valor menor que 1.0 o aumenta (padrão: 1.005). | FLOAT | Sim | 0.5 - 1.5 (passo: 0.001) |

Nota: O `scaling_factor` é protegido contra um valor zero para evitar divisão por zero. A interface impõe um mínimo de 0.5, então isso não pode ocorrer em uso normal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | Uma cópia do modelo de entrada com o patch da função de escalonamento épsilon aplicado ao seu processo de amostragem. O modelo original permanece inalterado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
