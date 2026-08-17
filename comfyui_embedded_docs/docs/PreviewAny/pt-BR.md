# Pré-visualizar como Texto

O nó PreviewAny aceita qualquer valor de entrada e o exibe como texto legível na interface. Ele foi projetado para inspecionar e depurar valores em qualquer ponto do fluxo de trabalho: strings são repassadas inalteradas, números e booleanos são convertidos em texto, e outros objetos são formatados como JSON. O texto convertido também é passado adiante como saída de string, para que possa ser usado por outros nós.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `source` | O valor a ser visualizado como texto. Aceita qualquer tipo de dados. Strings são repassadas inalteradas; números e booleanos são convertidos em texto; outros valores são serializados em JSON com indentação. Se a serialização JSON falhar, a representação em string simples do valor é usada, e se isso também falhar, o texto "source exists, but could not be serialized." é exibido. | ANY | Sim | Qualquer tipo de dados |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `UI Text Display` | Exibe os dados de entrada convertidos em texto na interface do usuário. O mesmo texto também é retornado como saída de string para processamento adicional por outros nós. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
