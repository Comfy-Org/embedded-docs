# MOSS-Image Color/Depth Control

Adiciona os mapas de região de cor e de profundidade de um adaptador de controle de cor/profundidade do MOSS-Image ao condicionamento. Conecte os condicionamentos positivo e negativo, um VAE e um ou ambos os mapas: os mapas são codificados em latentes, unidos em um sinal de controle de cor/profundidade e anexados ao condicionamento para a parte da amostragem que você escolher. Use-o em conjunto com um adaptador de controle do MOSS-Image carregado por meio de um carregador LoRA.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condicionamento positivo ao qual anexar o sinal de controle. | CONDITIONING | Sim | N/A |
| `negative` | Condicionamento negativo ao qual anexar o sinal de controle. | CONDITIONING | Sim | N/A |
| `vae` | VAE usada para codificar os mapas em latentes. | VAE | Sim | N/A |
| `color_map` | Uma cor sólida por região, no tamanho da saída. As cores são apenas IDs de região. | IMAGE | Não | N/A |
| `depth_map` | Mapa de profundidade no tamanho da saída, em que o que está próximo é branco. | IMAGE | Não | N/A |
| `strength` | Escala a contribuição dos mapas para os tokens da imagem. 0.0 é o mesmo que nenhum mapa; 1.0 é a intensidade treinada (padrão: 1.0). | FLOAT | Sim | 0.0 a 10.0 (passo 0.01) |
| `start_percent` | Percentual de amostragem em que o controle começa (padrão: 0.0). | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | Percentual de amostragem em que o controle termina. Terminar mais cedo mantém o layout e a profundidade enquanto o restante das etapas relaxa as formas (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |

**Nota:** Conecte pelo menos um entre `color_map` e `depth_map`; sem nenhum deles, o nó retorna os condicionamentos inalterados. Um mapa ausente é substituído por zeros, portanto configurações somente com cor e somente com profundidade funcionam. Quando os dois mapas tiverem tamanhos diferentes, o menor é ampliado para o tamanho do outro. Este nó está marcado como experimental no ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento positivo com o sinal de controle anexado. | CONDITIONING |
| `negative` | O condicionamento negativo com o sinal de controle anexado. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageControl/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c4a40c76f26237408e47cb9f683c13bccc3507bd775bec1b89919947a308c115`
