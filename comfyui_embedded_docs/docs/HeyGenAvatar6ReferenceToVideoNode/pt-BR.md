# HeyGen Avatar 6 Reference to Video

Faça uma pessoa ou um personagem falar o áudio que você conectar, usando uma foto ou um vídeo como referência. O Avatar 6 reconstrói o rosto e a cena a partir dessa referência, então o mesmo áudio pode animar uma foto estática, um clipe existente ou ambos.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | Seletor de modelo; selecionar um modelo revela suas entradas abaixo. `"heygen-avatar-6-turbo"` é a camada mais barata e rápida. | DYNAMIC_COMBO | Sim | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |

### Entradas do `heygen-avatar-6`

`"heygen-avatar-6-turbo"` expõe as mesmas entradas com os mesmos limites.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `image` | Foto opcional da pessoa ou do personagem a ser animado. Ela define a aparência e a cena e não é usada como primeiro quadro. | IMAGE | Não | Imagem única |
| `video` | Vídeo opcional de um personagem animado ou estilizado mostrando como ele fala e se move. Vídeos mais longos são cortados nos primeiros 30 segundos. | VIDEO | Não | 2 a 30 segundos |
| `audio` | Fala para o avatar. A duração do vídeo acompanha o áudio. | AUDIO | Sim | 1.5 segundos a 10 minutos |
| `resolution` | Resolução do vídeo de saída. Padrão: `"1080p"`. | COMBO | Sim | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Proporção do vídeo de saída. `"auto"` mantém o formato da imagem, ou do vídeo quando nenhuma imagem está conectada; outros valores reenquadram a cena. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Direcionamento opcional para gestos, expressão, postura e movimento de câmera. Padrão: string vazia. | STRING | Sim | Texto multilinha, até 1200 caracteres |
| `motion_expressiveness` | `"less"` produz gestos menos numerosos e menores. O prompt de movimento tem precedência onde os dois se sobrepõem. Padrão: `"default"`. | COMBO | Sim | `"less"`<br>`"default"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* Conecte uma imagem, um vídeo ou ambos; sem nenhum dos dois, o nó gera um erro.
* A entrada de imagem deve conter exatamente uma imagem, não um lote.
* Vídeos de referência de pessoas realistas são recusados. Use um vídeo de um personagem animado ou estilizado, ou conecte uma foto da pessoa em vez disso.
* Um vídeo de referência deve ter 2 segundos ou mais e não pode ser maior que 50 MB.
* O preço é por segundo de vídeo de saída e depende do modelo e da resolução.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo falado gerado, baixado do HeyGen assim que a renderização termina. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6ReferenceToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a50342827511e355a1d857c34e8bbfc0b74ca7b003dca783b76fcd151413ff8`
