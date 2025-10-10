> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/fr.md)

Le nœud CLIP Text Encode for Lumina2 encode une invite système et une invite utilisateur à l'aide d'un modèle CLIP en une incorporation qui peut guider le modèle de diffusion pour générer des images spécifiques. Il combine une invite système prédéfinie avec votre invite texte personnalisée et les traite via le modèle CLIP pour créer des données de conditionnement pour la génération d'images.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `system_prompt` | STRING | COMBO | - | "superior", "alignment" | Lumina2 propose deux types d'invites système : Superior : Vous êtes un assistant conçu pour générer des images supérieures avec un degré supérieur d'alignement image-texte basé sur des invites textuelles ou des invites utilisateur. Alignment : Vous êtes un assistant conçu pour générer des images de haute qualité avec le plus haut degré d'alignement image-texte basé sur des invites textuelles. |
| `user_prompt` | STRING | STRING | - | - | Le texte à encoder. |
| `clip` | CLIP | CLIP | - | - | Le modèle CLIP utilisé pour encoder le texte. |

**Note :** L'entrée `clip` est obligatoire et ne peut pas être None. Si l'entrée clip n'est pas valide, le nœud générera une erreur indiquant que le checkpoint peut ne pas contenir un modèle CLIP ou encodeur de texte valide.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Un conditionnement contenant le texte incorporé utilisé pour guider le modèle de diffusion. |