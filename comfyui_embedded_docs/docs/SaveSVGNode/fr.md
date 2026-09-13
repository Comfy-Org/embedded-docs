# NoeudEnregistrerSVG

Enregistre des fichiers SVG sur le disque. Ce nœud prend des données SVG en entrée et les écrit dans le répertoire de sortie de ComfyUI, en gérant automatiquement le nommage des fichiers avec des suffixes de compteur. Lorsque les informations de prompt du workflow sont disponibles, elles sont intégrées directement dans le fichier SVG en tant qu'élément de métadonnées.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `svg` | Les données SVG à enregistrer sur le disque | SVG | Oui | - |
| `filename_prefix` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant des nœuds. (par défaut : "svg/ComfyUI") | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `svg` | Les données SVG d'origine, transmises après l'enregistrement | SVG |
| `ui` | Informations sur le fichier enregistré, incluant le nom de fichier, le sous-dossier et le type, pour affichage dans l'interface ComfyUI | DICT |

**Remarque :** Ce nœud intègre automatiquement les métadonnées du workflow (prompt et informations PNG supplémentaires) dans le fichier SVG lorsqu'elles sont disponibles. Les métadonnées sont insérées sous forme de section CDATA dans l'élément de métadonnées du SVG. Les fichiers sont enregistrés selon le modèle `filename_prefix_00001_.svg` ; lors du traitement d'un lot, `%batch_num%` dans le préfixe est remplacé par l'index de l'élément du lot en cours. Le nœud est un nœud de sortie, il produit donc un résultat enregistré dans le dossier de sortie même si le fichier lui-même n'est pas affiché comme aperçu d'image.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/fr.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
