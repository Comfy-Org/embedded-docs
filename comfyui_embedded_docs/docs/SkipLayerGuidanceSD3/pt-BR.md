> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/pt-BR.md)

O nó **SkipLayerGuidanceSD3** aprimora a orientação para estruturas detalhadas ao aplicar um conjunto adicional de orientação livre de classificador com camadas ignoradas. Esta implementação experimental é inspirada na Orientação de Atenção Perturbada (*Perturbed Attention Guidance*) e funciona ignorando seletivamente certas camadas durante o processo de condicionamento negativo para melhorar os detalhes estruturais na saída gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sim | - | O modelo ao qual aplicar a orientação de camada ignorada |
| `camadas` | STRING | Sim | - | Lista separada por vírgulas dos índices das camadas a ignorar (padrão: "7, 8, 9") |
| `escala` | FLOAT | Sim | 0.0 - 10.0 | A intensidade do efeito de orientação de camada ignorada (padrão: 3.0) |
| `percentual_inicial` | FLOAT | Sim | 0.0 - 1.0 | O ponto inicial da aplicação da orientação como porcentagem do total de etapas (padrão: 0.01) |
| `percentual_final` | FLOAT | Sim | 0.0 - 1.0 | O ponto final da aplicação da orientação como porcentagem do total de etapas (padrão: 0.15) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `modelo` | MODEL | O modelo modificado com a orientação de camada ignorada aplicada |

---
**Source fingerprint (SHA-256):** `97c8220abd223bd35b4d0274c2b4536ffb6be7954ccd917943905bd22f60c1a5`
