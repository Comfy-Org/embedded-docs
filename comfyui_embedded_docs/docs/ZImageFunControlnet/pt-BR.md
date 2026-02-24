> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/pt-BR.md)

O nó ZImageFunControlnet aplica uma rede de controle especializada para influenciar o processo de geração ou edição de imagem. Ele utiliza um modelo base, um patch de modelo e um VAE, permitindo que você ajuste a intensidade do efeito de controle. Este nó pode trabalhar com uma imagem base, uma imagem para inpainting e uma máscara para edições mais direcionadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo base utilizado para o processo de geração. |
| `model_patch` | MODEL_PATCH | Sim | - | Um modelo de patch especializado que aplica a orientação da rede de controle. |
| `vae` | VAE | Sim | - | O Autoencoder Variacional utilizado para codificar e decodificar imagens. |
| `strength` | FLOAT | Sim | -10.0 a 10.0 | A intensidade da influência da rede de controle. Valores positivos aplicam o efeito, enquanto valores negativos podem invertê-lo (padrão: 1.0). |
| `image` | IMAGE | Não | - | Uma imagem base opcional para orientar o processo de geração. |
| `inpaint_image` | IMAGE | Não | - | Uma imagem opcional usada especificamente para preencher áreas definidas por uma máscara (inpainting). |
| `mask` | MASK | Não | - | Uma máscara opcional que define quais áreas de uma imagem devem ser editadas ou preenchidas. |

**Observação:** O parâmetro `inpaint_image` é tipicamente usado em conjunto com uma `mask` para especificar o conteúdo para inpainting. O comportamento do nó pode mudar com base em quais entradas opcionais são fornecidas (por exemplo, usar `image` para orientação ou usar `image`, `mask` e `inpaint_image` para inpainting).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo com o patch da rede de controle aplicado, pronto para uso em um pipeline de amostragem. |
| `positive` | CONDITIONING | O condicionamento positivo, potencialmente modificado pelas entradas da rede de controle. |
| `negative` | CONDITIONING | O condicionamento negativo, potencialmente modificado pelas entradas da rede de controle. |
