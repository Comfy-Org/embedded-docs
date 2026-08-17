# Bria Video Substituir Fundo

Substitua o fundo de um vídeo por uma imagem ou vídeo fornecido usando Bria. A saída mantém a resolução e a taxa de quadros do primeiro plano; um fundo com proporção de aspecto diferente é esticado para caber, portanto, ajuste-o para obter resultados sem distorção.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `video` | Vídeo de primeiro plano cujo fundo será substituído. | VIDEO | Sim | - |
| `background_image` | Imagem de fundo para compor atrás do primeiro plano. Forneça uma imagem de fundo ou um vídeo de fundo, não ambos. | IMAGE | Não | - |
| `background_video` | Vídeo de fundo para compor atrás do primeiro plano. Forneça uma imagem de fundo ou um vídeo de fundo, não ambos. | VIDEO | Não | - |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Nota:** Você deve fornecer exatamente uma das opções `background_image` ou `background_video` — não ambas e não nenhuma. Tanto o vídeo de primeiro plano quanto o de fundo devem ter 60 segundos ou menos. Se uma imagem de fundo for fornecida, seu canal alfa (transparência) é removido antes do envio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo resultante com o fundo substituído. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
