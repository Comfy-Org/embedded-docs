> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/pt-BR.md)

Gere uma imagem usando uma imagem de controle (canny). Este nó recebe uma imagem de controle e gera uma nova imagem com base no prompt fornecido, seguindo a estrutura de bordas detectada na imagem de controle.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Sim | - | A imagem de entrada usada para o controle de detecção de bordas canny |
| `prompt` | STRING | Não | - | Prompt para a geração da imagem (padrão: string vazia) |
| `prompt_upsampling` | BOOLEAN | Não | - | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma semente não produzirá exatamente o mesmo resultado). (padrão: False) |
| `canny_low_threshold` | FLOAT | Não | 0.01 - 0.99 | Limiar inferior para detecção de bordas Canny; ignorado se `skip_preprocessing` for True (padrão: 0.1) |
| `canny_high_threshold` | FLOAT | Não | 0.01 - 0.99 | Limiar superior para detecção de bordas Canny; ignorado se `skip_preprocessing` for True (padrão: 0.4) |
| `skip_preprocessing` | BOOLEAN | Não | - | Se deve pular o pré-processamento; defina como True se `control_image` já estiver no formato canny, False se for uma imagem bruta. (padrão: False) |
| `guidance` | FLOAT | Não | 1 - 100 | Força de orientação para o processo de geração de imagem (padrão: 30) |
| `steps` | INT | Não | 15 - 50 | Número de etapas para o processo de geração de imagem (padrão: 50) |
| `seed` | INT | Não | 0 - 18446744073709551615 | A semente aleatória usada para criar o ruído. (padrão: 0) |

**Nota:** Quando `skip_preprocessing` estiver definido como True, os parâmetros `canny_low_threshold` e `canny_high_threshold` são ignorados, pois presume-se que a imagem de controle já foi processada como uma imagem de bordas canny. A `control_image` é então usada diretamente como a imagem pré-processada.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output_image` | IMAGE | A imagem gerada com base na imagem de controle e no prompt |

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
