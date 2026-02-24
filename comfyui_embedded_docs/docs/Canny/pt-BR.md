> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/pt-BR.md)

Extraia todas as linhas de borda de fotos, como usar uma caneta para contornar uma foto, desenhando os contornos e limites de detalhes dos objetos.

## Princípio de Funcionamento

Imagine que você é um artista que precisa usar uma caneta para contornar uma foto. O nó Canny age como um assistente inteligente, ajudando você a decidir onde desenhar linhas (bordas) e onde não desenhar.

Este processo é como um trabalho de triagem:

- **Limite alto** é o "padrão de linha obrigatória": apenas contornos muito óbvios e claros serão desenhados, como os contornos faciais de pessoas e estruturas de edifícios
- **Limite baixo** é o "padrão de linha definitivamente não desenhar": bordas muito fracas serão ignoradas para evitar desenhar ruído e linhas sem significado
- **Área intermediária**: bordas entre os dois padrões serão desenhadas juntas se estiverem conectadas a "linhas obrigatórias", mas não serão desenhadas se estiverem isoladas

A saída final é uma imagem em preto e branco, onde as partes brancas são as linhas de borda detectadas e as partes pretas são áreas sem bordas.

## Entradas

| Nome do Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição da Função |
|-------------------|---------------|-----------------|--------|-----------|---------------------|
| `image`           | IMAGE         | Input           | -      | -         | Foto original que precisa de extração de bordas |
| `low_threshold`   | FLOAT         | Widget          | 0.4    | 0.01-0.99 | Limite baixo, determina quão fracas as bordas devem ser para serem ignoradas. Valores mais baixos preservam mais detalhes, mas podem produzir ruído |
| `high_threshold`  | FLOAT         | Widget          | 0.8    | 0.01-0.99 | Limite alto, determina quão fortes as bordas devem ser para serem preservadas. Valores mais altos mantêm apenas os contornos mais óbvios |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `image`       | IMAGE         | Imagem de bordas em preto e branco, linhas brancas são bordas detectadas, áreas pretas são partes sem bordas |

## Comparação de Parâmetros

![Imagem Original](./asset/input.webp)

![Comparação de Parâmetros](./asset/compare.webp)

**Problemas Comuns:**

- Bordas quebradas: Tente diminuir o limite alto
- Muito ruído: Aumente o limite baixo
- Detalhes importantes ausentes: Diminua o limite baixo
- Bordas muito grossas: Verifique a qualidade e resolução da imagem de entrada
