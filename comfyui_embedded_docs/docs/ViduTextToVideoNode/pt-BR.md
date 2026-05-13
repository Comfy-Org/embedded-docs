> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/en.md)

O nó de Geração de Vídeo a partir de Texto Vidu cria vídeos a partir de descrições textuais. Ele utiliza o modelo de geração de vídeo Vidu para transformar seus prompts de texto em conteúdo de vídeo com configurações personalizáveis para duração, proporção de tela e estilo visual.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | `viduq1` | Nome do modelo |
| `prompt` | STRING | Sim | - | Uma descrição textual para geração de vídeo |
| `duração` | INT | Não | 5-5 | Duração do vídeo de saída em segundos (padrão: 5) |
| `semente` | INT | Não | 0-2147483647 | Semente para geração de vídeo (0 para aleatório) (padrão: 0) |
| `proporção` | COMBO | Não | `16:9`<br>`9:16`<br>`1:1` | A proporção de tela do vídeo de saída |
| `resolução` | COMBO | Não | `1080p` | Os valores suportados podem variar conforme o modelo e a duração |
| `amplitude de movimento` | COMBO | Não | `auto`<br>`small`<br>`medium`<br>`large` | A amplitude de movimento dos objetos no quadro |

**Nota:** O campo `prompt` é obrigatório e não pode estar vazio. O parâmetro `duration` está atualmente fixado em 5 segundos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado com base no prompt de texto |

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
