# BriaVideoEraser

Apaga de um vídeo tudo o que uma máscara por quadro cobre usando o Bria e preenche a lacuna. A máscara deve ser branca sobre o que deve ser apagado e preta no restante. O Bria aceita clipes de no máximo 5,1 segundos a 20 a 30 quadros por segundo com dimensões em pixels pares; o áudio é mantido por padrão. O clipe retornado pode ter alguns quadros a menos que a entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | Clipe do qual apagar. | VIDEO | Sim | - |
| `mask` | Uma máscara por quadro do vídeo, branca onde está o objeto a apagar. Forneça uma máscara ou um vídeo de máscara, não ambos. | MASK | Não | - |
| `mask_video` | Um vídeo de máscara já codificado com as mesmas dimensões e a mesma contagem de quadros que o vídeo. Forneça uma máscara ou um vídeo de máscara, não ambos. | VIDEO | Não | - |
| `preserve_audio` | Manter a faixa de áudio da entrada. Padrão: true. | BOOLEAN | Não | `true`<br>`false` |

**Notas sobre restrições:**

- Exatamente um dos parâmetros `mask` ou `mask_video` deve estar conectado. Um erro é gerado se nenhum for fornecido, ou se ambos forem fornecidos.
- O vídeo deve ter no máximo 5,1 segundos de duração e deve estar a 20 a 30 quadros por segundo. Ajuste a temporização do clipe com Get Video Components e Create Video, se necessário.
- O vídeo deve ter dimensões em pixels pares (largura e altura divisíveis por 2). Caso contrário, recorte-o ou redimensione-o primeiro.
- Ao usar `mask`, ela deve conter um quadro de máscara por quadro do vídeo, e sua proporção de aspecto deve corresponder à do vídeo. As máscaras são binarizadas em 50%: áreas pintadas com menos de metade da opacidade são ignoradas, e uma máscara vazia gera um erro. Se a resolução da máscara for diferente da do vídeo, ela é redimensionada para as dimensões do vídeo.
- Ao usar `mask_video`, ele deve ter as mesmas dimensões e a mesma contagem de quadros que o vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe editado com as áreas mascaradas apagadas e as lacunas preenchidas. A saída pode ter alguns quadros a menos que o clipe de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/pt-BR.md)

---
**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`
