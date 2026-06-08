O nó **SkipLayerGuidanceSD3** aprimora a orientação para estruturas detalhadas ao aplicar um conjunto adicional de orientação livre de classificador com camadas ignoradas. Esta implementação experimental é inspirada na Orientação de Atenção Perturbada (*Perturbed Attention Guidance*) e funciona ignorando seletivamente certas camadas durante o processo de condicionamento negativo para melhorar os detalhes estruturais na saída gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar a orientação de camada ignorada | MODEL | Sim | - |
| `camadas` | Lista separada por vírgulas dos índices das camadas a ignorar (padrão: "7, 8, 9") | STRING | Sim | - |
| `escala` | A intensidade do efeito de orientação de camada ignorada (padrão: 3.0) | FLOAT | Sim | 0.0 - 10.0 |
| `percentual_inicial` | O ponto inicial da aplicação da orientação como porcentagem do total de etapas (padrão: 0.01) | FLOAT | Sim | 0.0 - 1.0 |
| `percentual_final` | O ponto final da aplicação da orientação como porcentagem do total de etapas (padrão: 0.15) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com a orientação de camada ignorada aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `97c8220abd223bd35b4d0274c2b4536ffb6be7954ccd917943905bd22f60c1a5`
