# Charger Vidéo-Texte (depuis dossier)

Ce nœud charge les fichiers vidéo et leurs légendes texte associées depuis un sous-dossier sélectionné dans le répertoire d'entrée de ComfyUI, et les retourne sous forme de deux listes : vidéos et légendes. Les entrées vidéo sont des références différées, de sorte que les frames ne sont décodées que lorsqu'un nœud en aval en a besoin. Les formats pris en charge sont MP4, AVI, MOV, WEBM, MKV et FLV. Les dossiers imbriqués avec un préfixe de répétition (par exemple `5_classname/`, comme utilisé par des outils tels que kohya-ss/sd-scripts) sont également pris en charge.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `dossier` | Le dossier contenant les fichiers vidéo et les légendes .txt. | COMBO | Oui | Plusieurs options disponibles : liste dynamiquement tous les sous-dossiers du répertoire d'entrée de ComfyUI |

Le dossier sélectionné doit être un sous-dossier du répertoire d'entrée de ComfyUI ; un nom de dossier qui résout hors de ce répertoire déclenche une erreur. Si le dossier sélectionné ne contient aucun fichier avec une extension vidéo prise en charge (MP4, AVI, MOV, WEBM, MKV, FLV), le nœud déclenche une erreur. Pour les dossiers imbriqués dont le nom commence par un nombre suivi d'un underscore (par exemple `5_classname`), chaque vidéo de ce dossier est incluse dans le jeu de données le nombre de fois indiqué par ce préfixe. La légende de chaque vidéo est lue depuis un fichier `.txt` portant le même nom de base ; si aucun fichier `.txt` correspondant n'existe, la légende est une chaîne vide.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `vidéos` | Références vidéo différées ; les frames ne sont décodées que lorsque c'est nécessaire en aval. Une entrée par fichier vidéo trouvé dans le dossier. | VIDEO (list) |
| `textes` | Liste de légendes texte. Une légende par vidéo ; si une vidéo n'a pas de fichier `.txt` correspondant, sa légende est une chaîne vide. | STRING (list) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
