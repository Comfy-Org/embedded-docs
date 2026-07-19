# Geração de Vídeo Vidu por Texto

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/en.md)

O nó de Geração de Vídeo a partir de Texto Vidu cria vídeos a partir de descrições textuais. Ele utiliza o modelo de geração de vídeo Vidu para transformar seus prompts de texto em conteúdo de vídeo com configurações personalizáveis para duração, proporção de tela e estilo visual.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | Nome do modelo | COMBO | Sim | `viduq1` |
| `prompt` | Uma descrição textual para geração de vídeo | STRING | Sim | - |
| `duração` | Duração do vídeo de saída em segundos (padrão: 5) | INT | Não | 5-5 |
| `semente` | Semente para geração de vídeo (0 para aleatório) (padrão: 0) | INT | Não | 0-2147483647 |
| `proporção` | A proporção de tela do vídeo de saída | COMBO | Não | `16:9`<br>`9:16`<br>`1:1` |
| `resolução` | Os valores suportados podem variar conforme o modelo e a duração | COMBO | Não | `1080p` |
| `amplitude de movimento` | A amplitude de movimento dos objetos no quadro | COMBO | Não | `auto`<br>`small`<br>`medium`<br>`large` |

**Nota:** O campo `prompt` é obrigatório e não pode estar vazio. O parâmetro `duration` está atualmente fixado em 5 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado com base no prompt de texto | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
