# Criar Interp. de Keyframes do Hook

Cria uma sequência de keyframes de hook com valores de intensidade interpolados entre um ponto inicial e final. O nó gera múltiplos keyframes que fazem a transição suave do parâmetro de intensidade ao longo de uma faixa percentual especificada do processo de geração, utilizando vários métodos de interpolação para controlar a curva de transição.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `força_inicial` | O valor inicial de intensidade para a sequência de interpolação (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `força_final` | O valor final de intensidade para a sequência de interpolação (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `interpolação` | O método de interpolação usado para fazer a transição entre os valores de intensidade (padrão: LINEAR) | COMBO | Sim | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` |
| `percentual_inicial` | A posição percentual inicial no processo de geração (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `percentual_final` | A posição percentual final no processo de geração (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `quantidade_keyframes` | O número de keyframes a serem gerados na sequência de interpolação (padrão: 5) | INT | Sim | 2 - 100 |
| `imprimir_keyframes` | Se deve imprimir as informações dos keyframes gerados no log (padrão: False) | BOOLEAN | Sim | True/False |
| `hook_kf_anterior` | Grupo opcional de keyframes de hook anterior para anexar | HOOK_KEYFRAMES | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `HOOK_KF` | O grupo de keyframes de hook gerado contendo a sequência interpolada | HOOK_KEYFRAMES |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
