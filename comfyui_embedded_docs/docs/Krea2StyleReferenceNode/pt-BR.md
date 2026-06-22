# Krea 2 Referência de Estilo

## Visão Geral

O nó Krea 2 Style Reference permite adicionar uma imagem de referência para influenciar o estilo de uma geração de imagem Krea 2. Você pode encadear múltiplas referências de estilo (até 10 no total) e alimentar o resultado combinado em um nó Krea 2 Image. Cada imagem fornecida é enviada para o armazenamento ComfyAPI e passada como uma URL.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | Imagem de referência cujo estilo influencia a geração. | IMAGE | Sim | - |
| `força` | Intensidade da referência; valores negativos invertem a influência do estilo (padrão: 1.0). | FLOAT | Sim | -2.0 a 2.0 (passo: 0.05) |
| `style_reference` | Cadeia opcional de referências de estilo recebida; este nó adiciona mais uma. | STYLE_REF | Não | - |

**Observação sobre limitações:** Você pode encadear no máximo 10 referências de estilo no total. Se tentar adicionar uma 11ª referência, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `style_reference` | Uma lista de entradas de referência de estilo, cada uma contendo uma URL e um valor de intensidade. Alimente esta saída em um nó Krea 2 Image. | STYLE_REF |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7f87568a1cd5038571f3188cfb1d71e15533ea19eee01d7826fe574a1a4dc88d`
