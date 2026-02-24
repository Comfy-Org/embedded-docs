> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/fr.md)

`CLIP Text Encode (CLIPTextEncode)` agit comme un traducteur, convertissant vos descriptions textuelles en un format que l'IA peut comprendre. Cela aide l'IA à interpréter votre saisie et à générer l'image souhaitée.

Imaginez que vous communiquez avec un artiste qui parle une langue différente. Le modèle CLIP, entraîné sur de vastes paires d'images et de textes, comble cet écart en convertissant vos descriptions en "instructions" que le modèle d'IA peut suivre.

## Entrées

| Paramètre | Type de données | Méthode de saisie | Par défaut | Plage | Description |
|-----------|-----------|--------------|---------|--------|-------------|
| text | STRING | Saisie de texte | Vide | Tout texte | Saisissez la description (prompt) pour l'image que vous souhaitez créer. Prend en charge la saisie multi-lignes pour des descriptions détaillées. |
| clip | CLIP | Sélection de modèle | Aucun | Modèles CLIP chargés | Sélectionnez le modèle CLIP à utiliser pour traduire votre description en instructions pour le modèle d'IA. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| CONDITIONING | CONDITIONING | Les "instructions" traitées de votre description qui guident le modèle d'IA lors de la génération d'une image. |

## Fonctionnalités des Prompts

### Modèles d'Embedding

Les modèles d'embedding vous permettent d'appliquer des effets ou styles artistiques spécifiques. Les formats pris en charge incluent `.safetensors`, `.pt` et `.bin`. Pour utiliser un modèle d'embedding :

1. Placez le fichier dans le dossier `ComfyUI/models/embeddings`.
2. Référencez-le dans votre texte en utilisant `embedding:nom_du_modèle`.

Exemple : Si vous avez un modèle nommé `EasyNegative.pt` dans votre dossier `ComfyUI/models/embeddings`, vous pouvez l'utiliser comme ceci :

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANT** : Lorsque vous utilisez des modèles d'embedding, vérifiez que le nom du fichier correspond et qu'il est compatible avec l'architecture de votre modèle. Par exemple, un embedding conçu pour SD1.5 ne fonctionnera pas correctement avec un modèle SDXL.

### Ajustement du Poids des Prompts

Vous pouvez ajuster l'importance de certaines parties de votre description en utilisant des parenthèses. Par exemple :

- `(beautiful:1.2)` augmente le poids de "beautiful".
- `(beautiful:0.8)` diminue le poids de "beautiful".
- Les parenthèses simples `(beautiful)` appliqueront un poids par défaut de 1.1.

Vous pouvez utiliser les raccourcis clavier `ctrl + flèche haut/bas` pour ajuster rapidement les poids. Le pas d'ajustement du poids peut être modifié dans les paramètres.

Si vous souhaitez inclure des parenthèses littérales dans votre prompt sans changer le poids, vous pouvez les échapper avec une barre oblique inverse, par exemple `\(mot\)`.

### Prompts Dynamiques / Wildcard

Utilisez `{}` pour créer des prompts dynamiques. Par exemple, `{day|night|morning}` sélectionnera aléatoirement une option à chaque fois que le prompt est traité.

Si vous souhaitez inclure des accolades littérales dans votre prompt sans déclencher le comportement dynamique, vous pouvez les échapper avec une barre oblique inverse, par exemple `\{mot\}`.

### Commentaires dans les Prompts

Vous pouvez ajouter des commentaires qui sont exclus du prompt en utilisant :

- `//` pour commenter une seule ligne.
- `/* */` pour commenter une section ou plusieurs lignes.

Exemple :

```
// cette ligne est exclue du prompt.
a beautiful landscape, /* cette partie est ignorée */ high quality
```
