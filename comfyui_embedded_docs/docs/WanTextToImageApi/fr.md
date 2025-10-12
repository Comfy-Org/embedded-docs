> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/fr.md)

Le nœud Wan Text to Image génère des images à partir de descriptions textuelles. Il utilise des modèles d'IA pour créer du contenu visuel à partir d'invitations écrites, prenant en charge les saisies de texte en anglais et en chinois. Le nœud offre divers contrôles pour ajuster la taille, la qualité et les préférences de style de l'image générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | "wan2.5-t2i-preview" | Modèle à utiliser (par défaut : "wan2.5-t2i-preview") |
| `prompt` | STRING | Oui | - | Invitation utilisée pour décrire les éléments et les caractéristiques visuelles, prend en charge l'anglais/le chinois (par défaut : vide) |
| `negative_prompt` | STRING | Non | - | Invitation textuelle négative pour guider ce qu'il faut éviter (par défaut : vide) |
| `width` | INT | Non | 768-1440 | Largeur de l'image en pixels (par défaut : 1024, pas : 32) |
| `height` | INT | Non | 768-1440 | Hauteur de l'image en pixels (par défaut : 1024, pas : 32) |
| `seed` | INT | Non | 0-2147483647 | Graine à utiliser pour la génération (par défaut : 0) |
| `prompt_extend` | BOOLEAN | Non | - | Indique s'il faut améliorer l'invitation avec l'assistance de l'IA (par défaut : True) |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane "Généré par IA" au résultat (par défaut : True) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image générée basée sur l'invitation textuelle |