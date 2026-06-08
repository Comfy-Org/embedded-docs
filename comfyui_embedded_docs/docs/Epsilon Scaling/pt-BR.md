Este nó implementa o método de Escalonamento Épsilon (Epsilon Scaling) do artigo de pesquisa "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6). Ele funciona escalonando o ruído previsto durante o processo de amostragem para ajudar a reduzir o viés de exposição, o que pode levar a uma qualidade melhorada nas imagens geradas. Esta implementação utiliza o "esquema uniforme" recomendado pelo artigo por sua praticidade e eficácia.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual o patch de escalonamento épsilon será aplicado. | MODEL | Sim | - |
| `fator_de_escalonamento` | O fator pelo qual o ruído previsto é escalonado. Um valor maior que 1,0 reduz o ruído, enquanto um valor menor que 1,0 o aumenta (padrão: 1,005). | FLOAT | Não | 0,5 - 1,5 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | Uma versão corrigida do modelo de entrada com a função de escalonamento épsilon aplicada ao seu processo de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/pt-BR.md)

---
**Source fingerprint (SHA-256):** `85c464ce0b2ec2a031a01d9eef5d50fd300be3012499cc061705fb7964110882`
