> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/pt-BR.md)

Melhora a orientação para detalhes estruturais usando outro conjunto de CFG negativo com camadas ignoradas. Esta versão genérica do SkipLayerGuidance pode ser usada em qualquer modelo DiT e é inspirada no Perturbed Attention Guidance. A implementação experimental original foi criada para o SD3.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sim | - | O modelo ao qual aplicar a orientação de camada ignorada |
| `camadas duplas` | STRING | Sim | - | Números de camadas separados por vírgula para blocos duplos a serem ignorados (padrão: "7, 8, 9") |
| `camadas simples` | STRING | Sim | - | Números de camadas separados por vírgula para blocos simples a serem ignorados (padrão: "7, 8, 9") |
| `escala` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala da orientação (padrão: 3.0) |
| `percentual inicial` | FLOAT | Sim | 0.0 - 1.0 | Percentual inicial para aplicação da orientação (padrão: 0.01) |
| `percentual final` | FLOAT | Sim | 0.0 - 1.0 | Percentual final para aplicação da orientação (padrão: 0.15) |
| `escala de reescalonamento` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala de redimensionamento para ajustar a magnitude da saída (padrão: 0.0, significando sem redimensionamento) |

**Nota:** Se tanto `double_layers` quanto `single_layers` estiverem vazios (não contiverem números de camadas), o nó retorna o modelo original sem aplicar nenhuma orientação.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `modelo` | MODEL | O modelo modificado com a orientação de camada ignorada aplicada |

---
**Source fingerprint (SHA-256):** `cf494fbeb33e7bc3b3f798e9e9b025623afad4ea6340ef628caa776c7d42ba12`
