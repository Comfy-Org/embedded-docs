# Pruna P-Video-2 Pro Avatar

Transforme um retrato em um vídeo de pessoa falando com o Pruna P-Video-2 Pro Avatar. Fale um roteiro por meio de conversão de texto em fala ou conecte seu próprio áudio, e a pessoa sincroniza os lábios com ele.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | Retrato a partir do qual o vídeo começa. Proporções de 1:2 a 4:1 são mantidas; imagens mais extremas, como 1:5, são cortadas para 9:16 ou 16:9. | IMAGE | Sim | - |
| `fala` | Conduza o vídeo com um roteiro de conversão de texto em fala ou com seu próprio áudio. Selecionar uma opção revela as entradas correspondentes abaixo. | DYNAMIC_COMBO | Sim | `"script"`<br>`"audio"` |
| `prompt` | Descreve o que o vídeo mostra (padrão: "The person is talking."). Até 5000 caracteres. | STRING | Sim | Até 5000 caracteres |
| `resolução` | Resolução de saída (padrão: `"768p"`). 1080p, 2k e 4k aumentam a escala do vídeo gerado em 768p. | COMBO | Sim | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `enhance_prompt` | Adiciona ao prompt o movimento visto no retrato, como fundo, iluminação e movimento corporal (padrão: True). Configuração avançada. | BOOLEAN | Sim | `True`<br>`False` |
| `semente` | Semente para a geração (padrão: 42). A mesma seed reproduz um resultado exatamente somente quando `enhance_prompt` está desativado. | INT | Sim | 0 a 2147483647<br>Passo: 1 |

### Entradas de `"script"`

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `roteiro` | Palavras que a pessoa fala. O vídeo acompanha a duração da fala, e falas com mais de 3 minutos são cortadas em 3 minutos. | STRING | Sim | Qualquer texto |
| `voz` | Voz usada para a fala (padrão: `"Zephyr (Female)"`). | COMBO | Sim | 30 vozes predefinidas |
| `idioma` | Idioma em que o roteiro é falado (padrão: `"English (US)"`). | COMBO | Sim | `"English (US)"`<br>`"English (UK)"`<br>`"Spanish"`<br>`"French"`<br>`"German"`<br>`"Italian"`<br>`"Portuguese (Brazil)"`<br>`"Japanese"`<br>`"Korean"`<br>`"Hindi"` |
| `voice_prompt` | Como o roteiro é falado: tom, ritmo, sotaque, emoção (padrão: "Say the following."). Esse texto não é falado. | STRING | Sim | Qualquer texto |

### Entradas de `"audio"`

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `speech.audio` | Fala com a qual a pessoa sincroniza os lábios. O vídeo acompanha a duração do áudio. | AUDIO | Sim | Pelo menos 1 segundo |

**Notas:**

- Saídas mais longas limitam a duração do áudio: 2k aceita até 150 segundos de áudio e 4k até 60 segundos. Áudios mais longos nessas resoluções interrompem o nó com um erro, então use uma resolução menor ou um clipe mais curto.
- A proporção do retrato define o formato da saída. Retratos muito altos ou muito largos são cortados em vez de preenchidos com margens, então mantenha o assunto longe das bordas.
- Com `enhance_prompt` desativado, o prompt é usado como escrito, o que faz com que a mesma seed reproduza um resultado exatamente.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo com fala gerado a partir do retrato. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaAvatarNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `58efc7a110734f8da0a771371c5230908bf8226a946d69c5315e51e259630043`
