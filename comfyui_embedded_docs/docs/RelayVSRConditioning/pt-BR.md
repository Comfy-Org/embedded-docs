# RelayVSRConditioning

O RelayVSR Conditioning prepara o condicionamento e o latent vazio para um upscale de vídeo com RelayVSR. O RelayVSR executa seu modelo Wan 2.2 de uma etapa apenas a cada 15º quadro do clipe, além do último, portanto o latent que ele entrega contém apenas esses quadros-chave. O VSR Decode então preenche os quadros entre eles.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão RelayVSR, carregado com Load Model: `relayvsr_x2_lightx2v_int8_convrot.safetensors` ou `relayvsr_x4_int8_convrot.safetensors`. | MODEL | Sim | N/A |
| `images` | O vídeo de baixa qualidade em sua resolução nativa. O fator de upscale do modelo determina o tamanho final do resultado. | IMAGE | Sim | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento que carrega os quadros-chave selecionados como orientação de baixa qualidade. | CONDITIONING |
| `latent` | Latent vazio com um quadro para cada quadro-chave, pronto para o sampler. | LATENT |

## Uso

Conecte `positive` à entrada positiva do sampler e, em seguida, faça a amostragem do `latent` com uma etapa em CFG 1: não há prompt nem codificador de texto no grafo. Envie a saída do sampler, as mesmas `images` e um RelayVSR Flash VAE para o VSR Decode, e mantenha o par correspondente: o modelo x2 com o decodificador x2, o modelo x4 com o decodificador x4.

Apenas os quadros-chave são amostrados, então um clipe de 150 quadros se transforma em um latent de 11 quadros. O sampler trabalha em uma pequena fração do vídeo, e o VSR Decode restaura o restante.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
