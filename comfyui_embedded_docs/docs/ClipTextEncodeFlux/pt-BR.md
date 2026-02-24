> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/pt-BR.md)

`CLIPTextEncodeFlux` é um nó avançado de codificação de texto no ComfyUI, projetado especificamente para a arquitetura Flux. Ele utiliza um mecanismo de codificador duplo (CLIP-L e T5XXL) para processar tanto palavras-chave estruturadas quanto descrições detalhadas em linguagem natural, fornecendo ao modelo Flux uma compreensão de texto mais precisa e abrangente para melhorar a qualidade da geração de imagem a partir de texto.

Este nó é baseado em um mecanismo de colaboração de codificadores duplos:

1. A entrada `clip_l` é processada pelo codificador CLIP-L, extraindo características de palavras-chave como estilo, tema e outras — ideal para descrições concisas.
2. A entrada `t5xxl` é processada pelo codificador T5XXL, que se destaca em compreender descrições de cena complexas e detalhadas em linguagem natural.
3. As saídas de ambos os codificadores são fundidas e combinadas com o parâmetro `guidance` para gerar embeddings de condicionamento unificados (`CONDITIONING`) para os nós de amostragem Flux subsequentes, controlando o quão fielmente o conteúdo gerado corresponde à descrição de texto.

## Entradas

| Parâmetro | Tipo de Dado | Método de Entrada | Padrão | Intervalo | Descrição |
|-----------|--------------|-------------------|--------|-----------|-----------|
| `clip`    | CLIP         | Entrada do nó     | Nenhum | -         | Deve ser um modelo CLIP compatível com a arquitetura Flux, incluindo os codificadores CLIP-L e T5XXL |
| `clip_l`  | STRING       | Caixa de texto    | Nenhum | Até 77 *tokens* | Adequado para descrições concisas de palavras-chave, como estilo ou tema |
| `t5xxl`   | STRING       | Caixa de texto    | Nenhum | Quase ilimitado | Adequado para descrições detalhadas em linguagem natural, expressando cenas e detalhes complexos |
| `guidance`| FLOAT        | Controle deslizante | 3.5   | 0.0 - 100.0 | Controla a influência das condições de texto no processo de geração; valores mais altos significam uma aderência mais estrita ao texto |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Contém os embeddings fundidos de ambos os codificadores e o parâmetro de orientação, usado para geração de imagem condicional |

## Exemplos de Uso

### Exemplos de *Prompt*

- **Entrada `clip_l`** (estilo de palavra-chave):
  - Use combinações de palavras-chave estruturadas e concisas
  - Exemplo: `obra-prima, melhor qualidade, retrato, pintura a óleo, iluminação dramática`
  - Foque no estilo, qualidade e assunto principal

- **Entrada `t5xxl`** (descrição em linguagem natural):
  - Use descrições de cena completas e fluentes
  - Exemplo: `Um retrato altamente detalhado no estilo de pintura a óleo, apresentando iluminação de claro-escuro dramática que cria sombras profundas e destaques brilhantes, enfatizando os traços do sujeito com uma composição inspirada no renascimento.`
  - Foque nos detalhes da cena, relações espaciais e efeitos de iluminação

### Observações

1. Certifique-se de usar um modelo CLIP compatível com a arquitetura Flux
2. É recomendado preencher ambos os campos, `clip_l` e `t5xxl`, para aproveitar a vantagem do codificador duplo
3. Observe o limite de 77 *tokens* para `clip_l`
4. Ajuste o parâmetro `guidance` com base nos resultados gerados
