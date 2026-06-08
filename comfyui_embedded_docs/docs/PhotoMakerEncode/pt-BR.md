O nó PhotoMakerEncode processa imagens e texto para gerar dados de condicionamento para geração de imagens por IA. Ele recebe uma imagem de referência e um prompt de texto, criando embeddings que podem ser usados para guiar a geração de imagens com base nas características visuais da imagem de referência. O nó procura especificamente pelo token "photomaker" no texto para determinar onde aplicar o condicionamento baseado em imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `photomaker` | O modelo PhotoMaker usado para processar a imagem e gerar embeddings | PHOTOMAKER | Sim | - |
| `imagem` | A imagem de referência que fornece características visuais para o condicionamento | IMAGE | Sim | - |
| `clip` | O modelo CLIP usado para tokenização e codificação de texto | CLIP | Sim | - |
| `texto` | O prompt de texto para geração de condicionamento (padrão: "photograph of photomaker") | STRING | Sim | - |

**Observação:** Quando o texto contém a palavra "photomaker", o nó aplica condicionamento baseado em imagem naquela posição do prompt. Se "photomaker" não for encontrado no texto, o nó gera condicionamento de texto padrão sem influência da imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento contendo embeddings de imagem e texto para guiar a geração de imagens | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `535fd3dbbe0e48205bebde030138ffca841dc94a18fd47db768a1066fe84bce4`
