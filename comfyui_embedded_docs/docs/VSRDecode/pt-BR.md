# VSR Decode

VSR Decode converte os latentes de keyframe do RelayVSR Conditioning de volta em um vídeo completo com o decodificador RelayVSR Flash. O decodificador adiciona seu detalhe sobre um upscale bicúbico dos quadros de baixa qualidade que você fornece, no fator x2 ou x4 do decodificador. A contagem de quadros permanece a mesma.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O decodificador RelayVSR Flash, carregado com Load VAE: `relayvsr_flash_vae_x2_fp32.safetensors` ou `relayvsr_flash_vae_x4_fp32.safetensors`. Os metadados do arquivo definem o fator de upscale, então ele precisa corresponder ao modelo. | VAE | Sim | N/A |
| `samples` | O latente retornado pelo sampler, carregando um quadro por keyframe. | LATENT | Sim | N/A |
| `images` | O mesmo vídeo de baixa qualidade fornecido ao RelayVSR Conditioning. | IMAGE | Sim | N/A |
| `detail` | Quanto do detalhe do decodificador é mantido sobre o upscale bicúbico: 1 é a saída completa do modelo, 0 é o upscale simples. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | O vídeo ampliado com cada quadro restaurado. | IMAGE |

## Notas

- Passe o mesmo vídeo de baixa qualidade para ambos os nós. O decodificador o lê quadro a quadro, então uma incompatibilidade no comprimento ou na resolução gera um resultado errado ou quebrado.
- Reduzir `detail` suaviza o detalhe restaurado e mantém a saída mais próxima de um upscale bicúbico simples, o que pode ajudar em fontes muito ruidosas.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VSRDecode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `946ac04bc9f205fd6d1088554caaa16238086e570f212e747b166e3fb0d9b3c5`
