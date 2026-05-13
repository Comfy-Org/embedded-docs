> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/pt-BR.md)

O nó QwenImageDiffsynthControlnet aplica um patch de rede de controle de síntese de difusão para modificar o comportamento de um modelo base. Ele utiliza uma entrada de imagem e uma máscara opcional para guiar o processo de geração do modelo com intensidade ajustável, criando um modelo com patch que incorpora a influência da rede de controle para uma síntese de imagem mais controlada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo base a ser modificado com o patch da rede de controle |
| `model_patch` | MODEL_PATCH | Sim | - | O modelo de patch da rede de controle a ser aplicado ao modelo base |
| `vae` | VAE | Sim | - | O VAE (Autoencoder Variacional) utilizado no processo de difusão |
| `image` | IMAGE | Sim | - | A imagem de entrada usada para guiar a rede de controle (apenas os canais RGB são utilizados) |
| `strength` | FLOAT | Sim | -10.0 a 10.0 | A intensidade da influência da rede de controle (padrão: 1.0) |
| `mask` | MASK | Não | - | Máscara opcional que define áreas onde a rede de controle deve ser aplicada (invertida internamente) |

**Observação:** Quando uma máscara é fornecida, ela é automaticamente invertida (1.0 - máscara) e redimensionada para corresponder às dimensões esperadas para o processamento da rede de controle. O nó utiliza diferentes métodos de processamento interno dependendo se o patch do modelo é do tipo ZImage Control ou uma rede de controle DiffSynth padrão.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model` | MODEL | O modelo modificado com o patch da rede de controle de síntese de difusão aplicado |

---
**Source fingerprint (SHA-256):** `61833984d0b92be65fae72a894806572c0588dea74a295e8289d1194dee611bb`
