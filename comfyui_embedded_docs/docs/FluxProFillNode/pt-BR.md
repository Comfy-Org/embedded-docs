> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/pt-BR.md)

Preenche imagens com base em máscara e prompt. Este nó utiliza o modelo Flux.1 para preencher áreas mascaradas de uma imagem de acordo com a descrição de texto fornecida, gerando novo conteúdo que se harmoniza com a imagem ao redor.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser preenchida |
| `mask` | MASK | Sim | - | A máscara que define quais áreas da imagem devem ser preenchidas |
| `prompt` | STRING | Não | - | Prompt para a geração da imagem (padrão: string vazia) |
| `prompt_upsampling` | BOOLEAN | Não | - | Se deve realizar *upsampling* no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma *seed* não produzirá exatamente o mesmo resultado). (padrão: false) |
| `guidance` | FLOAT | Não | 1.5-100 | Força de orientação para o processo de geração de imagem (padrão: 60) |
| `steps` | INT | Não | 15-50 | Número de etapas para o processo de geração de imagem (padrão: 50) |
| `seed` | INT | Não | 0-18446744073709551615 | A *seed* aleatória usada para criar o ruído. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output_image` | IMAGE | A imagem gerada com as áreas mascaradas preenchidas de acordo com o prompt |
