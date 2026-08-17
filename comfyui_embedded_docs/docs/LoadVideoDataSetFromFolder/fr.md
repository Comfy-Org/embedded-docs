# Charger Vidéo (depuis dossier)

Charge tous les fichiers vidéo pris en charge à partir d'un dossier sélectionné dans le répertoire d'entrée de ComfyUI et les renvoie sous forme d'une liste de références vidéo. Ce nœud renvoie des références vidéo différées, de sorte que les trames ne sont décodées que lorsqu'un autre nœud en a réellement besoin. Formats pris en charge : MP4, AVI, MOV, WEBM, MKV et FLV.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `folder` | Le dossier contenant les fichiers vidéo. Sélectionnez parmi les sous-dossiers disponibles dans le répertoire d'entrée de ComfyUI. | COMBO | Oui | Tous les sous-dossiers disponibles dans le répertoire d'entrée de ComfyUI |

**Remarque :** Le dossier sélectionné doit contenir au moins un fichier vidéo pris en charge. Les extensions prises en charge sont MP4, AVI, MOV, WEBM, MKV et FLV. Si aucun fichier vidéo pris en charge n'est trouvé, le nœud génère une erreur. Le dossier doit correspondre à un emplacement situé dans le répertoire d'entrée de ComfyUI ; les noms de dossier qui tentent d'en sortir (par exemple avec « .. ») sont rejetés avec une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `videos` | Une liste de références vidéo différées, une pour chaque fichier vidéo du dossier sélectionné. Les trames ne sont décodées que lorsque la sortie est consommée par un autre nœud. | VIDEO (liste) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
