> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/pt-BR.md)

O nó EmptyMochiLatentVideo cria um tensor de vídeo latente vazio com dimensões especificadas. Ele gera uma representação latente preenchida com zeros que pode ser usada como ponto de partida para fluxos de trabalho de geração de vídeo. O nó permite definir a largura, altura, duração (número de quadros) e tamanho do lote para o tensor de vídeo latente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sim | 16 a MAX_RESOLUTION | A largura do vídeo latente em pixels (padrão: 848, deve ser divisível por 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | A altura do vídeo latente em pixels (padrão: 480, deve ser divisível por 16) |
| `length` | INT | Sim | 7 a MAX_RESOLUTION | O número de quadros no vídeo latente (padrão: 25) |
| `batch_size` | INT | Não | 1 a 4096 | O número de vídeos latentes a serem gerados em um lote (padrão: 1) |

**Observação:** As dimensões latentes reais são calculadas como largura/8 e altura/8, e a dimensão temporal é calculada como ((duração - 1) // 6) + 1.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | Um tensor de vídeo latente vazio com as dimensões especificadas, contendo apenas zeros |
