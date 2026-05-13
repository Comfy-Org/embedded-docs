> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/pt-BR.md)

O nó OpenAIVideoSora2 gera vídeos usando os modelos Sora da OpenAI. Ele cria conteúdo de vídeo com base em prompts de texto e imagens de entrada opcionais, retornando a saída de vídeo gerada. O nó suporta diferentes durações e resoluções de vídeo, dependendo do modelo selecionado.

**AVISO DE OBSOLESCÊNCIA:** A OpenAI deixará de fornecer a API Sora v2 em setembro de 2026. Este nó será removido do ComfyUI nessa ocasião.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | "sora-2"<br>"sora-2-pro" | O modelo OpenAI Sora a ser usado para geração de vídeo (padrão: "sora-2") |
| `prompt` | STRING | Sim | - | Texto de orientação; pode estar vazio se uma imagem de entrada estiver presente (padrão: vazio) |
| `tamanho` | COMBO | Sim | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" | A resolução do vídeo gerado (padrão: "1280x720") |
| `duração` | COMBO | Sim | 4<br>8<br>12 | A duração do vídeo gerado em segundos (padrão: 8) |
| `imagem` | IMAGE | Não | - | Imagem de entrada opcional para geração de vídeo |
| `seed` | INT | Não | 0 a 2147483647 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da semente (padrão: 0) |

**Restrições e Limitações:**

- O modelo "sora-2" suporta apenas as resoluções "720x1280" e "1280x720"
- Apenas uma imagem de entrada é suportada ao usar o parâmetro `image`
- Os resultados são não determinísticos, independentemente do valor da semente

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | A saída de vídeo gerada |

---
**Source fingerprint (SHA-256):** `c87b696dd92c6a6a929f49d189a375b1ebed80bf47f24667ee17c0b210330e55`
