> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/pt-BR.md)

O nó `ConditioningAverage` é usado para mesclar dois conjuntos diferentes de condicionamentos (como prompts de texto) de acordo com um peso especificado, gerando um novo vetor de condicionamento que se situa entre os dois. Ao ajustar o parâmetro de peso, você pode controlar de forma flexível a influência de cada condicionamento no resultado final. Isso é especialmente adequado para interpolação de prompts, fusão de estilos e outros casos de uso avançados.

Conforme mostrado abaixo, ajustando a força de `conditioning_to`, você pode obter um resultado intermediário entre os dois condicionamentos.

![example](./asset/example.webp)

## Entradas

| Parâmetro               | Tipo Comfy    | Descrição |
|------------------------|---------------|-------------|
| `conditioning_to`      | `CONDITIONING`| O vetor de condicionamento alvo, que serve como base principal para a média ponderada. |
| `conditioning_from`    | `CONDITIONING`| O vetor de condicionamento de origem, que será mesclado no alvo de acordo com um determinado peso. |
| `conditioning_to_strength` | `FLOAT`    | A força do condicionamento alvo, intervalo 0.0-1.0, padrão 1.0, passo 0.01. |

## Saídas

| Parâmetro        | Tipo Comfy    | Descrição |
|------------------|---------------|-------------|
| `conditioning`   | `CONDITIONING`| O vetor de condicionamento resultante após a mesclagem, refletindo a média ponderada. |

## Casos de Uso Típicos

- **Interpolação de Prompts:** Transicionar suavemente entre dois prompts de texto diferentes, gerando conteúdo com estilo ou semântica intermediários.
- **Fusão de Estilos:** Combinar diferentes estilos artísticos ou condições semânticas para criar efeitos novos.
- **Ajuste de Força:** Controlar com precisão a influência de um condicionamento específico no resultado, ajustando o peso.
- **Exploração Criativa:** Explorar diversos efeitos generativos misturando diferentes prompts.
