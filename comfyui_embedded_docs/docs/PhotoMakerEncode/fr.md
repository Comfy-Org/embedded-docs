> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/fr.md)

Le nœud PhotoMakerEncode traite des images et du texte pour générer des données de conditionnement pour la génération d'images IA. Il prend une image de référence et une invite texte, puis crée des plongements qui peuvent être utilisés pour guider la génération d'image en fonction des caractéristiques visuelles de l'image de référence. Le nœud recherche spécifiquement le jeton "photomaker" dans le texte pour déterminer où appliquer le conditionnement basé sur l'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `photomaker` | PHOTOMAKER | Oui | - | Le modèle PhotoMaker utilisé pour traiter l'image et générer les plongements |
| `image` | IMAGE | Oui | - | L'image de référence qui fournit les caractéristiques visuelles pour le conditionnement |
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte |
| `texte` | STRING | Oui | - | L'invite texte pour la génération du conditionnement (par défaut : "photograph of photomaker") |

**Note :** Lorsque le texte contient le mot "photomaker", le nœud applique un conditionnement basé sur l'image à cette position dans l'invite. Si "photomaker" n'est pas trouvé dans le texte, le nœud génère un conditionnement texte standard sans influence de l'image.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement contenant les plongements d'image et de texte pour guider la génération d'image |
