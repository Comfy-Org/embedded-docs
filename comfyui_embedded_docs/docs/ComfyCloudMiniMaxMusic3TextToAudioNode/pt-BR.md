# Comfy Cloud MiniMax Music 3 Texto para Áudio [BETA]

Executa o fluxo de trabalho MiniMax Music 3 em uma GPU do Comfy Cloud e retorna uma música gerada. O prompt transmite o estilo, a instrumentação e o clima; as letras são cantadas, não descritas, e uma letra vazia deixa a faixa instrumental. Este é um nó beta e é cobrado por segundo de GPU.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição da música: estilo, instrumentação e clima. Os espaços em branco no início e no fim são removidos antes do envio. | STRING | Sim | 1 a 4096 caracteres |
| `letra` | Palavras a serem cantadas. Deixe vazio para uma faixa instrumental. | STRING | Não | 0 a 4096 caracteres |
| `semente` | Semente aleatória que controla o resultado gerado (padrão: 42). | INT | Sim | 0 a 9223372036854775807 |
| `duração_máxima` | Duração máxima que a faixa pode ter, em segundos (padrão: 120.0). O modelo pode encerrar a música antes. | FLOAT | Sim | 0.04 a 360.0 (passo 0.04) |
| `qualidade_de_áudio` | Taxa de bits da saída. `"V0"` é variável e a mais alta qualidade das três (padrão: `"V0"`). | COMBO | Sim | `"V0"`<br>`"128k"`<br>`"320k"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `AUDIO` | A música gerada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxMusic3TextToAudioNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `defc8d97071f2eaef4b00c6df721f4d10756e4867fefa22c1db7b8c3aafb6b7b`
