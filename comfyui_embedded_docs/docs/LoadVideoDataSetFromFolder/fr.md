# Charger Vidéo (depuis dossier)

Chargez un ensemble de vidéos à partir d'un dossier spécifié dans le répertoire d'entrée de ComfyUI. Ce nœud analyse le dossier à la recherche de fichiers vidéo pris en charge et retourne des références paresseuses — les images réelles sont décodées uniquement lorsque nécessaire en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `dossier` | Le dossier contenant les fichiers vidéo. Sélectionnez parmi les sous-dossiers disponibles dans le répertoire d'entrée de ComfyUI. | STRING | Oui | *(généré à partir des sous-dossiers d'entrée)* |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéos` | Une liste de références vidéo paresseuses (une par fichier). Les images vidéo sont décodées uniquement lorsque la sortie est consommée par un autre nœud. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`
