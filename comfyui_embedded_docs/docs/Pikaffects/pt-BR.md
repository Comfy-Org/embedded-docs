> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/pt-BR.md)

O nó Pikaffects gera vídeos com diversos efeitos visuais aplicados a uma imagem de entrada. Ele utiliza a API de geração de vídeos da Pika para transformar imagens estáticas em vídeos animados com efeitos específicos, como derretimento, explosão ou levitação. O nó requer uma chave de API e um token de autenticação para acessar o serviço Pika.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de referência para aplicar o Pikaffect. |
| `pikaffect` | COMBO | Sim | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | O efeito visual específico a ser aplicado na imagem (padrão: "Cake-ify"). |
| `prompt_text` | STRING | Sim | - | Descrição textual que orienta a geração do vídeo. |
| `negative_prompt` | STRING | Sim | - | Descrição textual do que deve ser evitado no vídeo gerado. |
| `seed` | INT | Sim | 0 a 4294967295 | Valor de semente aleatória para resultados reproduzíveis. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado com o Pikaffect aplicado. |

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`
