> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/pt-BR.md)

Este nó gera imagens usando uma imagem de controle de profundidade como guia. Ele recebe uma imagem de controle e um prompt de texto, então cria uma nova imagem que segue tanto as informações de profundidade da imagem de controle quanto a descrição no prompt. O nó se conecta a uma API externa para realizar o processo de geração de imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Sim | - | A imagem de controle de profundidade usada para guiar a geração da imagem |
| `prompt` | STRING | Não | - | Prompt para a geração da imagem (padrão: string vazia) |
| `prompt_upsampling` | BOOLEAN | Não | - | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma seed não produzirá exatamente o mesmo resultado). (padrão: False) |
| `skip_preprocessing` | BOOLEAN | Não | - | Se deve pular o pré-processamento; defina como True se `control_image` já estiver com profundidade aplicada, False se for uma imagem bruta. (padrão: False) |
| `guidance` | FLOAT | Não | 1-100 | Força da orientação para o processo de geração de imagem (padrão: 15) |
| `steps` | INT | Não | 15-50 | Número de passos para o processo de geração de imagem (padrão: 50) |
| `seed` | INT | Não | 0-18446744073709551615 | A seed aleatória usada para criar o ruído. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output_image` | IMAGE | A imagem gerada com base na imagem de controle de profundidade e no prompt |
