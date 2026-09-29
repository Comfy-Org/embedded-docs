# ZImageFunControlnet

ZImageFunControlnet aplica um patch de rede de controle a um modelo base para que ele possa orientar o processo de geração ou edição de imagens. Ele combina um modelo, um patch de modelo e um VAE, e permite controlar quão fortemente o efeito de controle influencia o resultado. Entradas opcionais de imagem, imagem de inpainting e máscara permitem edições mais direcionadas. O nó funciona com patches Z-Image ControlNet e com patches Qwen Image 2.1 Fun ControlNet carregados através do nó Load Model Patch.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo base usado para o processo de geração. | MODEL | Sim | - |
| `patch_do_modelo` | Um patch de modelo especializado que aplica a orientação da rede de controle. | MODEL_PATCH | Sim | - |
| `vae` | O Autoencoder Variacional usado para codificar e decodificar imagens. | VAE | Sim | - |
| `força` | A força da influência da rede de controle. Valores positivos aplicam o efeito, enquanto valores negativos podem invertê-lo (padrão: 1.0). | FLOAT | Sim | -10.0 a 10.0 (passo 0.01) |
| `imagem` | Uma imagem base opcional para orientar o processo de geração. | IMAGE | Não | - |
| `imagem_para_retouch` | Uma imagem opcional usada especificamente para inpainting de áreas definidas por uma máscara. | IMAGE | Não | - |
| `máscara` | Uma máscara opcional que define quais áreas de uma imagem devem ser editadas ou preenchidas por inpainting. | MASK | Não | - |
| `start_percent` | O ponto no processo de denoising, como fração do total de etapas de amostragem, em que a rede de controle começa a fazer efeito (padrão: 0.0). | FLOAT | Não | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | O ponto no processo de denoising em que a rede de controle para de fazer efeito (padrão: 1.0). | FLOAT | Não | 0.0 a 1.0 (passo 0.001) |

**Nota:** O parâmetro `inpaint_image` normalmente é usado em conjunto com uma `mask` para especificar o conteúdo de inpainting. O comportamento do nó pode mudar dependendo de quais entradas opcionais são fornecidas (por exemplo, usar `image` para orientação ou usar `image`, `mask` e `inpaint_image` para inpainting). Os valores `start_percent` e `end_percent` restringem a rede de controle a uma janela do processo de denoising, e fora dessa janela o modelo é amostrado sem o patch. Se `strength` for 0, ou se nenhum de `image`, `inpaint_image` e `mask` estiver conectado, o nó retorna o modelo base inalterado. Para patches Z-Image Control, uma máscara fornecida é invertida (1.0 - mask) antes do uso, enquanto um patch Qwen Image 2.1 Fun ControlNet usa a máscara como fornecida. Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com o patch da rede de controle aplicado, pronto para uso em um pipeline de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9673b8b6e091713bcc93fe5fd1cfed12e6941571d1017e10ac94c19e1afd4ca1`
