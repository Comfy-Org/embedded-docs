# Geração de Vídeo por Referência Vidu

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/en.md)

O Nó de Vídeo de Referência Vidu gera vídeos a partir de múltiplas imagens de referência e um prompt de texto. Ele utiliza modelos de IA para criar conteúdo de vídeo consistente com base nas imagens e na descrição fornecidas. O nó suporta várias configurações de vídeo, incluindo duração, proporção de aspecto, resolução e controle de movimento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | Nome do modelo para geração de vídeo (padrão: "viduq1") | COMBO | Sim | `"viduq1"` |
| `imagens` | Imagens a serem usadas como referência para gerar um vídeo com assuntos consistentes (máximo de 7 imagens) | IMAGE | Sim | - |
| `prompt` | Uma descrição textual para a geração do vídeo | STRING | Sim | - |
| `duração` | Duração do vídeo de saída em segundos (padrão: 5) | INT | Não | 5-5 |
| `semente` | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) | INT | Não | 0-2147483647 |
| `proporção` | A proporção de aspecto do vídeo de saída (padrão: "16:9") | COMBO | Não | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `resolução` | Os valores suportados podem variar conforme o modelo e a duração (padrão: "1080p") | COMBO | Não | `"1080p"` |
| `amplitude de movimento` | A amplitude de movimento dos objetos no quadro (padrão: "auto") | COMBO | Não | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Restrições e Limitações:**

- O campo `prompt` é obrigatório e não pode estar vazio
- Máximo de 7 imagens permitidas para referência
- Cada imagem deve ter uma proporção de aspecto entre 1:4 e 4:1
- Cada imagem deve ter dimensões mínimas de 128x128 pixels
- A duração é fixa em 5 segundos

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado com base nas imagens de referência e no prompt | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `11a7de2f50658467f63d284ef6b95d91dcdd39b4e6e5cea3b8d2f2a5d63a3020`
