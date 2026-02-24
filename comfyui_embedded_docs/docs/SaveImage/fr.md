> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | Les images à enregistrer. |
| `préfixe_du_nom_de_fichier` | STRING | Oui | - | Le préfixe pour le fichier à enregistrer. Peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant d'autres nœuds (par défaut : "ComfyUI"). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `ui` | UI_RESULT | Ce nœud produit un résultat d'interface utilisateur contenant une liste des images enregistrées avec leurs noms de fichiers et sous-dossiers. Il ne produit pas de données pour les connecter à d'autres nœuds. |
