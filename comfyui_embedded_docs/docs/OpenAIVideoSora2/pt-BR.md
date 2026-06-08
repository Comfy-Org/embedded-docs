O nó OpenAIVideoSora2 gera vídeos usando os modelos Sora da OpenAI. Ele cria conteúdo de vídeo com base em prompts de texto e imagens de entrada opcionais, retornando a saída de vídeo gerada. O nó suporta diferentes durações e resoluções de vídeo, dependendo do modelo selecionado.

**AVISO DE OBSOLESCÊNCIA:** A OpenAI deixará de fornecer a API Sora v2 em setembro de 2026. Este nó será removido do ComfyUI nessa ocasião.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo OpenAI Sora a ser usado para geração de vídeo (padrão: "sora-2") | COMBO | Sim | "sora-2"<br>"sora-2-pro" |
| `prompt` | Texto de orientação; pode estar vazio se uma imagem de entrada estiver presente (padrão: vazio) | STRING | Sim | - |
| `tamanho` | A resolução do vídeo gerado (padrão: "1280x720") | COMBO | Sim | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duração` | A duração do vídeo gerado em segundos (padrão: 8) | COMBO | Sim | 4<br>8<br>12 |
| `imagem` | Imagem de entrada opcional para geração de vídeo | IMAGE | Não | - |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da semente (padrão: 0) | INT | Não | 0 a 2147483647 |

**Restrições e Limitações:**

- O modelo "sora-2" suporta apenas as resoluções "720x1280" e "1280x720"
- Apenas uma imagem de entrada é suportada ao usar o parâmetro `image`
- Os resultados são não determinísticos, independentemente do valor da semente

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A saída de vídeo gerada | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c87b696dd92c6a6a929f49d189a375b1ebed80bf47f24667ee17c0b210330e55`
