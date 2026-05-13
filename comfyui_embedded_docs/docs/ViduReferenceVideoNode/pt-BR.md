> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/en.md)

O Nó de Vídeo de Referência Vidu gera vídeos a partir de múltiplas imagens de referência e um prompt de texto. Ele utiliza modelos de IA para criar conteúdo de vídeo consistente com base nas imagens e na descrição fornecidas. O nó suporta várias configurações de vídeo, incluindo duração, proporção de aspecto, resolução e controle de movimento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"viduq1"` | Nome do modelo para geração de vídeo (padrão: "viduq1") |
| `images` | IMAGE | Sim | - | Imagens a serem usadas como referência para gerar um vídeo com assuntos consistentes (máximo de 7 imagens) |
| `prompt` | STRING | Sim | - | Uma descrição textual para a geração do vídeo |
| `duration` | INT | Não | 5-5 | Duração do vídeo de saída em segundos (padrão: 5) |
| `seed` | INT | Não | 0-2147483647 | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) |
| `aspect_ratio` | COMBO | Não | `"16:9"`<br>`"9:16"`<br>`"1:1"` | A proporção de aspecto do vídeo de saída (padrão: "16:9") |
| `resolution` | COMBO | Não | `"1080p"` | Os valores suportados podem variar conforme o modelo e a duração (padrão: "1080p") |
| `movement_amplitude` | COMBO | Não | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | A amplitude de movimento dos objetos no quadro (padrão: "auto") |

**Restrições e Limitações:**

- O campo `prompt` é obrigatório e não pode estar vazio
- Máximo de 7 imagens permitidas para referência
- Cada imagem deve ter uma proporção de aspecto entre 1:4 e 4:1
- Cada imagem deve ter dimensões mínimas de 128x128 pixels
- A duração é fixa em 5 segundos

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado com base nas imagens de referência e no prompt |

---
**Source fingerprint (SHA-256):** `11a7de2f50658467f63d284ef6b95d91dcdd39b4e6e5cea3b8d2f2a5d63a3020`
