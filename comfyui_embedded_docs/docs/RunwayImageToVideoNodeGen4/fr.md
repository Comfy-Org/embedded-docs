> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/fr.md)

Le nœud Runway Image to Video (Gen4 Turbo) génère une vidéo à partir d'une seule image de départ en utilisant le modèle Gen4 Turbo de Runway. Il prend une invite textuelle et une image initiale, puis crée une séquence vidéo en fonction de la durée et du format d'image définis. Le nœud gère le téléchargement de l'image de départ vers l'API de Runway et renvoie la vidéo générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite textuelle pour la génération (par défaut : chaîne vide) |
| `start_frame` | IMAGE | Oui | - | Image de départ à utiliser pour la vidéo |
| `duration` | COMBO | Oui | `"5"`<br>`"10"` | Durée de la vidéo en secondes (par défaut : "5") |
| `ratio` | COMBO | Oui | `"1024:1024"`<br>`"1280:720"`<br>`"720:1280"`<br>`"1920:1080"`<br>`"1080:1920"`<br>`"2048:1080"`<br>`"1080:2048"` | Format d'image pour la vidéo générée (par défaut : "1024:1024") |
| `seed` | INT | Non | 0 à 4294967295 | Graine aléatoire pour la génération (par défaut : 0) |

**Contraintes des paramètres :**

- L'image `start_frame` doit avoir des dimensions ne dépassant pas 7999x7999 pixels
- L'image `start_frame` doit avoir un format d'image compris entre 0,5 et 2,0
- Le `prompt` doit contenir au moins un caractère

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée à partir de l'image et de l'invite fournies |

---
**Source fingerprint (SHA-256):** `ebb5f1cd5e6bf6e0fcfb4910c774c087980daf9a1987900ad966120608b924e7`
