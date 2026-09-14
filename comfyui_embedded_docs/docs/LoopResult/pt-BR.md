# LoopResult

LoopResult é um nó de saída exclusivo para desenvolvedores que marca o ponto de encerramento de um bloco de loop. Ele coleta os valores passados para ele em ordem (nomeados `output0`, `output1` e assim por diante) e libera o bloco de execução externo identificado por um ID de fechamento. Como o fingerprint de entrada sempre retorna NaN, o nó é tratado como sempre alterado e é reexecutado a cada execução.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `close_id` | Identificador do bloco de loop a fechar; apenas o primeiro valor da lista é usado | STRING | Sim | - |
| `output0`, `output1`, ... | Valores coletados do bloco de loop. O nó aceita quaisquer entradas adicionais e as reúne em ordem sequencial começando em `output0`, parando no primeiro índice ausente | Qualquer tipo | Não | - |

Observação: este nó aceita todas as entradas (`accept_all_inputs`). Qualquer entrada além de `close_id` é tratada como um valor de loop coletado e deve ser nomeada `output0`, `output1`, `output2` etc., sem lacunas, para ser incluída no resultado.

## Saídas

Este nó não retorna nenhuma saída. Ele apenas libera o bloco de execução externo associado a `close_id`.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopResult/pt-BR.md)

---
**Source fingerprint (SHA-256):** `637f8a39b0e99e8d4453cfc482463bd14d909b710264021ac2c27fdcd68b6063`
