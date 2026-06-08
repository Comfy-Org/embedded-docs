# Bria Video Green Screen

Este nó substitui o fundo de um vídeo por uma tela sólida de chroma-key usando a API Bria. Ele processa o vídeo de entrada e retorna um novo vídeo onde o fundo original foi removido e substituído por uma cor uniforme de tela verde ou azul.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-----------|--------------|-------------|-----------|
| `video` | O vídeo de entrada a ser processado | VIDEO | Sim | Arquivo de vídeo |
| `green_shade` | Tom sólido de chroma-key aplicado atrás do primeiro plano: broadcast_green (#00B140), chroma_green (#00FF00) ou blue_screen (#0000FF) | STRING | Sim | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Observação:** O vídeo de entrada não deve exceder 60 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `video` | O vídeo processado com o fundo original substituído pelo tom de chroma-key selecionado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/pt-BR.md)

---
**Source fingerprint (SHA-256):** `663b41bf51bd8d871a59e756f226e4bf6244bb616ebcd2e8ccfa426137f2a05b`
