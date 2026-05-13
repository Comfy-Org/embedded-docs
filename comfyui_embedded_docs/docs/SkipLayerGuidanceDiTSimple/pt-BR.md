> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/pt-BR.md)

Versão simplificada do nó SkipLayerGuidanceDiT que modifica apenas a passagem incondicional durante o processo de remoção de ruído. Este nó aplica orientação de salto de camada a camadas específicas do transformador em modelos DiT (Diffusion Transformer) ao pular seletivamente certas camadas durante a passagem incondicional com base em parâmetros de tempo e camada especificados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar a orientação de salto de camada |
| `double_layers` | STRING | Não | - | Lista separada por vírgulas dos índices das camadas de bloco duplo a pular (padrão: "7, 8, 9") |
| `single_layers` | STRING | Não | - | Lista separada por vírgulas dos índices das camadas de bloco único a pular (padrão: "7, 8, 9") |
| `start_percent` | FLOAT | Não | 0.0 - 1.0 | A porcentagem inicial do processo de remoção de ruído quando a orientação de salto de camada começa (padrão: 0.0) |
| `end_percent` | FLOAT | Não | 0.0 - 1.0 | A porcentagem final do processo de remoção de ruído quando a orientação de salto de camada para (padrão: 1.0) |

**Observação:** A orientação de salto de camada é aplicada apenas quando tanto `double_layers` quanto `single_layers` contêm índices de camada válidos. Se ambos estiverem vazios, o nó retorna o modelo original inalterado. A orientação de salto de camada fica ativa apenas quando o valor sigma da etapa atual de remoção de ruído está entre `start_percent` e `end_percent` (convertidos internamente para valores sigma).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com orientação de salto de camada aplicada às camadas especificadas |

---
**Source fingerprint (SHA-256):** `6795a67a63d9aa8b2adea3d96e49272d88c21d0642bb507e175a2fcf3a125f98`
