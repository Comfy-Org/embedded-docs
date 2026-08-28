# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet aplica um patch de rede de controle de síntese de difusão a um modelo base. Utiliza uma imagem de entrada e uma máscara opcional para guiar o processo de geração do modelo com intensidade ajustável, produzindo um modelo com patch que incorpora a influência da rede de controle para uma síntese de imagem mais controlada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo base a ser modificado com o patch da rede de controle | MODEL | Sim | - |
| `patch do modelo` | O modelo de patch da rede de controle a ser aplicado ao modelo base | MODEL_PATCH | Sim | - |
| `vae` | O VAE (Autoencoder Variacional) usado no processo de difusão | VAE | Sim | - |
| `imagem` | A imagem de entrada usada para guiar a rede de controle. Apenas os três primeiros canais de cor (RGB) são utilizados; quaisquer canais adicionais são descartados | IMAGE | Sim | - |
| `força` | A intensidade da influência da rede de controle (padrão: 1.0) | FLOAT | Sim | -10.0 a 10.0 |
| `máscara` | Máscara opcional que define as áreas onde a rede de controle deve ser aplicada. A máscara é invertida internamente antes do uso | MASK | Não | - |

**Observação:** Quando uma máscara é fornecida, ela é automaticamente invertida (1.0 - mask) e redimensionada para corresponder às dimensões esperadas para o processamento da rede de controle. O nó utiliza diferentes métodos internos de processamento dependendo se o patch do modelo é do tipo ZImage Control ou uma rede de controle DiffSynth padrão. Este nó é marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch da rede de controle de síntese de difusão aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
