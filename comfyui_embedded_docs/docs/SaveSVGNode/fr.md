> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/fr.md)

Enregistre des fichiers SVG sur le disque. Ce nœud prend des données SVG en entrée et les enregistre dans votre répertoire de sortie avec une option d'intégration de métadonnées. Le nœud gère automatiquement la nomination des fichiers avec des suffixes numérotés et peut intégrer les informations du prompt de workflow directement dans le fichier SVG.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `svg` | SVG | Oui | - | Les données SVG à enregistrer sur le disque |
| `filename_prefix` | STRING | Oui | - | Le préfixe pour le fichier à enregistrer. Peut inclure des informations de formatage telles que %date:yyyy-MM-dd% ou %Empty Latent Image.width% pour inclure des valeurs provenant d'autres nœuds. (par défaut : "svg/ComfyUI") |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `ui` | DICT | Retourne les informations du fichier incluant le nom, le sous-dossier et le type pour l'affichage dans l'interface ComfyUI |

**Note :** Ce nœud intègre automatiquement les métadonnées du workflow (prompt et informations PNG supplémentaires) dans le fichier SVG lorsqu'elles sont disponibles. Les métadonnées sont insérées sous forme de section CDATA dans l'élément de métadonnées du SVG.
