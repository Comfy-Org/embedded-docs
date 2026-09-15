# Normalizar Imagens

Este nó normaliza as cores de uma imagem de entrada ajustando seus valores de pixel com base em uma média e um desvio padrão especificados. A média é subtraída de cada pixel e, em seguida, ele é dividido pelo desvio padrão, o que é uma etapa comum para padronizar dados de imagem antes de outros processamentos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser normalizada. | IMAGE | Sim | - |
| `mean` | Valor médio para normalização (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `std` | Desvio padrão para normalização (padrão: 0.5). | FLOAT | Não | 0.001 - 1.0 |

Os parâmetros `mean` e `std` controlam a normalização aplicada à imagem de entrada. O valor padrão para ambos os parâmetros é 0.5.

Observação: Se a imagem de entrada tiver um canal alfa (transparência), esse canal não é normalizado. Ele é copiado sem alterações para a saída porque o alfa armazena transparência, e não cor.

Observação: O nó funciona com qualquer tamanho de lote, portanto várias imagens podem ser processadas ao mesmo tempo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem resultante após a aplicação do processo de normalização. Os valores de pixel são ajustados usando a média e o desvio padrão especificados, e o canal alfa (se presente) é preservado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
