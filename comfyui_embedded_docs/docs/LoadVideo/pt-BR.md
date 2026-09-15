# Carregar Vídeo

O nó Load Video carrega arquivos de vídeo do diretório de entrada e os disponibiliza para processamento no fluxo de trabalho. Ele lê arquivos de vídeo da pasta de entrada designada e os gera como dados de vídeo que podem ser conectados a outros nós de processamento de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `arquivo` | O arquivo de vídeo a ser carregado do diretório de entrada. A lista suspensa é preenchida dinamicamente com todos os arquivos de vídeo encontrados na pasta de entrada do ComfyUI, e novos arquivos de vídeo podem ser enviados diretamente pelo seletor de arquivos. | COMBO | Sim | Várias opções disponíveis (todos os arquivos de vídeo no diretório de entrada) |

**Nota:** As opções disponíveis para o parâmetro `file` são preenchidas dinamicamente a partir dos arquivos de vídeo presentes no diretório de entrada. Apenas arquivos que correspondem a tipos de conteúdo de vídeo suportados são exibidos, e a lista é classificada em ordem alfabética. Você também pode enviar um novo arquivo de vídeo diretamente pela interface de seleção de arquivos do nó. Se um arquivo de vídeo selecionado anteriormente não puder mais ser encontrado, o nó relata um erro de arquivo inválido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | Os dados de vídeo carregados que podem ser passados a outros nós de processamento de vídeo para manipulação ou análise adicionais. | VIDEO |

**Nota:** O nó também produz uma pré-visualização do vídeo carregado, que é exibida diretamente no nó.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`
