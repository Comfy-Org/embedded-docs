# NoeudEnregistrerSVG

Enregistre des fichiers SVG sur le disque. Ce nœud prend des données SVG en entrée et les enregistre dans votre répertoire de sortie, avec intégration facultative de métadonnées. Le nœud gère automatiquement la dénomination des fichiers avec des suffixes de compteur et peut intégrer directement les informations du prompt du workflow dans le fichier SVG.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `svg` | Les données SVG à enregistrer sur le disque. | SVG | Oui | - |
| `filename_prefix` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que %date:yyyy-MM-dd% ou %Empty Latent Image.width% pour inclure des valeurs provenant de nœuds. (par défaut : "svg/ComfyUI") | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `svg` | Les données SVG qui ont été enregistrées sur le disque. | SVG |
| `ui` | Renvoie les informations du fichier, notamment le nom du fichier, le sous-dossier et le type, pour affichage dans l'interface ComfyUI. | DICT |

**Remarque :** Ce nœud intègre automatiquement les métadonnées du workflow (prompt et informations PNG supplémentaires) dans le fichier SVG lorsqu'elles sont disponibles. Les métadonnées sont insérées sous forme de section CDATA dans l'élément metadata du SVG.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/fr.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
