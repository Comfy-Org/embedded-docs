# Substituir Fundo de Vídeo Bria

Este nó substitui o fundo de um vídeo por uma imagem ou vídeo fornecido usando a API da Bria. A saída mantém a resolução e a taxa de quadros do vídeo em primeiro plano; um fundo com proporção diferente é esticado para se ajustar, portanto, proporções correspondentes produzem resultados sem distorção.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `video` | Vídeo em primeiro plano cujo fundo será substituído. | VIDEO | Sim | - |
| `background_image` | Imagem de fundo para compor atrás do primeiro plano. Forneça uma imagem de fundo ou um vídeo de fundo, não ambos. | IMAGE | Não | - |
| `background_video` | Vídeo de fundo para compor atrás do primeiro plano. Forneça uma imagem de fundo ou um vídeo de fundo, não ambos. | VIDEO | Não | - |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

**Observação:** Você deve fornecer exatamente um dos parâmetros `background_image` ou `background_video` — nem ambos e nem nenhum. O vídeo em primeiro plano deve ter no máximo 60 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `video` | O vídeo resultante com o fundo substituído. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4eb9650e5ca88baf2a91a9309b87936b3d18b88e314a56ab4c73d06a9143c645`
