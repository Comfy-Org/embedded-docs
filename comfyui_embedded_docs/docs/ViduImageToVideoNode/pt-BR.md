O nó de Geração de Vídeo a partir de Imagem Vidu cria um vídeo curto a partir de uma imagem inicial e uma descrição textual opcional. Ele utiliza um modelo de IA para gerar conteúdo de vídeo que dá continuidade ao quadro da imagem fornecida e retorna o vídeo resultante.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | Nome do modelo (padrão: viduq1) | COMBO | Sim | `viduq1` |
| `image` | Uma imagem a ser usada como quadro inicial do vídeo gerado | IMAGE | Sim | - |
| `prompt` | Uma descrição textual para a geração do vídeo (padrão: vazio) | STRING | Não | - |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5, fixado em 5 segundos) | INT | Não | 5-5 |
| `seed` | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) | INT | Não | 0-2147483647 |
| `resolution` | Os valores suportados podem variar conforme o modelo e a duração (padrão: 1080p) | COMBO | Não | `1080p` |
| `movement_amplitude` | A amplitude de movimento dos objetos no quadro (padrão: auto) | COMBO | Não | `auto`<br>`small`<br>`medium`<br>`large` |

**Restrições:**

- Apenas uma imagem de entrada é permitida (não é possível processar múltiplas imagens).
- A imagem de entrada deve ter uma proporção de aspecto entre 1:4 e 4:1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado como saída | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `064b3efba8219770595e68a6607a6f8113d1be7c9f3863a4740ee5c3a146d91e`
