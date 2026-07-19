# Pikaffects

O nó Pikaffects gera vídeos com diversos efeitos visuais aplicados a uma imagem de entrada. Ele utiliza a API de geração de vídeos da Pika para transformar imagens estáticas em vídeos animados com efeitos específicos, como derretimento, explosão ou levitação. O nó requer uma chave de API e um token de autenticação para acessar o serviço Pika.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de referência para aplicar o Pikaffect. | IMAGE | Sim | - |
| `pikaffect` | O efeito visual específico a ser aplicado na imagem (padrão: "Cake-ify"). | COMBO | Sim | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | Descrição textual que orienta a geração do vídeo. | STRING | Sim | - |
| `negative_prompt` | Descrição textual do que deve ser evitado no vídeo gerado. | STRING | Sim | - |
| `seed` | Valor de semente aleatória para resultados reproduzíveis. | INT | Sim | 0 a 4294967295 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado com o Pikaffect aplicado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/pt-BR.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`
