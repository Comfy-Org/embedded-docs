# PhotoMakerEncode

PhotoMakerEncode cria dados de condicionamento para geração de imagens por IA, combinando uma imagem de referência com um prompt de texto. Ele pesquisa no prompt de texto a palavra "photomaker" e, quando encontrada, usa o modelo PhotoMaker para aplicar as características visuais da imagem de referência naquela posição do prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `photomaker` | O modelo PhotoMaker usado para processar a imagem de referência e gerar embeddings baseados em imagem | PHOTOMAKER | Sim | - |
| `image` | A imagem de referência que fornece características visuais para o condicionamento | IMAGE | Sim | - |
| `clip` | O modelo CLIP usado para tokenização e codificação de texto | CLIP | Sim | - |
| `text` | O prompt de texto para geração de condicionamento. Suporta múltiplas linhas e prompts dinâmicos (padrão: "photograph of photomaker") | STRING | Sim | - |

**Nota:** A palavra "photomaker" deve aparecer como uma palavra separada no prompt de texto (a correspondência diferencia maiúsculas de minúsculas) para que o condicionamento baseado em imagem seja aplicado. Quando presente, as características da imagem são injetadas naquela posição do prompt. Se "photomaker" não for encontrado, o nó retorna o condicionamento de texto padrão sem influência da imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento contendo embeddings de imagem e texto para orientar a geração de imagens, juntamente com a saída pooled do codificador de texto CLIP | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
