# Edição de Vídeo Flux

Edita um clipe de vídeo existente a partir de uma instrução escrita. Você pode remover, adicionar ou substituir objetos, alterar o cenário, alterar o estilo da filmagem, alterar o texto na tela ou substituir o diálogo falado. A duração, o enquadramento, o movimento de câmera e o áudio vêm do clipe de origem, portanto, tudo o que você não mencionar no prompt deve permanecer como estava.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `vídeo` | Clipe de origem de 0.7 a 15 segundos, com pelo menos 160x160 pixels. A saída é renderizada a 24 fps e limitada a cerca de 0.9 megapixels por quadro, então uma origem maior retorna menor. | VIDEO | Sim | 0.7 a 15 segundos; mínimo 160x160 pixels |
| `prompt` | O que alterar, em linguagem simples, até 4096 caracteres. Tudo o que você não mencionar deve permanecer como estava. O diálogo de substituição precisa caber no tempo que a fala original leva, e um clipe silencioso permanece silencioso. Padrão: string vazia. | STRING | Sim | 1 a 4096 caracteres |
| `auto_downscale` | Reduz automaticamente a escala de origens maiores que 1280x704 pixels em área antes do envio. A proporção é preservada; vídeos menores não são alterados. Padrão: true. | BOOLEAN | Não | true<br>false |
| `safety_tolerance` | Tolerância de moderação; 0 é o mais restrito. Padrão: 4. | INT | Não | 0 a 4 |
| `seed` | Seed para determinar se o nó deve ser executado novamente; o FLUX escolhe sua própria seed, então os resultados reais são não determinísticos independentemente deste valor. Padrão: 42. | INT | Não | 0 a 4294967295 |

**Observação:** O `prompt` deve conter pelo menos 1 caractere e no máximo 4096 caracteres. O `video` de origem deve ter entre 0.7 e 15 segundos de duração e pelo menos 160x160 pixels; envios que estiverem fora desses limites são rejeitados antes de a solicitação ser enviada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O clipe de vídeo editado retornado pelo serviço FLUX. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `169b14700acfee3f6ccc247f08f3ae8c5f3c4610062a447e8215246460299b6a`
