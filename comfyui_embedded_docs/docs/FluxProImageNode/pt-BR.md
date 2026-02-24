> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/pt-BR.md)

Gera imagens de forma síncrona com base em um prompt e resolução. Este nó cria imagens usando o modelo Flux 1.1 Pro enviando requisições para um endpoint de API e aguardando a resposta completa antes de retornar a imagem gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: string vazia) |
| `prompt_upsampling` | BOOLEAN | Sim | - | Define se deve realizar *upsampling* no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma *seed* não produzirá exatamente o mesmo resultado). (padrão: False) |
| `width` | INT | Sim | 256-1440 | Largura da imagem em pixels (padrão: 1024, passo: 32) |
| `height` | INT | Sim | 256-1440 | Altura da imagem em pixels (padrão: 768, passo: 32) |
| `seed` | INT | Sim | 0-18446744073709551615 | A *seed* aleatória usada para criar o ruído. (padrão: 0) |
| `image_prompt` | IMAGE | Não | - | Imagem de referência opcional para guiar a geração |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem gerada retornada pela API |
