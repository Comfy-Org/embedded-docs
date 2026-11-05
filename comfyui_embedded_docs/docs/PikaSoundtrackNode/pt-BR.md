# Pika Soundtrack

Este nó gera uma trilha sonora sincronizada para um vídeo com Pika. A imagem e a duração são mantidas; apenas o áudio é substituído. Descreva o som desejado ou deixe a instrução vazia para derivá-lo da imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O clipe para o qual criar uma trilha sonora. Até 10 minutos. | VIDEO | Sim | - |
| `instruction` | Como o áudio deve ser: efeitos sonoros, ambiente, música ou estilo. Deixe vazio para derivá-lo da imagem. Padrão: "" (string vazia). | STRING | Sim | 0 a 10000 caracteres |
| `seed` | Semente para amostragem. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições:**

* O vídeo de entrada deve ter no máximo 10 minutos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O clipe de entrada com a trilha sonora gerada no lugar do áudio original. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSoundtrackNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9820efec607ba52dbabe5e4fb0862240fb0f0215ce7e72914451823b7e75120b`
