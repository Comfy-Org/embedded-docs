# NoeudEnregistrerSVG

Save SVG files on disk. This node takes SVG data as input and saves it to your output directory with optional metadata embedding. The node automatically handles file naming with counter suffixes and can embed workflow prompt information directly into the SVG file.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `svg` | Les données SVG à enregistrer sur le disque | SVG | Oui | - |
| `préfixe_nom_fichier` | Le préfixe du fichier à enregistrer. Cela peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant des nœuds. | STRING | Oui | (default: "svg/ComfyUI") |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `svg` | Les données SVG d'origine, transmises après l'enregistrement | SVG |
| `ui` | Informations sur le fichier enregistré, y compris le nom du fichier, le sous-dossier et le type, pour affichage dans l'interface ComfyUI | DICT |

**Remarque :** Ce nœud incorpore automatiquement les métadonnées du workflow (prompt et informations PNG supplémentaires) dans le fichier SVG lorsque celles-ci sont disponibles. Les métadonnées sont insérées sous forme de section CDATA dans l'élément metadata du SVG. Les fichiers sont enregistrés selon le modèle `filename_prefix_00001_.svg` ; lors du traitement d'un lot, `%batch_num%` dans le préfixe est remplacé par l'index de l'élément du lot actuel.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/fr.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
