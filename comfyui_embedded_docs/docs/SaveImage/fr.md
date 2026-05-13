> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/fr.md)

Le nœud SaveImage enregistre les images qu'il reçoit dans votre répertoire `ComfyUI/output`. Il sauvegarde chaque image au format PNG et peut intégrer des métadonnées de workflow, telles que le prompt, dans le fichier sauvegardé pour référence ultérieure.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | Les images à sauvegarder. |
| `filename_prefix` | STRING | Oui | - | Le préfixe du fichier à sauvegarder. Peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant de nœuds (par défaut : "ComfyUI"). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `ui` | UI_RESULT | Ce nœud produit un résultat d'interface utilisateur contenant une liste des images sauvegardées avec leurs noms de fichiers et sous-dossiers. Il ne génère pas de données destinées à être connectées à d'autres nœuds. |

---
**Source fingerprint (SHA-256):** `fa88c26e5e03f788dcc545434a54124c5e9d03b559da67f0857b52faec0e97e7`
