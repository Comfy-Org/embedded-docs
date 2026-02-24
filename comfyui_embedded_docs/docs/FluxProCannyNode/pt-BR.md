> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/pt-BR.md)

Gere imagens usando uma imagem de controle (canny). Este nó recebe uma imagem de controle e gera uma nova imagem com base no prompt fornecido, seguindo a estrutura de bordas detectada na imagem de controle.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Sim | - | A imagem de entrada usada para o controle de detecção de bordas canny |
| `prompt` | STRING | Não | - | Prompt para a geração da imagem (padrão: string vazia) |
| `prompt_upsampling` | BOOLEAN | Não | - | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma seed não produzirá exatamente o mesmo resultado). (padrão: False) |
| `canny_low_threshold` | FLOAT | Não | 0.01 - 0.99 | Limite inferior para a detecção de bordas Canny; ignorado se skip_processing for True (padrão: 0.1) |
| `canny_high_threshold` | FLOAT | Não | 0.01 - 0.99 | Limite superior para a detecção de bordas Canny; ignorado se skip_processing for True (padrão: 0.4) |
| `skip_preprocessing` | BOOLEAN | Não | - | Se deve pular o pré-processamento; defina como True se a `control_image` já estiver processada como canny, False se for uma imagem bruta. (padrão: False) |
| `guidance` | FLOAT | Não | 1 - 100 | Força de orientação (guidance) para o processo de geração de imagem (padrão: 30) |
| `steps` | INT | Não | 15 - 50 | Número de etapas para o processo de geração de imagem (padrão: 50) |
| `seed` | INT | Não | 0 - 18446744073709551615 | A seed aleatória usada para criar o ruído. (padrão: 0) |

**Nota:** Quando `skip_preprocessing` é definido como True, os parâmetros `canny_low_threshold` e `canny_high_threshold` são ignorados, pois a imagem de controle é considerada já processada como uma imagem de bordas canny.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output_image` | IMAGE | A imagem gerada com base na imagem de controle e no prompt |
