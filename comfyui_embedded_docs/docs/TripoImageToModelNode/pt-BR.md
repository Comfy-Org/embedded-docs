Gera modelos 3D de forma síncrona com base em uma única imagem usando a API da Tripo. Este nó recebe uma imagem de entrada e a converte em um modelo 3D com várias opções de personalização para textura, qualidade e propriedades do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | Imagem de entrada usada para gerar o modelo 3D | IMAGE | Sim | - |
| `versão_do_modelo` | A versão do modelo Tripo a ser usada para geração | COMBO | Não | Múltiplas opções disponíveis |
| `estilo` | Configuração de estilo para o modelo gerado (padrão: "Nenhum") | COMBO | Não | Múltiplas opções disponíveis |
| `textura` | Se deve gerar texturas para o modelo (padrão: Verdadeiro) | BOOLEAN | Não | - |
| `pbr` | Se deve usar Renderização Baseada em Física (padrão: Verdadeiro) | BOOLEAN | Não | - |
| `semente_do_modelo` | Semente aleatória para geração do modelo (padrão: 42) | INT | Não | - |
| `orientação` | Configuração de orientação para o modelo gerado | COMBO | Não | Múltiplas opções disponíveis |
| `semente_da_textura` | Semente aleatória para geração de textura (padrão: 42) | INT | Não | - |
| `qualidade_da_textura` | Nível de qualidade para geração de textura (padrão: "standard") | COMBO | Não | "standard"<br>"detailed" |
| `alinhamento_da_textura` | Método de alinhamento para mapeamento de textura (padrão: "original_image") | COMBO | Não | "original_image"<br>"geometry" |
| `limite_de_faces` | Número máximo de faces no modelo gerado, -1 para sem limite (padrão: -1) | INT | Não | -1 a 500000 |
| `quad` | Se deve usar faces quadriláteras em vez de triângulos (padrão: Falso) | BOOLEAN | Não | - |
| `qualidade_da_geometria` | Nível de qualidade para geração de geometria (padrão: "standard") | COMBO | Não | "standard"<br>"detailed" |

**Observação:** O parâmetro `image` é obrigatório e deve ser fornecido para o funcionamento do nó. Se nenhuma imagem for fornecida, o nó gerará um RuntimeError.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O arquivo do modelo 3D gerado (apenas para compatibilidade reversa) | STRING |
| `model task_id` | O ID da tarefa para rastrear o processo de geração do modelo | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
