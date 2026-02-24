> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/pt-BR.md)

Cria uma sequência de quadros-chave de gancho com valores de força interpolados entre um ponto inicial e final. O nó gera múltiplos quadros-chave que fazem uma transição suave do parâmetro de força através de uma faixa de porcentagem especificada do processo de geração, usando vários métodos de interpolação para controlar a curva de transição.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `strength_start` | FLOAT | Sim | 0.0 - 10.0 | O valor de força inicial para a sequência de interpolação (padrão: 1.0) |
| `strength_end` | FLOAT | Sim | 0.0 - 10.0 | O valor de força final para a sequência de interpolação (padrão: 1.0) |
| `interpolation` | COMBO | Sim | Múltiplas opções disponíveis | O método de interpolação usado para transicionar entre os valores de força |
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | A posição percentual inicial no processo de geração (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | A posição percentual final no processo de geração (padrão: 1.0) |
| `keyframes_count` | INT | Sim | 2 - 100 | O número de quadros-chave a serem gerados na sequência de interpolação (padrão: 5) |
| `print_keyframes` | BOOLEAN | Sim | Verdadeiro/Falso | Se deve imprimir as informações dos quadros-chave gerados no log (padrão: Falso) |
| `prev_hook_kf` | HOOK_KEYFRAMES | Não | - | Grupo opcional de quadros-chave de gancho anteriores para anexar |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | O grupo de quadros-chave de gancho gerado contendo a sequência interpolada |
