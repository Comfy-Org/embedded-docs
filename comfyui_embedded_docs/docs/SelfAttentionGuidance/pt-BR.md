> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/pt-BR.md)

O nó Self-Attention Guidance aplica uma orientação a modelos de difusão modificando o mecanismo de atenção durante o processo de amostragem. Ele captura os escores de atenção das etapas de remoção de ruído incondicionais e os utiliza para criar mapas de orientação borrados que influenciam a saída final. Esta técnica ajuda a orientar o processo de geração aproveitando os próprios padrões de atenção do modelo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a orientação de auto-atenção |
| `scale` | FLOAT | Não | -2.0 a 5.0 | A intensidade do efeito de orientação de auto-atenção (padrão: 0.5) |
| `blur_sigma` | FLOAT | Não | 0.0 a 10.0 | A quantidade de borrão aplicada para criar o mapa de orientação (padrão: 2.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a orientação de auto-atenção aplicada |

**Observação:** Este nó é atualmente experimental e tem limitações com lotes divididos (chunked batches). Ele só pode salvar escores de atenção de uma chamada do UNet e pode não funcionar corretamente com tamanhos de lote maiores.
