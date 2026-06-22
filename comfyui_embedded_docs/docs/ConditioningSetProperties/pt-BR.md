# Props de Cond Set

O nó ConditioningSetProperties modifica as propriedades dos dados de condicionamento ajustando intensidade, configurações de área e aplicando máscaras opcionais, ganchos ou intervalos de timestep. Ele permite controlar como o condicionamento influencia o processo de geração, definindo parâmetros específicos que afetam a aplicação dos dados de condicionamento durante a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `cond_NOVO` | Os dados de condicionamento a serem modificados | CONDITIONING | Obrigatório | - | - |
| `força` | Controla a intensidade do efeito de condicionamento | FLOAT | Obrigatório | 1.0 | 0.0 - 10.0 (passo: 0.01) |
| `definir_área_cond` | Determina como a área de condicionamento é aplicada. Escolha "default" para comportamento padrão ou "mask bounds" para restringir à região da máscara | STRING | Obrigatório | default | ["default", "mask bounds"] |
| `mask` | Máscara opcional para restringir onde o condicionamento é aplicado | MASK | Opcional | - | - |
| `ganchos` | Funções de gancho opcionais para processamento personalizado | HOOKS | Opcional | - | - |
| `etapas_de_tempo` | Intervalo de timestep opcional para limitar quando o condicionamento está ativo | TIMESTEPS_RANGE | Opcional | - | - |

**Observação:** Quando uma `mask` é fornecida, o parâmetro `set_cond_area` pode ser definido como "mask bounds" para restringir a aplicação do condicionamento apenas à região mascarada. O parâmetro `hooks` permite processamento personalizado por meio de funções de gancho, e `timesteps` limita o efeito de condicionamento a um intervalo específico de timesteps durante a geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento modificados com propriedades atualizadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
