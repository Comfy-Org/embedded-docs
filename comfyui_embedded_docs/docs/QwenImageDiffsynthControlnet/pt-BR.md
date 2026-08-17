# QwenImageDiffsynthControlnet

O nó QwenImageDiffsynthControlnet aplica um patch de rede de controle de síntese por difusão para modificar o comportamento de um modelo base. Ele usa uma imagem de entrada e uma máscara opcional para orientar o processo de geração do modelo com intensidade ajustável, criando um modelo com patch que incorpora a influência da rede de controle para uma síntese de imagem mais controlada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo base a ser modificado com o patch da rede de controle | MODEL | Sim | - |
| `model_patch` | O modelo de patch da rede de controle a ser aplicado ao modelo base | MODEL_PATCH | Sim | - |
| `vae` | O VAE (Autoencoder Variacional) usado no processo de difusão | VAE | Sim | - |
| `image` | A imagem de entrada usada para orientar a rede de controle (apenas os canais RGB são usados) | IMAGE | Sim | - |
| `strength` | A intensidade da influência da rede de controle (padrão: 1.0) | FLOAT | Sim | -10.0 a 10.0 (passo: 0.01) |
| `mask` | Máscara opcional que define as áreas onde a rede de controle deve ser aplicada (invertida internamente) | MASK | Não | - |

**Observação:** Quando uma máscara é fornecida, ela é invertida automaticamente (1.0 - máscara) e redimensionada para corresponder às dimensões esperadas pelo processamento da rede de controle. Quando o patch do modelo é do tipo ZImage Control, o patch é aplicado tanto ao refinador de ruído quanto aos blocos duplos; para uma rede de controle DiffSynth padrão, apenas o patch do bloco duplo é aplicado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch da rede de controle de síntese por difusão aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
