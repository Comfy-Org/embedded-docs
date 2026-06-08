Este nó prepara dados para treinamento, codificando imagens e textos. Ele recebe uma lista de imagens e uma lista correspondente de legendas de texto, em seguida, utiliza um modelo VAE para converter as imagens em representações latentes e um modelo CLIP para converter o texto em dados de condicionamento. Os pares resultantes de latentes e condicionamentos são gerados como listas, prontos para uso em fluxos de trabalho de treinamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | Lista de imagens a serem codificadas. | IMAGE | Sim | N/A |
| `vae` | Modelo VAE para codificar imagens em latentes. | VAE | Sim | N/A |
| `clip` | Modelo CLIP para codificar texto em condicionamento. | CLIP | Sim | N/A |
| `textos` | Lista de legendas de texto. Pode ter comprimento n (correspondendo às imagens), 1 (repetido para todas) ou ser omitida (usa string vazia). | STRING | Não | N/A |

**Restrições dos Parâmetros:**

* O número de itens na lista `texts` deve ser 0, 1 ou corresponder exatamente ao número de itens na lista `images`. Se for 0, uma string vazia é usada para todas as imagens. Se for 1, esse único texto é repetido para todas as imagens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latents` | Lista de dicionários de latentes. | LATENT |
| `conditioning` | Lista de listas de condicionamento. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `95947c03f140f527f3db54d0b0131d956646055542ddb546ae5eaa82e4e8cefa`
