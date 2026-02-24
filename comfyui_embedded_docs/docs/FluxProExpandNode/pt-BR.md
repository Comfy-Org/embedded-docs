> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/pt-BR.md)

Expande uma imagem com base em um prompt. Este nó expande uma imagem adicionando pixels às bordas superior, inferior, esquerda e direita, enquanto gera novo conteúdo que corresponde à descrição de texto fornecida.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser expandida |
| `prompt` | STRING | Não | - | Prompt para a geração da imagem (padrão: "") |
| `prompt_upsampling` | BOOLEAN | Não | - | Se deve realizar *upsampling* no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma *seed* não produzirá exatamente o mesmo resultado). (padrão: False) |
| `top` | INT | Não | 0-2048 | Número de pixels para expandir na parte superior da imagem (padrão: 0) |
| `bottom` | INT | Não | 0-2048 | Número de pixels para expandir na parte inferior da imagem (padrão: 0) |
| `left` | INT | Não | 0-2048 | Número de pixels para expandir no lado esquerdo da imagem (padrão: 0) |
| `right` | INT | Não | 0-2048 | Número de pixels para expandir no lado direito da imagem (padrão: 0) |
| `guidance` | FLOAT | Não | 1.5-100 | Força de orientação (*guidance*) para o processo de geração da imagem (padrão: 60) |
| `steps` | INT | Não | 15-50 | Número de etapas para o processo de geração da imagem (padrão: 50) |
| `seed` | INT | Não | 0-18446744073709551615 | A *seed* aleatória usada para criar o ruído. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem de saída expandida |
