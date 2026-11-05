# Pika Music

Este nó gera música a partir de uma descrição textual e letras opcionais, ou faz cover de uma música fornecida por você, com a Pika. Escolha `"text to music"` para escrever uma nova música com a duração que você definir, ou `"cover"` para regravar uma música e manter a duração dela.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mode` | O que o nó faz: `"text to music"` escreve uma nova música; `"cover"` regrava uma música fornecida. Cada modo revela suas próprias entradas abaixo. Padrão: `"text to music"`. | DYNAMIC_COMBO | Sim | `"text to music"`<br>`"cover"` |

### Entradas de Text to Music

Estas entradas aparecem quando `mode` está definido como `"text to music"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Como a música deve soar. Não pode estar vazio. Padrão: "" (string vazia). | STRING | Sim | 1 a 4000 caracteres |
| `lyrics` | Letras opcionais. Tags de seção como `[Verse]` e `[Chorus]` são permitidas. Padrão: "" (string vazia). | STRING | Sim | 0 a 8000 caracteres |
| `duration` | Duração da música em segundos. Padrão: 30.0. | FLOAT | Sim | 10.0 a 360.0 (passo: 0.1) |
| `rewrite_prompt` | Expande um prompt curto ou vago com um modelo antes de gerar. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `seed` | Semente para amostragem. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas de Cover

Estas entradas aparecem quando `mode` está definido como `"cover"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `source_audio` | A música para fazer cover. O resultado tem a mesma duração, limitada a 5 a 360 segundos. | AUDIO | Sim | - |
| `prompt` | Como o cover deve soar. Não pode estar vazio. Padrão: "" (string vazia). | STRING | Sim | 1 a 4000 caracteres |
| `lyrics` | Letras opcionais. Tags de seção como `[Verse]` e `[Chorus]` são permitidas. Padrão: "" (string vazia). | STRING | Sim | 0 a 8000 caracteres |
| `rewrite_prompt` | Expande um prompt curto ou vago com um modelo antes de gerar. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `seed` | Semente para amostragem. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições:**

* O prompt deve ter entre 1 e 4000 caracteres, e as letras devem ter no máximo 8000 caracteres.
* O modo cover ignora `duration`: a saída corresponde à duração de `source_audio`, limitada a 5 a 360 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `AUDIO` | A música gerada, ou o cover da faixa fornecida. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaMusicNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e3051b2d0cfff72cf7e359d7383f4e0d133df0338ff42a00f0649387f504ec28`
