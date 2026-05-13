> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/pt-BR.md)

O nó de Geração de Vídeo a partir de Imagem Vidu cria um vídeo curto a partir de uma imagem inicial e uma descrição textual opcional. Ele utiliza um modelo de IA para gerar conteúdo de vídeo que dá continuidade ao quadro da imagem fornecida e retorna o vídeo resultante.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `viduq1` | Nome do modelo (padrão: viduq1) |
| `image` | IMAGE | Sim | - | Uma imagem a ser usada como quadro inicial do vídeo gerado |
| `prompt` | STRING | Não | - | Uma descrição textual para a geração do vídeo (padrão: vazio) |
| `duration` | INT | Não | 5-5 | Duração do vídeo de saída em segundos (padrão: 5, fixado em 5 segundos) |
| `seed` | INT | Não | 0-2147483647 | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) |
| `resolution` | COMBO | Não | `1080p` | Os valores suportados podem variar conforme o modelo e a duração (padrão: 1080p) |
| `movement_amplitude` | COMBO | Não | `auto`<br>`small`<br>`medium`<br>`large` | A amplitude de movimento dos objetos no quadro (padrão: auto) |

**Restrições:**

- Apenas uma imagem de entrada é permitida (não é possível processar múltiplas imagens).
- A imagem de entrada deve ter uma proporção de aspecto entre 1:4 e 4:1.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado como saída |

---
**Source fingerprint (SHA-256):** `064b3efba8219770595e68a6607a6f8113d1be7c9f3863a4740ee5c3a146d91e`
