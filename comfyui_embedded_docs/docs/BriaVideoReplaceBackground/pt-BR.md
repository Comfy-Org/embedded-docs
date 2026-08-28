# Bria Video Substituir Fundo

Este nó substitui o fundo de um vídeo por uma imagem ou vídeo fornecido usando a API da Bria. A saída mantém a resolução e a taxa de quadros do vídeo de primeiro plano; um fundo com proporção de aspecto diferente é esticado para caber, portanto, proporções de aspecto correspondentes produzem resultados sem distorção.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `vídeo` | Vídeo de primeiro plano cujo fundo será substituído. | VIDEO | Sim | - |
| `imagem_de_fundo` | Imagem de fundo para compor atrás do primeiro plano. Forneça uma imagem de fundo ou um vídeo de fundo, não ambos. | IMAGE | Não | - |
| `vídeo_de_fundo` | Vídeo de fundo para compor atrás do primeiro plano. Forneça uma imagem de fundo ou um vídeo de fundo, não ambos. | VIDEO | Não | - |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Observação:** Você deve fornecer exatamente um de `background_image` ou `background_video` — não ambos e também não nenhum. O vídeo de primeiro plano e o vídeo de fundo (se usado) devem ter no máximo 60 segundos cada. Quando `background_image` é usado, seu canal alfa é removido antes do processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `video` | O vídeo resultante com o fundo substituído, codificado como MP4 (H.264). | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
