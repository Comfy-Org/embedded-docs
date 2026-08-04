# Charger Vidéo-Texte (depuis dossier)

Ce nœud charge des fichiers vidéo et leurs légendes textuelles associées depuis un sous-dossier sélectionné dans le répertoire d'entrée de ComfyUI et les renvoie sous forme de deux listes : vidéos et légendes. Les entrées vidéo sont des références paresseuses, donc les images ne sont décodées que lorsqu'un nœud aval en a besoin. Les formats pris en charge sont MP4, AVI, MOV, WEBM, MKV et FLV. Les dossiers imbriqués avec un préfixe de nombre de répétitions (par exemple `5_classname/`, comme utilisé par des outils tels que kohya-ss/sd-scripts) sont également pris en charge.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `dossier` | Le dossier contenant les fichiers vidéo et les légendes .txt. | STRING | Oui | Combo : liste dynamique de tous les sous-dossiers du répertoire d'entrée de ComfyUI |

## Sorties

| Nom de sortie | Description | Type de données |
Si le dossier sélectionné ne contient aucun fichier avec une extension vidéo prise en charge, le nœud génère une erreur. Pour les dossiers imbriqués dont le nom commence par un nombre suivi d'un trait de soulignement (par exemple `5_classname`), chaque vidéo de ce dossier est incluse dans le jeu de données autant de fois que l'indique ce préfixe.
|---------------|-------------|-----------------|
| `vidéos` | Références vidéo paresseuses ; les images ne sont décodées que lorsque nécessaire en aval. Une entrée par fichier vidéo trouvé dans le dossier. | VIDEO (list) |
| `textes` | Liste de légendes textuelles. Une légende par vidéo ; si une vidéo n'a pas de fichier `.txt` correspondant, sa légende est une chaîne vide. | STRING (list) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
