> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/pt-BR.md)

O nó Pikaffects gera vídeos com vários efeitos visuais aplicados a uma imagem de entrada. Ele utiliza a API de geração de vídeo da Pika para transformar imagens estáticas em vídeos animados com efeitos específicos, como derretimento, explosão ou levitação. O nó requer uma chave de API e um token de autenticação para acessar o serviço da Pika.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de referência à qual aplicar o efeito Pikaffect. |
| `pikaffect` | COMBO | Sim | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | O efeito visual específico a ser aplicado à imagem (padrão: "Cake-ify"). |
| `prompt_text` | STRING | Sim | - | Descrição textual que orienta a geração do vídeo. |
| `negative_prompt` | STRING | Sim | - | Descrição textual do que evitar no vídeo gerado. |
| `seed` | INT | Sim | 0 a 4294967295 | Valor de semente aleatória para resultados reproduzíveis. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com o efeito Pikaffect aplicado. |
