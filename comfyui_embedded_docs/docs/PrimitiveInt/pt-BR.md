# Inteiro

O nó PrimitiveInt fornece uma maneira simples de trabalhar com valores inteiros no seu fluxo de trabalho. Ele recebe uma entrada inteira e retorna o mesmo valor, sendo útil para passar parâmetros inteiros entre nós ou definir valores numéricos específicos para outras operações.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `value` | O valor inteiro a ser emitido (padrão: 0) | INT | Sim | -9223372036854775807 a 9223372036854775807 |

Nota: O parâmetro `value` está definido com um comportamento fixo de control-after-generate, portanto o valor não muda automaticamente após cada geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O valor inteiro de entrada repassado sem alterações | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
