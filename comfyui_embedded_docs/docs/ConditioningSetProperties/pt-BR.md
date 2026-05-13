> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/pt-BR.md)

O nó ConditioningSetProperties modifica as propriedades dos dados de condicionamento ajustando intensidade, configurações de área e aplicando máscaras opcionais, ganchos ou intervalos de timestep. Ele permite controlar como o condicionamento influencia o processo de geração, definindo parâmetros específicos que afetam a aplicação dos dados de condicionamento durante a geração de imagens.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|--------------|-----------------|--------|-------|-----------|
| `cond_NEW` | CONDITIONING | Obrigatório | - | - | Os dados de condicionamento a serem modificados |
| `strength` | FLOAT | Obrigatório | 1.0 | 0.0 - 10.0 (passo: 0.01) | Controla a intensidade do efeito de condicionamento |
| `set_cond_area` | STRING | Obrigatório | default | ["default", "mask bounds"] | Determina como a área de condicionamento é aplicada. Escolha "default" para comportamento padrão ou "mask bounds" para restringir à região da máscara |
| `mask` | MASK | Opcional | - | - | Máscara opcional para restringir onde o condicionamento é aplicado |
| `hooks` | HOOKS | Opcional | - | - | Funções de gancho opcionais para processamento personalizado |
| `timesteps` | TIMESTEPS_RANGE | Opcional | - | - | Intervalo de timestep opcional para limitar quando o condicionamento está ativo |

**Observação:** Quando uma `mask` é fornecida, o parâmetro `set_cond_area` pode ser definido como "mask bounds" para restringir a aplicação do condicionamento apenas à região mascarada. O parâmetro `hooks` permite processamento personalizado por meio de funções de gancho, e `timesteps` limita o efeito de condicionamento a um intervalo específico de timesteps durante a geração.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento modificados com propriedades atualizadas |

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
