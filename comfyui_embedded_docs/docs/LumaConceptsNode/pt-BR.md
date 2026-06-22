# Luma Concepts

Armazena um ou mais Conceitos de Câmera para uso com os nós Luma Texto para Vídeo e Luma Imagem para Vídeo. Este nó permite selecionar até quatro conceitos de câmera e, opcionalmente, combiná-los com cadeias de conceitos existentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `concept1` | Primeira seleção de conceito de câmera dentre os conceitos Luma disponíveis | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "Nenhum" |
| `concept2` | Segunda seleção de conceito de câmera dentre os conceitos Luma disponíveis | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "Nenhum" |
| `concept3` | Terceira seleção de conceito de câmera dentre os conceitos Luma disponíveis | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "Nenhum" |
| `concept4` | Quarta seleção de conceito de câmera dentre os conceitos Luma disponíveis | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "Nenhum" |
| `luma_concepts` | Conceitos de Câmera opcionais para adicionar aos selecionados aqui | LUMA_CONCEPTS | Não | N/A |

**Observação:** Todos os parâmetros de conceito (`concept1` a `concept4`) podem ser definidos como "Nenhum" caso não queira usar todos os quatro slots de conceito. O nó mesclará quaisquer `luma_concepts` fornecidos com os conceitos selecionados para criar uma cadeia de conceitos combinada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `luma_concepts` | Cadeia de conceitos de câmera combinada contendo todos os conceitos selecionados | LUMA_CONCEPTS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d0e334104884eadab86987f188dff079e11ee4a3de05d2537d88fa9d2a30534a`
