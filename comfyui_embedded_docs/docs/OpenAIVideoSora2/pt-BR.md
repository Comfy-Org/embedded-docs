# OpenAI Sora - Vídeo

O nó OpenAIVideoSora2 gera vídeos com os modelos Sora da OpenAI. Ele recebe um prompt de texto junto com uma única imagem de referência opcional, envia a solicitação para a OpenAI, aguarda a conclusão da geração e retorna o vídeo resultante. As durações e resoluções suportadas dependem do modelo selecionado.

**AVISO DE DESCONTINUAÇÃO:** A OpenAI deixará de fornecer a API Sora v2 em setembro de 2026. Este nó será removido do ComfyUI nessa data.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo Sora da OpenAI a ser usado para geração de vídeo (padrão: "sora-2") | COMBO | Sim | "sora-2"<br>"sora-2-pro" |
| `prompt` | Texto orientador; pode ficar vazio se uma imagem de entrada estiver presente (padrão: string vazia) | STRING | Sim | - |
| `tamanho` | A resolução do vídeo gerado (padrão: "1280x720") | COMBO | Sim | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duração` | A duração do vídeo gerado em segundos (padrão: 8) | COMBO | Sim | 4<br>8<br>12 |
| `imagem` | Imagem de referência de entrada opcional usada para geração de vídeo; apenas uma única imagem é suportada | IMAGE | Não | - |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Não | 0 a 2147483647 |

**Restrições e limitações:**

- O modelo "sora-2" suporta apenas os tamanhos "720x1280" e "1280x720"; selecionar "1024x1792" ou "1792x1024" com "sora-2" gera um erro. Os tamanhos maiores estão disponíveis apenas com "sora-2-pro".
- Quando uma imagem é conectada, ela deve conter exatamente uma imagem; conectar mais de uma imagem gera um erro.
- Os resultados são não determinísticos independentemente do valor da semente.
- A estimativa de preço exibida depende dos valores selecionados de `model`, `size` e `duration`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O vídeo gerado pela OpenAI Sora | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
