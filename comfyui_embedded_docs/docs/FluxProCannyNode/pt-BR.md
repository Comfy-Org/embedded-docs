Gere uma imagem usando uma imagem de controle (canny). Este nó recebe uma imagem de controle e gera uma nova imagem com base no prompt fornecido, seguindo a estrutura de bordas detectada na imagem de controle.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `control_image` | A imagem de entrada usada para o controle de detecção de bordas canny | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia) | STRING | Não | - |
| `prompt_upsampling` | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma semente não produzirá exatamente o mesmo resultado). (padrão: False) | BOOLEAN | Não | - |
| `canny_low_threshold` | Limiar inferior para detecção de bordas Canny; ignorado se `skip_preprocessing` for True (padrão: 0.1) | FLOAT | Não | 0.01 - 0.99 |
| `canny_high_threshold` | Limiar superior para detecção de bordas Canny; ignorado se `skip_preprocessing` for True (padrão: 0.4) | FLOAT | Não | 0.01 - 0.99 |
| `skip_preprocessing` | Se deve pular o pré-processamento; defina como True se `control_image` já estiver no formato canny, False se for uma imagem bruta. (padrão: False) | BOOLEAN | Não | - |
| `guidance` | Força de orientação para o processo de geração de imagem (padrão: 30) | FLOAT | Não | 1 - 100 |
| `steps` | Número de etapas para o processo de geração de imagem (padrão: 50) | INT | Não | 15 - 50 |
| `seed` | A semente aleatória usada para criar o ruído. (padrão: 0) | INT | Não | 0 - 18446744073709551615 |

**Nota:** Quando `skip_preprocessing` estiver definido como True, os parâmetros `canny_low_threshold` e `canny_high_threshold` são ignorados, pois presume-se que a imagem de controle já foi processada como uma imagem de bordas canny. A `control_image` é então usada diretamente como a imagem pré-processada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output_image` | A imagem gerada com base na imagem de controle e no prompt | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
