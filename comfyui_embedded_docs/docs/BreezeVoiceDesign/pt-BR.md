# Breeze Voice Design

Cria uma nova voz Breeze a partir de uma descrição escrita. Forneça uma descrição da voz e uma frase para ela falar; a voz é construída a partir dessa prévia e salva na sua conta.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `description` | Descrição da voz em 3 a 500 caracteres: idade, gênero, sotaque, tom, ritmo. Padrão: vazio. | STRING | Sim | 3 a 500 caracteres |
| `preview_text` | A frase que a nova voz fala na prévia, com até 500 caracteres. Escreva-a no idioma selecionado, porque a voz é construída a partir desta prévia. Padrão: vazio. | STRING | Sim | 1 a 500 caracteres |
| `language` | Idioma do texto de prévia. English e Chinese podem usar qualquer um dos modelos; outros idiomas usam Breeze TTS 2 Multilingual. | DYNAMIC_COMBO | Sim | Várias opções disponíveis |
| `strength` | O quão fielmente a voz segue a descrição. Padrão: 4.0. | FLOAT | Não | 1.0 a 10.0 (passo 0.1) |
| `seed` | Controla se o nó será executado novamente; os resultados não são determinísticos, independentemente da seed. Padrão: 42. | INT | Não | 0 a 2147483647 |

### Entradas para os idiomas "English" e "Chinese"

Estas aparecem apenas quando `language` é "English" ou "Chinese".

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` ou `Breeze TTS 2 Multilingual`. Padrão: `"Breeze TTS 2"`. | COMBO | Sim | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `voice` | A nova voz Breeze, nomeada conforme a descrição. | BREEZE_VOICE |
| `preview` | Prévia de áudio da voz projetada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceDesign/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b0ea4ccd03e442972a71ec839be7b755f569686400e472967a09a956de0982f`
