> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/fr.md)

Voici la traduction en français de la documentation du nœud SaveSVG :

Enregistre les fichiers SVG sur le disque. Ce nœud prend des données SVG en entrée et les sauvegarde dans votre répertoire de sortie avec possibilité d'intégration de métadonnées. Le nœud gère automatiquement la nomination des fichiers avec des suffixes de compteur et peut intégrer les informations de prompt du workflow directement dans le fichier SVG.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `svg` | SVG | Oui | - | Les données SVG à enregistrer sur le disque |
| `préfixe_nom_fichier` | STRING | Oui | - | Le préfixe du fichier à sauvegarder. Peut inclure des informations de formatage telles que %date:yyyy-MM-dd% ou %Empty Latent Image.width% pour inclure des valeurs provenant de nœuds. (par défaut : "svg/ComfyUI") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `ui` | DICT | Renvoie les informations du fichier, notamment le nom, le sous-dossier et le type, pour affichage dans l'interface ComfyUI |

**Remarque :** Ce nœud intègre automatiquement les métadonnées du workflow (prompt et informations PNG supplémentaires) dans le fichier SVG lorsque celles-ci sont disponibles. Les métadonnées sont insérées sous forme de section CDATA dans l'élément metadata du SVG.

---
**Source fingerprint (SHA-256):** `a294103d8d2306ce6765912a98c5572323bb5394909ee384591534b0b404ea70`
