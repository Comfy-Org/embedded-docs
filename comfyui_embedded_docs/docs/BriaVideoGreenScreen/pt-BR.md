# Bria Video Green Screen

Este nó substitui o fundo de um vídeo por uma tela de chroma-key sólida usando a API Bria. Ele processa o vídeo de entrada e retorna um novo vídeo onde o fundo original foi removido e substituído por uma cor de tela verde ou azul uniforme.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O vídeo de entrada a ser processado | VIDEO | Sim | Arquivo de vídeo |
| `green_shade` | Tom de chroma-key sólido aplicado atrás do primeiro plano: broadcast_green (#00B140), chroma_green (#00FF00) ou blue_screen (#0000FF) | COMBO | Sim | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Nota:** O vídeo de entrada não deve exceder 60 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo processado com o fundo original substituído pelo tom de chroma-key selecionado, retornado como um vídeo MP4 (H.264) | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/pt-BR.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
