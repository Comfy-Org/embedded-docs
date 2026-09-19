# Pruna P-Video-2 Texto para Vídeo

Gera um vídeo a partir de um prompt de texto com o modelo P-Video-2 da Pruna. O prompt descreve a cena, seu movimento e seu som, e o nó gera sua própria trilha sonora ou recebe um clipe de áudio que conduz o movimento e se torna a trilha sonora.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo de vídeo da Pruna a usar. Selecionar um modelo revela suas próprias entradas abaixo. | DYNAMIC_COMBO | Sim | `"p-video-2"` |

### Entradas do P-Video-2

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Descreve o vídeo, seu movimento e seu som. Deve conter pelo menos um caractere que não seja espaço em branco, até 5000 caracteres (padrão: vazio). | STRING | Sim | Até 5000 caracteres |
| `proporção_de_aspecto` | Proporção de aspecto do vídeo de saída (padrão: `"16:9"`). | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `duração` | Duração do vídeo em segundos. `"auto"` permite que o modelo escolha a duração a partir do prompt. Ignorado quando `model.audio` está conectado: o vídeo então segue a duração do áudio, arredondada para cima até o segundo inteiro, até 20 segundos (padrão: `"5"`). | COMBO | Sim | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolução` | Resolução de saída. 720p renderiza cerca de 0,9 megapixels (1280x704 em 16:9), 1080p cerca de 2 megapixels (1920x1088 em 16:9) (padrão: `"720p"`). | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `fps` | Quadros por segundo. 48 fps não está disponível com rascunho em 1080p (padrão: `"24"`). | COMBO | Sim | `"24"`<br>`"48"` |
| `rascunho` | Renderização mais rápida e menos detalhada, cobrada a uma tarifa menor que uma renderização padrão (padrão: False). | BOOLEAN | Sim | True/False |
| `gerar_áudio` | Gera uma trilha sonora para o vídeo. Ignorado quando `model.audio` está conectado; nesse caso, ele se torna a trilha sonora (padrão: True). | BOOLEAN | Sim | True/False |
| `aprimorar_prompt` | Reescreve o prompt com mais detalhes antes da geração; prompts curtos precisam disso. Desative-o para reproduzir um resultado exatamente com a mesma seed (padrão: True). Configuração avançada. | BOOLEAN | Sim | True/False |
| `model.audio` | Áudio que conduz o movimento e se torna a trilha sonora. Com pelo menos 1 segundo de duração; áudio com mais de 20 segundos é truncado. Define a duração do vídeo em vez de `model.duration`. | AUDIO | Não | - |
| `semente` | Seed para a geração. A mesma seed reproduz um resultado exatamente apenas quando `model.enhance_prompt` está desativado (padrão: 42). | INT | Sim | 0 a 2147483647 |

**Observações:**

- `model.prompt` é obrigatório e limitado a 5000 caracteres.
- Rascunho em 1080p não pode ser combinado com 48 fps: o nó gera um erro, então desative o rascunho ou use 24 fps.
- O áudio conectado deve ter pelo menos 1 segundo de duração; qualquer parte após 20 segundos é ignorada.
- Com `model.audio` conectado, o áudio define a duração do vídeo, portanto `model.duration` e `model.generate_audio` não têm efeito.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo gerado com sua trilha sonora. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bb7bacf2591618220c72525c1e32382174abe3a55069720adbc84fc1d8081718`
