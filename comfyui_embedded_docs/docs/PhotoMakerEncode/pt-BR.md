# PhotoMakerEncode

O nó PhotoMakerEncode combina uma imagem de referência com um prompt de texto para criar dados de condicionamento para geração de imagens. Quando o texto contém a palavra "photomaker", o nó usa o modelo PhotoMaker para inserir a identidade visual da imagem de referência no condicionamento naquela posição do prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `photomaker` | O modelo PhotoMaker usado para processar a imagem de referência e gerar embeddings baseados em imagem | PHOTOMAKER | Sim | - |
| `imagem` | A imagem de referência que fornece as características visuais para o condicionamento | IMAGE | Sim | - |
| `clip` | O modelo CLIP usado para tokenização e codificação de texto | CLIP | Sim | - |
| `texto` | O prompt de texto para geração de condicionamento. Suporta texto multilinha e prompts dinâmicos (padrão: "photograph of photomaker") | STRING | Sim | Qualquer string |

**Nota:** Quando o texto contém "photomaker" como uma palavra isolada, o nó remove essa palavra do prompt codificado e aplica a identidade da imagem de referência nessa posição usando o modelo PhotoMaker. Se "photomaker" não for encontrado no texto, o nó retorna o condicionamento de texto padrão sem influência da imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento contendo os embeddings de texto e imagem que guiam a geração de imagens, juntamente com a saída com pooling do codificador de texto CLIP | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
