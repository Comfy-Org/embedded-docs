# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet aplica um patch de rede de controle de síntese por difusão a um modelo base. Ele usa uma imagem de entrada e uma máscara opcional para orientar o processo de geração do modelo com força ajustável, produzindo um modelo com patch que incorpora a influência da rede de controle para uma síntese de imagem mais controlada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo base a receber o patch da rede de controle | MODEL | Sim | - |
| `patch do modelo` | O modelo de patch da rede de controle a ser aplicado ao modelo base | MODEL_PATCH | Sim | - |
| `vae` | O VAE (Autoencoder Variacional) usado no processo de difusão | VAE | Sim | - |
| `imagem` | A imagem de entrada usada para orientar a rede de controle. Apenas os três primeiros canais de cor (RGB) são usados; quaisquer canais adicionais são descartados | IMAGE | Sim | - |
| `força` | A força da influência da rede de controle (padrão: 1.0) | FLOAT | Sim | -10.0 a 10.0 (passo 0.01) |
| `máscara` | Máscara opcional que define as áreas onde a rede de controle deve ser aplicada. Para patches DiffSynth e Z-Image, a máscara é invertida internamente antes do uso | MASK | Não | - |
| `start_percent` | O ponto no processo de remoção de ruído, como uma fração do total de etapas de amostragem, em que a rede de controle começa a fazer efeito (padrão: 0.0) | FLOAT | Não | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | O ponto no processo de remoção de ruído em que a rede de controle deixa de fazer efeito (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 (passo 0.001) |

**Nota:** Os valores de `start_percent` e `end_percent` restringem a rede de controle a uma janela do processo de remoção de ruído; fora dessa janela, o modelo é amostrado sem o patch. Se `strength` for definido como 0, o nó retorna o modelo base inalterado. Quando uma máscara é fornecida, ela é invertida (1.0 - mask) e remodelada para os caminhos do Z-Image Control e do DiffSynth padrão, enquanto um patch do Qwen Image 2.1 Fun ControlNet usa a máscara como fornecida. O nó escolhe sua implementação interna de patch a partir do modelo de patch carregado, então as mesmas entradas se comportam de forma um pouco diferente para Z-Image Control, Qwen Image 2.1 Fun ControlNet e checkpoints DiffSynth padrão. Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch da rede de controle de síntese por difusão aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7be42c001c2937af7ca5c2d45aa8a529574aa9117b4740c62da822910041d231`
