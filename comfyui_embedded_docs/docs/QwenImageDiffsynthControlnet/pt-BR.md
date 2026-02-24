> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/pt-BR.md)

O nó QwenImageDiffsynthControlnet aplica um patch de rede de controle de síntese por difusão para modificar o comportamento de um modelo base. Ele utiliza uma imagem de entrada e uma máscara opcional para orientar o processo de geração do modelo com força ajustável, criando um modelo modificado que incorpora a influência da rede de controle para uma síntese de imagem mais controlada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo base que será modificado com a rede de controle |
| `model_patch` | MODEL_PATCH | Sim | - | O modelo de patch da rede de controle a ser aplicado ao modelo base |
| `vae` | VAE | Sim | - | O VAE (Autoencoder Variacional) usado no processo de difusão |
| `image` | IMAGE | Sim | - | A imagem de entrada usada para orientar a rede de controle (apenas os canais RGB são usados) |
| `strength` | FLOAT | Sim | -10.0 a 10.0 | A força da influência da rede de controle (padrão: 1.0) |
| `mask` | MASK | Não | - | Máscara opcional que define as áreas onde a rede de controle deve ser aplicada (invertida internamente) |

**Observação:** Quando uma máscara é fornecida, ela é automaticamente invertida (1.0 - máscara) e redimensionada para corresponder às dimensões esperadas para o processamento da rede de controle.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com o patch da rede de controle de síntese por difusão aplicado |
