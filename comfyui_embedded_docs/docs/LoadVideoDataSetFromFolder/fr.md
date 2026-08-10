# Charger Vidéo (depuis dossier)

Charge tous les fichiers vidéo pris en charge depuis un dossier sélectionné dans le répertoire d'entrée de ComfyUI et les renvoie sous forme de liste de références vidéo. Ce nœud renvoie des références vidéo paresseuses, donc les images ne sont décodées que lorsqu'un autre nœud en a réellement besoin.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `dossier` | Le dossier contenant les fichiers vidéo. Sélectionnez parmi les sous-dossiers disponibles dans le répertoire d'entrée de ComfyUI. | STRING | Oui | Tous les sous-dossiers disponibles dans le répertoire d'entrée de ComfyUI |

## Sorties

| Nom de sortie | Description | Type de données |
**Remarque :** Le dossier sélectionné doit contenir au moins un fichier vidéo pris en charge. Les extensions prises en charge sont MP4, AVI, MOV, WEBM, MKV et FLV. Si aucun fichier vidéo pris en charge n'est trouvé, le nœud génère une erreur.
|---------------|-------------|-----------------|
| `vidéos` | Une liste de références vidéo paresseuses, une pour chaque fichier vidéo du dossier sélectionné. Les images vidéo ne sont décodées que lorsque la sortie est consommée par un autre nœud. | VIDEO (list) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`
