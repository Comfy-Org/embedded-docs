> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/pt-BR.md)

O nó EmptyAudio gera um clipe de áudio silencioso com duração, taxa de amostragem e configuração de canais especificadas. Ele cria uma forma de onda contendo apenas zeros, produzindo silêncio completo para a duração fornecida. Este nó é útil para criar áudios de espaço reservado ou gerar segmentos silenciosos em fluxos de trabalho de áudio.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `duration` | FLOAT | Sim | 0.0 a 1.8446744073709552e+19 | Duração do clipe de áudio vazio em segundos (padrão: 60.0) |
| `sample_rate` | INT | Sim | - | Taxa de amostragem do clipe de áudio vazio (padrão: 44100) |
| `channels` | INT | Sim | 1 a 2 | Número de canais de áudio (1 para mono, 2 para estéreo) (padrão: 2) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | O clipe de áudio silencioso gerado, contendo dados da forma de onda e informações da taxa de amostragem |
