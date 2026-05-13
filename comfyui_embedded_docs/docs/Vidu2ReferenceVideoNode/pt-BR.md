> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/pt-BR.md)

Aqui está a tradução da documentação para português brasileiro, seguindo todas as regras estabelecidas:

O nó de Geração de Vídeo a partir de Referência Vidu2 cria um vídeo a partir de um prompt de texto e múltiplas imagens de referência. Você pode definir até sete temas, cada um com seu próprio conjunto de imagens de referência, e referenciá-los no prompt usando `@subject{subject_id}`. O nó gera um vídeo com duração, proporção de aspecto e movimento configuráveis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | `"viduq2"` | O modelo de IA a ser usado para geração de vídeo. |
| `sujeitos` | AUTOGROW | Sim | N/A | Para cada tema, forneça até 3 imagens de referência (7 imagens no total entre todos os temas). Referencie-os nos prompts via `@subject{subject_id}`. |
| `prompt` | STRING | Sim | N/A | A descrição textual usada para guiar a geração do vídeo. Quando o parâmetro `áudio` está ativado, o vídeo incluirá fala gerada e música de fundo com base neste prompt. |
| `áudio` | BOOLEAN | Não | N/A | Quando ativado, o vídeo conterá fala gerada e música de fundo com base no prompt (padrão: `False`). |
| `duração` | INT | Não | 1 a 10 | A duração do vídeo gerado em segundos (padrão: `5`). |
| `semente` | INT | Não | 0 a 2147483647 | Um número usado para controlar a aleatoriedade da geração para resultados reproduzíveis (padrão: `1`). |
| `proporção` | COMBO | Não | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | A forma do quadro do vídeo. |
| `resolução` | COMBO | Não | `"720p"`<br>`"1080p"` | A resolução em pixels do vídeo de saída. |
| `amplitude_de_movimento` | COMBO | Não | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | Controla a amplitude de movimento dos objetos no quadro. |

**Restrições:**

* O `prompt` deve ter entre 1 e 2000 caracteres.
* Você pode definir múltiplos temas, mas o número total de imagens de referência entre todos os temas não deve exceder 7.
* Cada tema individual pode ter no máximo 3 imagens de referência.
* Cada imagem de referência deve ter uma proporção largura-altura entre 1:4 e 4:1.
* Cada imagem de referência deve ter pelo menos 128 pixels tanto em largura quanto em altura.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `3e02b05a0e374442a6ca4ce6a3dbc182b4059e19b5ed7dfc2794e036de7beffd`
