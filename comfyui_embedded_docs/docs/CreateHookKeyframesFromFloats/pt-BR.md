> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/pt-BR.md)

Este nó cria keyframes de hook a partir de uma lista de valores de intensidade em ponto flutuante, distribuindo-os uniformemente entre percentuais inicial e final especificados. Ele gera uma sequência de keyframes onde cada valor de intensidade é atribuído a uma posição percentual específica na linha do tempo da animação. O nó pode criar um novo grupo de keyframes ou adicionar a um existente, com uma opção para imprimir os keyframes gerados para fins de depuração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `força_floats` | FLOATS | Sim | -1 a ∞ | Um único valor float ou lista de valores float representando valores de intensidade para os keyframes (padrão: -1) |
| `percentual_inicial` | FLOAT | Sim | 0,0 a 1,0 | A posição percentual inicial para o primeiro keyframe na linha do tempo (padrão: 0,0) |
| `percentual_final` | FLOAT | Sim | 0,0 a 1,0 | A posição percentual final para o último keyframe na linha do tempo (padrão: 1,0) |
| `imprimir_quadros-chave` | BOOLEAN | Sim | Verdadeiro/Falso | Quando ativado, imprime as informações do keyframe gerado no console (padrão: Falso) |
| `quadro-chave_gancho_anterior` | HOOK_KEYFRAMES | Não | - | Um grupo de keyframes de hook existente para adicionar os novos keyframes, ou cria um novo grupo se não for fornecido |

**Nota:** O parâmetro `floats_strength` aceita um único valor float ou uma lista iterável de floats. Os keyframes são distribuídos linearmente entre `start_percent` e `end_percent` com base no número de valores de intensidade fornecidos. O primeiro keyframe tem garantia de pelo menos um passo para garantir que seja aplicado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|---------------|-----------|
| `HOOK_KF` | HOOK_KEYFRAMES | Um grupo de keyframes de hook contendo os keyframes recém-criados, seja como um novo grupo ou anexado ao grupo de keyframes de entrada |

---
**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`
