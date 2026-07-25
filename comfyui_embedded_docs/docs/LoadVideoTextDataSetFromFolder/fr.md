# Charger Vidéo-Texte (depuis dossier)

Ce nœud charge un ensemble de données de fichiers vidéo et leurs légendes textuelles correspondantes à partir d'un sous-dossier spécifié dans le répertoire d'entrée de ComfyUI. Il renvoie deux listes : des références vidéo paresseuses (les images sont décodées uniquement lorsqu'elles sont nécessaires en aval) et leurs légendes associées. Le nœud prend en charge les formats vidéo courants tels que MP4, AVI, MOV, WEBM, MKV et FLV, et peut également gérer des structures de dossiers imbriquées avec des préfixes de comptage de répétitions (par exemple `5_classname/`) utilisés par des outils comme kohya‑ss/sd‑scripts.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `dossier` | Le sous-dossier contenant les fichiers vidéo et les fichiers de légendes `.txt`. Sélectionnez parmi les sous-dossiers disponibles dans le répertoire d'entrée de ComfyUI. | STRING | Oui | Liste déroulante : tous les sous-répertoires du dossier d'entrée de ComfyUI |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéos` | Références paresseuses aux fichiers vidéo chargés. Les images sont décodées uniquement lorsque connectées à un nœud aval qui les traite. Chaque élément correspond à une vidéo du dossier d'entrée. | VIDEO (liste) |
| `textes` | Liste de légendes textuelles, une par vidéo. Si une vidéo n'a pas de fichier `.txt` correspondant, sa légende est une chaîne vide. | STRING (liste) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
