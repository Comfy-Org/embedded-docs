# Recraft Criar Estilo

Este nó cria um estilo personalizado para geração de imagens através do upload de imagens de referência. Você pode enviar entre 1 e 5 imagens para definir o novo estilo, e o nó retornará um ID de estilo único que pode ser usado com outros nós Recraft. O tamanho total combinado de todos os arquivos de imagem enviados não deve exceder 5 MB.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `estilo` | O estilo base das imagens geradas. | STRING | Sim | `"realistic_image"`<br>`"digital_illustration"` |
| `imagens` | Um conjunto de 1 a 5 imagens de referência usadas para criar o estilo personalizado. | IMAGE | Sim | 1 a 5 imagens |

**Observação:** O tamanho total do arquivo de todas as imagens na entrada `images` deve ser inferior a 5 MB. O nó falhará se esse limite for excedido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `style_id` | O identificador único para o estilo personalizado recém-criado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `36340e64d90b3edbbecedf15ac123adaabb5bc0c950183d2df6627dc873da61c`
