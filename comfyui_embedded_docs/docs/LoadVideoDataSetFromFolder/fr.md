# Charger Vidéo (depuis dossier)

Charge un ensemble de vidéos depuis un dossier sélectionné dans le répertoire d'entrée de ComfyUI et les retourne sous forme de liste de références vidéo différées. Ce nœud charge un ensemble de vidéos : les images ne sont décodées que lorsqu'un autre nœud en a réellement besoin. Les formats pris en charge sont MP4, AVI, MOV, WEBM, MKV et FLV.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `dossier` | Le dossier contenant les fichiers vidéo. | COMBO | Oui | Tous les sous-dossiers disponibles dans le répertoire d'entrée de ComfyUI (peuplé dynamiquement) |

**Remarque :** Le dossier sélectionné doit être un sous-dossier du répertoire d'entrée de ComfyUI et contenir au moins un fichier vidéo pris en charge. Les extensions prises en charge sont MP4, AVI, MOV, WEBM, MKV et FLV. Si aucun fichier vidéo pris en charge n'est trouvé, ou si le chemin du dossier pointe en dehors du répertoire d'entrée, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéos` | Une liste de références vidéo différées, une pour chaque fichier vidéo pris en charge dans le dossier sélectionné, triée alphabétiquement par nom de fichier. Les images vidéo ne sont décodées que lorsque la sortie est consommée par un autre nœud. | VIDEO (list) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
