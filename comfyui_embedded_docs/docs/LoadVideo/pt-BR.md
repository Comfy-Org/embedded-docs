> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/pt-BR.md)

O nó Carregar Vídeo carrega arquivos de vídeo do diretório de entrada e os disponibiliza para processamento no fluxo de trabalho. Ele lê arquivos de vídeo da pasta de entrada designada e os envia como dados de vídeo que podem ser conectados a outros nós de processamento de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `file` | STRING | Sim | Múltiplas opções disponíveis | O arquivo de vídeo a ser carregado do diretório de entrada. A lista suspensa é preenchida dinamicamente com todos os arquivos de vídeo encontrados na pasta de entrada do ComfyUI. |

**Nota:** As opções disponíveis para o parâmetro `file` são preenchidas dinamicamente a partir dos arquivos de vídeo presentes no diretório de entrada. Apenas arquivos de vídeo com tipos de conteúdo suportados são exibidos. Você também pode fazer upload de um novo arquivo de vídeo diretamente através da interface do seletor de arquivos do nó.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `video` | VIDEO | Os dados de vídeo carregados que podem ser passados para outros nós de processamento de vídeo para manipulação ou análise adicional. |

---
**Source fingerprint (SHA-256):** `e3d18eb43cba34734761b5b147d9fee91fe3ca99db21f9e19a130efc3349cecb`
