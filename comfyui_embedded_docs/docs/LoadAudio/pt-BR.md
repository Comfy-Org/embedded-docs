> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/en.md)

O nó LoadAudio carrega arquivos de áudio do diretório de entrada e os converte em um formato que pode ser processado por outros nós de áudio no ComfyUI. Ele lê arquivos de áudio e extrai tanto os dados da forma de onda quanto a taxa de amostragem, disponibilizando-os para tarefas de processamento de áudio downstream.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `audio` | AUDIO | Sim | Todos os arquivos de áudio e vídeo suportados no diretório de entrada | O arquivo de áudio a ser carregado do diretório de entrada |

**Nota:** O nó aceita apenas arquivos de áudio e vídeo que estejam presentes no diretório de entrada do ComfyUI. O arquivo deve existir e estar acessível para que o carregamento seja bem-sucedido.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `AUDIO` | AUDIO | Dados de áudio contendo informações de forma de onda e taxa de amostragem |

---
**Source fingerprint (SHA-256):** `a7fe63cbbb3a854359189e8685936a2b8b855e22c3c282fc77affacf640af010`
