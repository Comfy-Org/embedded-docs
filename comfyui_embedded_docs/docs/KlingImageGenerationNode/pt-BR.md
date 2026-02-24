> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/pt-BR.md)

O nó Kling Image Generation gera imagens a partir de prompts de texto com a opção de usar uma imagem de referência para orientação. Ele cria uma ou mais imagens com base na sua descrição textual e configurações de referência, retornando as imagens geradas como saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo |
| `image_type` | COMBO | Sim | Opções de KlingImageGenImageReferenceType<br>(extraídas do código-fonte) | Seleção do tipo de referência de imagem |
| `image_fidelity` | FLOAT | Sim | 0.0 - 1.0 | Intensidade de referência para imagens enviadas pelo usuário (padrão: 0.5) |
| `human_fidelity` | FLOAT | Sim | 0.0 - 1.0 | Similaridade de referência do assunto (padrão: 0.45) |
| `model_name` | COMBO | Sim | "kling-v1"<br>(e outras opções de KlingImageGenModelName) | Seleção do modelo para geração de imagem (padrão: "kling-v1") |
| `aspect_ratio` | COMBO | Sim | "16:9"<br>(e outras opções de KlingImageGenAspectRatio) | Proporção da imagem gerada (padrão: "16:9") |
| `n` | INT | Sim | 1 - 9 | Número de imagens geradas (padrão: 1) |
| `image` | IMAGE | Não | - | Imagem de referência opcional |

**Restrições dos Parâmetros:**

- O parâmetro `image` é opcional, mas quando fornecido, o modelo kling-v1 não suporta imagens de referência
- O prompt e o prompt negativo têm limitações de comprimento máximo (MAX_PROMPT_LENGTH_IMAGE_GEN)
- Quando nenhuma imagem de referência é fornecida, o parâmetro `image_type` é automaticamente definido como None

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | Imagem(ns) gerada(s) com base nos parâmetros de entrada |
