# Charger Vidéo-Texte (depuis dossier)

Ce nœud charge un ensemble de paires vidéo-texte à partir d'un sous-dossier sélectionné dans le répertoire d'entrée de ComfyUI et les retourne sous forme de deux listes : vidéos et légendes textuelles. Les entrées vidéo sont des références paresseuses, de sorte que les images ne sont décodées que lorsqu'un nœud en aval en a besoin. Les formats pris en charge sont MP4, AVI, MOV, WEBM, MKV et FLV. Les légendes sont lues à partir des fichiers `.txt` portant le même nom que chaque fichier vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `folder` | Le dossier contenant les fichiers vidéo et les légendes .txt. | COMBO | Oui | Tous les sous-dossiers du répertoire d'entrée de ComfyUI (liste dynamique) |

Remarques :
- Le dossier sélectionné doit être un sous-dossier du répertoire d'entrée de ComfyUI ; les chemins qui pointent à l'extérieur de celui-ci sont rejetés.
- Si le dossier ne contient aucun fichier avec une extension vidéo prise en charge, le nœud génère une erreur.
- Les sous-dossiers dont le nom commence par un nombre suivi d'un trait de soulignement (par exemple `5_classname/`, comme utilisé par des outils tels que kohya-ss/sd-scripts) sont également pris en charge : chaque vidéo de ce dossier est incluse dans l'ensemble de données autant de fois que l'indique ce préfixe.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `videos` | Références vidéo paresseuses ; les images ne sont décodées que si nécessaire en aval. Une entrée par fichier vidéo trouvé dans le dossier. | VIDEO (liste) |
| `texts` | Liste des légendes textuelles. Une légende par vidéo ; si une vidéo n'a pas de fichier `.txt` correspondant, sa légende est une chaîne vide. | STRING (liste) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
