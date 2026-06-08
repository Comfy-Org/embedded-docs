O nó **ExtendIntermediateSigmas** recebe uma sequência existente de valores sigma e insere valores sigma intermediários adicionais entre eles. Ele permite especificar quantos passos extras adicionar, o método de espaçamento para interpolação e limites opcionais de sigma inicial e final para controlar onde a extensão ocorre dentro da sequência sigma.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `sigmas` | A sequência sigma de entrada a ser estendida com valores intermediários | SIGMAS | Sim | - |
| `passos` | Número de passos intermediários a inserir entre sigmas existentes (padrão: 2) | INT | Sim | 1 a 100 |
| `iniciar_em_sigma` | Limite superior sigma para extensão — estende apenas sigmas abaixo deste valor (padrão: -1.0, que significa infinito) | FLOAT | Sim | -1.0 a 20000.0 |
| `terminar_em_sigma` | Limite inferior sigma para extensão — estende apenas sigmas acima deste valor (padrão: 12.0) | FLOAT | Sim | 0.0 a 20000.0 |
| `espaçamento` | O método de interpolação para espaçar os valores sigma intermediários (padrão: "linear") | COMBO | Sim | `"linear"`<br>`"cosseno"`<br>`"seno"` |

**Nota:** O nó insere sigmas intermediários apenas entre pares de sigmas existentes onde ambos o sigma atual é menor ou igual a `start_at_sigma` e maior ou igual a `end_at_sigma`. Quando `start_at_sigma` é definido como -1.0, ele é tratado como infinito, significando que apenas o limite inferior `end_at_sigma` se aplica.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | A sequência sigma estendida com valores intermediários adicionais inseridos | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f51ed433fc38365334ff8e4072174dc04982a8a00770d07f544320a6863577c4`
