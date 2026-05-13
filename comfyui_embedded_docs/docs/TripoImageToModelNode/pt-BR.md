> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/pt-BR.md)

Gera modelos 3D de forma síncrona com base em uma única imagem usando a API da Tripo. Este nó recebe uma imagem de entrada e a converte em um modelo 3D com várias opções de personalização para textura, qualidade e propriedades do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | Imagem de entrada usada para gerar o modelo 3D |
| `versão_do_modelo` | COMBO | Não | Múltiplas opções disponíveis | A versão do modelo Tripo a ser usada para geração |
| `estilo` | COMBO | Não | Múltiplas opções disponíveis | Configuração de estilo para o modelo gerado (padrão: "Nenhum") |
| `textura` | BOOLEAN | Não | - | Se deve gerar texturas para o modelo (padrão: Verdadeiro) |
| `pbr` | BOOLEAN | Não | - | Se deve usar Renderização Baseada em Física (padrão: Verdadeiro) |
| `semente_do_modelo` | INT | Não | - | Semente aleatória para geração do modelo (padrão: 42) |
| `orientação` | COMBO | Não | Múltiplas opções disponíveis | Configuração de orientação para o modelo gerado |
| `semente_da_textura` | INT | Não | - | Semente aleatória para geração de textura (padrão: 42) |
| `qualidade_da_textura` | COMBO | Não | "standard"<br>"detailed" | Nível de qualidade para geração de textura (padrão: "standard") |
| `alinhamento_da_textura` | COMBO | Não | "original_image"<br>"geometry" | Método de alinhamento para mapeamento de textura (padrão: "original_image") |
| `limite_de_faces` | INT | Não | -1 a 500000 | Número máximo de faces no modelo gerado, -1 para sem limite (padrão: -1) |
| `quad` | BOOLEAN | Não | - | Se deve usar faces quadriláteras em vez de triângulos (padrão: Falso) |
| `qualidade_da_geometria` | COMBO | Não | "standard"<br>"detailed" | Nível de qualidade para geração de geometria (padrão: "standard") |

**Observação:** O parâmetro `image` é obrigatório e deve ser fornecido para o funcionamento do nó. Se nenhuma imagem for fornecida, o nó gerará um RuntimeError.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | O arquivo do modelo 3D gerado (apenas para compatibilidade reversa) |
| `model task_id` | MODEL_TASK_ID | O ID da tarefa para rastrear o processo de geração do modelo |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB |

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
