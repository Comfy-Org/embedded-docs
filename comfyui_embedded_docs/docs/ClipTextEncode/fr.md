> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI `CLIPTextEncode` :

`CLIP Text Encode (CLIPTextEncode)` agit comme un traducteur, convertissant vos descriptions textuelles dans un format compréhensible par l'IA. Cela aide l'IA à interpréter votre entrée et à générer l'image souhaitée.

Considérez cela comme une communication avec un artiste qui parle une langue différente. Le modèle CLIP, entraîné sur de vastes paires image-texte, comble cet écart en convertissant vos descriptions en « instructions » que le modèle d'IA peut suivre.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `text` | STRING | Oui | Tout texte | Le texte à encoder. Prend en charge les entrées multilignes et les invites dynamiques. |
| `clip` | CLIP | Oui | Modèles CLIP chargés | Le modèle CLIP utilisé pour encoder le texte. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Un conditionnement contenant le texte intégré utilisé pour guider le modèle de diffusion. |

## Fonctionnalités des Invites

### Modèles d'Intégration (Embedding)

Les modèles d'intégration vous permettent d'appliquer des effets artistiques ou des styles spécifiques. Les formats pris en charge incluent `.safetensors`, `.pt` et `.bin`. Pour utiliser un modèle d'intégration :

1. Placez le fichier dans le dossier `ComfyUI/models/embeddings`.
2. Référencez-le dans votre texte en utilisant `embedding:nom_du_modèle`.

Exemple : Si vous avez un modèle nommé `EasyNegative.pt` dans votre dossier `ComfyUI/models/embeddings`, vous pouvez l'utiliser comme ceci :

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANT** : Lorsque vous utilisez des modèles d'intégration, vérifiez que le nom du fichier correspond et est compatible avec l'architecture de votre modèle. Par exemple, une intégration conçue pour SD1.5 ne fonctionnera pas correctement avec un modèle SDXL.

### Ajustement du Poids des Invites

Vous pouvez ajuster l'importance de certaines parties de votre description en utilisant des parenthèses. Par exemple :

- `(beautiful:1.2)` augmente le poids de « beautiful ».
- `(beautiful:0.8)` diminue le poids de « beautiful ».
- Les parenthèses simples `(beautiful)` appliqueront un poids par défaut de 1.1.

Vous pouvez utiliser les raccourcis clavier `ctrl + flèche haut/bas` pour ajuster rapidement les poids. La taille du pas d'ajustement du poids peut être modifiée dans les paramètres.

Si vous souhaitez inclure des parenthèses littérales dans votre invite sans modifier le poids, vous pouvez les échapper en utilisant une barre oblique inverse, par exemple `\(mot\)`.

### Invites Dynamiques / Wildcard

Utilisez `{}` pour créer des invites dynamiques. Par exemple, `{jour|nuit|matin}` sélectionnera aléatoirement une option à chaque traitement de l'invite.

Si vous souhaitez inclure des accolades littérales dans votre invite sans déclencher de comportement dynamique, vous pouvez les échapper en utilisant une barre oblique inverse, par exemple `\{mot\}`.

**Source fingerprint (SHA-256):** `e8f286cdec879c529270e110ccf5959ed6df77737cfb5a8019379afac9266118`
