# ClipTextEncode

`CLIP Text Encode (CLIPTextEncode)` agit comme un traducteur, convertissant vos descriptions textuelles dans un format que l'IA peut comprendre. Cela aide l'IA à interpréter votre saisie et à générer l'image souhaitée.

Considérez cela comme une communication avec un artiste qui parle une langue différente. Le modèle CLIP, entraîné sur de vastes paires image-texte, comble cette lacune en convertissant vos descriptions en « instructions » que le modèle d'IA peut suivre.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `text` | Le texte à encoder. Prend en charge les saisies multi-lignes et les prompts dynamiques. | STRING | Oui | Texte quelconque |
| `clip` | Le modèle CLIP utilisé pour encoder le texte. | CLIP | Oui | Modèles CLIP chargés |

Remarque : Si l'entrée `clip` est None (par exemple, lorsqu'elle provient d'un chargeur de checkpoint dont le checkpoint ne contient pas un modèle CLIP ou un encodeur de texte valide), le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Un conditioning contenant le texte intégré utilisé pour guider le modèle de diffusion. | CONDITIONING |

## Fonctionnalités du prompt

### Modèles d'embedding

Les modèles d'embedding vous permettent d'appliquer des effets artistiques ou des styles spécifiques. Les formats pris en charge incluent `.safetensors`, `.pt` et `.bin`. Pour utiliser un modèle d'embedding :

1. Placez le fichier dans le dossier `ComfyUI/models/embeddings`.
2. Référencez-le dans votre texte en utilisant `embedding:model_name`.

Exemple : Si vous avez un modèle nommé `EasyNegative.pt` dans votre dossier `ComfyUI/models/embeddings`, vous pouvez l'utiliser comme ceci :

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANT** : Lorsque vous utilisez des modèles d'embedding, vérifiez que le nom du fichier correspond et est compatible avec l'architecture de votre modèle. Par exemple, un embedding conçu pour SD1.5 ne fonctionnera pas correctement avec un modèle SDXL.

### Ajustement du poids du prompt

Vous pouvez ajuster l'importance de certaines parties de votre description à l'aide de parenthèses. Par exemple :

- `(beautiful:1.2)` augmente le poids de « beautiful ».
- `(beautiful:0.8)` diminue le poids de « beautiful ».
- Les parenthèses simples `(beautiful)` appliquent un poids par défaut de 1.1.

Vous pouvez utiliser les raccourcis clavier `ctrl + flèche haut/bas` pour ajuster rapidement les poids. La taille du pas d'ajustement du poids peut être modifiée dans les paramètres.

Si vous souhaitez inclure des parenthèses littérales dans votre prompt sans modifier le poids, vous pouvez les échapper à l'aide d'un antislash, par exemple `\(word\)`.

### Wildcards/Prompts dynamiques

Utilisez `{}` pour créer des prompts dynamiques. Par exemple, `{day|night|morning}` sélectionnera aléatoirement une option à chaque traitement du prompt.

Si vous souhaitez inclure des accolades littérales dans votre prompt sans déclencher le comportement dynamique, vous pouvez les échapper à l'aide d'un antislash, par exemple `\{word\}`.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/fr.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
