> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/pt-BR.md)

Cria uma sequência de keyframes de hook com valores de intensidade interpolados entre um ponto inicial e final. O nó gera múltiplos keyframes que fazem a transição suave do parâmetro de intensidade ao longo de uma faixa percentual especificada do processo de geração, utilizando vários métodos de interpolação para controlar a curva de transição.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `strength_start` | FLOAT | Sim | 0.0 - 10.0 | O valor inicial de intensidade para a sequência de interpolação (padrão: 1.0) |
| `strength_end` | FLOAT | Sim | 0.0 - 10.0 | O valor final de intensidade para a sequência de interpolação (padrão: 1.0) |
| `interpolation` | COMBO | Sim | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` | O método de interpolação usado para fazer a transição entre os valores de intensidade (padrão: LINEAR) |
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | A posição percentual inicial no processo de geração (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | A posição percentual final no processo de geração (padrão: 1.0) |
| `keyframes_count` | INT | Sim | 2 - 100 | O número de keyframes a serem gerados na sequência de interpolação (padrão: 5) |
| `print_keyframes` | BOOLEAN | Sim | True/False | Se deve imprimir as informações dos keyframes gerados no log (padrão: False) |
| `prev_hook_kf` | HOOK_KEYFRAMES | Não | - | Grupo opcional de keyframes de hook anterior para anexar |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `HOOK_KF` | HOOK_KEYFRAMES | O grupo de keyframes de hook gerado contendo a sequência interpolada |

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
