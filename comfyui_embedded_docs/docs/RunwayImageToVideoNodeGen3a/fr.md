# Runway Image vers Vidéo (Gen3a Turbo)

Le nœud Runway Image to Video (Gen3a Turbo) génère une vidéo à partir d’une seule image de départ à l’aide du modèle Gen3a Turbo de Runway. Il prend une invite textuelle et une image de départ, puis crée une séquence vidéo en fonction de la durée et du rapport d’aspect spécifiés. La génération est traitée à distance via l’API de Runway. Ce nœud est marqué comme obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération (par défaut : "") | STRING | Oui | N/A |
| `image_début` | Image de départ à utiliser pour la vidéo | IMAGE | Oui | N/A |
| `durée` | Durée de la vidéo générée, en secondes (par défaut : "5") | COMBO | Oui | `"5"`<br>`"10"` |
| `ratio` | Rapport d’aspect de la vidéo générée (par défaut : "768:1280") | COMBO | Oui | `"768:1280"`<br>`"1280:768"` |
| `graine` | Graine aléatoire pour la génération (par défaut : 0) | INT | Oui | 0 à 4294967295 |

**Contraintes des paramètres :**

- `prompt` doit contenir au moins un caractère (il ne peut pas être vide).
- `start_frame` accepte une seule image (maximum : 1).
- `start_frame` ne doit pas dépasser 7999 x 7999 pixels en dimensions.
- `start_frame` doit avoir un rapport d’aspect compris entre 1:2 et 2:1 (0,5 à 2,0).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La séquence vidéo générée | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/fr.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
