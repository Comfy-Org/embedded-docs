> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/pt-BR.md)

Este nó gera imagens de forma síncrona usando o modelo Stable Diffusion 3.5 da Stability AI. Ele cria imagens com base em prompts de texto e também pode modificar imagens existentes quando fornecidas como entrada. O nó suporta várias proporções de aspecto e predefinições de estilo para personalizar o resultado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. (padrão: string vazia) |
| `model` | COMBO | Sim | Múltiplas opções disponíveis | O modelo Stable Diffusion 3.5 a ser usado para a geração. |
| `aspect_ratio` | COMBO | Sim | Múltiplas opções disponíveis | Proporção de aspecto da imagem gerada. (padrão: proporção 1:1) |
| `style_preset` | COMBO | Não | Múltiplas opções disponíveis | Estilo desejado opcional para a imagem gerada. |
| `cfg_scale` | FLOAT | Sim | 1.0 a 10.0 | Quão estritamente o processo de difusão adere ao texto do prompt (valores mais altos mantêm sua imagem mais próxima do seu prompt). (padrão: 4.0) |
| `seed` | INT | Sim | 0 a 4294967294 | A semente aleatória usada para criar o ruído. (padrão: 0) |
| `image` | IMAGE | Não | - | Imagem de entrada opcional para geração de imagem para imagem. |
| `negative_prompt` | STRING | Não | - | Palavras-chave do que você não deseja ver na imagem de saída. Este é um recurso avançado. (padrão: string vazia) |
| `image_denoise` | FLOAT | Não | 0.0 a 1.0 | Desfoque da imagem de entrada; 0.0 resulta em uma imagem idêntica à entrada, 1.0 é como se nenhuma imagem fosse fornecida. (padrão: 0.5) |

**Observação:** Quando uma `image` é fornecida, o nó muda para o modo de geração de imagem para imagem e o parâmetro `aspect_ratio` é determinado automaticamente a partir da imagem de entrada. Quando nenhuma `image` é fornecida, o parâmetro `image_denoise` é ignorado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem gerada ou modificada. |
