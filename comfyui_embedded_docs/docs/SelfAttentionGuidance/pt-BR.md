O nó Self-Attention Guidance aplica orientação a modelos de difusão modificando o mecanismo de atenção durante o processo de amostragem. Ele captura pontuações de atenção das etapas de remoção de ruído incondicionais e as utiliza para criar mapas de orientação desfocados que influenciam o resultado final. Esta técnica ajuda a guiar o processo de geração aproveitando os próprios padrões de atenção do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar a orientação por autoatenção | MODEL | Sim | - |
| `escala` | A intensidade do efeito de orientação por autoatenção (padrão: 0.5) | FLOAT | Não | -2.0 a 5.0 |
| `sigma_de_desfoque` | A quantidade de desfoque aplicada para criar o mapa de orientação (padrão: 2.0) | FLOAT | Não | 0.0 a 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com orientação por autoatenção aplicada | MODEL |

**Observação:** Este nó é atualmente experimental e possui limitações com lotes fragmentados. Ele só pode salvar pontuações de atenção de uma chamada UNet e pode não funcionar corretamente com tamanhos de lote maiores.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f16ecd8f74bfd71073c6e3a65be08e54e4f5b9c56fe08deb48f35df381e82fa`
