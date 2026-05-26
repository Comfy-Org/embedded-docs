> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/pt-BR.md)

## Visão Geral

O nó Not realiza uma operação lógica de negação (NOT) em qualquer valor de entrada. Ele retorna Verdadeiro (True) se o valor de entrada for considerado falso (como 0, string vazia, None, Falso), e retorna Falso (False) se o valor de entrada for verdadeiro. Utiliza as regras padrão do Python para determinar a veracidade.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `valor` | QUALQUER | Sim | Qualquer valor | O valor de entrada a ser invertido. Qualquer tipo de dado é aceito e avaliado usando as regras de veracidade do Python. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | BOOLEANO | O inverso lógico do valor de entrada. Retorna Verdadeiro se a entrada for falsa, Falso se a entrada for verdadeira. |

---
**Source fingerprint (SHA-256):** `fd8f940218538fce28079bc836379703c0e3c04f80351520497855c464176877`
