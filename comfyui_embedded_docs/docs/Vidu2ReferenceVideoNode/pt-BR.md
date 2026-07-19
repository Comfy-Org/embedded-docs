# Geração de Vídeo por Referência Vidu2

Aqui está a tradução da documentação para português brasileiro, seguindo todas as regras estabelecidas:

O nó de Geração de Vídeo a partir de Referência Vidu2 cria um vídeo a partir de um prompt de texto e múltiplas imagens de referência. Você pode definir até sete temas, cada um com seu próprio conjunto de imagens de referência, e referenciá-los no prompt usando `@subject{subject_id}`. O nó gera um vídeo com duração, proporção de aspecto e movimento configuráveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para geração de vídeo. | COMBO | Sim | `"viduq2"` |
| `sujeitos` | Para cada tema, forneça até 3 imagens de referência (7 imagens no total entre todos os temas). Referencie-os nos prompts via `@subject{subject_id}`. | AUTOGROW | Sim | N/A |
| `prompt` | A descrição textual usada para guiar a geração do vídeo. Quando o parâmetro `áudio` está ativado, o vídeo incluirá fala gerada e música de fundo com base neste prompt. | STRING | Sim | N/A |
| `áudio` | Quando ativado, o vídeo conterá fala gerada e música de fundo com base no prompt (padrão: `False`). | BOOLEAN | Não | N/A |
| `duração` | A duração do vídeo gerado em segundos (padrão: `5`). | INT | Não | 1 a 10 |
| `semente` | Um número usado para controlar a aleatoriedade da geração para resultados reproduzíveis (padrão: `1`). | INT | Não | 0 a 2147483647 |
| `proporção` | A forma do quadro do vídeo. | COMBO | Não | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `resolução` | A resolução em pixels do vídeo de saída. | COMBO | Não | `"720p"`<br>`"1080p"` |
| `amplitude_de_movimento` | Controla a amplitude de movimento dos objetos no quadro. | COMBO | Não | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Restrições:**

* O `prompt` deve ter entre 1 e 2000 caracteres.
* Você pode definir múltiplos temas, mas o número total de imagens de referência entre todos os temas não deve exceder 7.
* Cada tema individual pode ter no máximo 3 imagens de referência.
* Cada imagem de referência deve ter uma proporção largura-altura entre 1:4 e 4:1.
* Cada imagem de referência deve ter pelo menos 128 pixels tanto em largura quanto em altura.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3e02b05a0e374442a6ca4ce6a3dbc182b4059e19b5ed7dfc2794e036de7beffd`
