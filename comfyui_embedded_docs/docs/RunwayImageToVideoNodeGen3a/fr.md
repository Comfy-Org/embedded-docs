# Runway Image vers Vidéo (Gen3a Turbo)

Le nœud Runway Image to Video (Gen3a Turbo) génère une vidéo à partir d'une image de départ unique à l'aide du modèle Gen3a Turbo de Runway. Il prend une invite textuelle et une image initiale, puis crée une séquence vidéo en fonction de la durée et du format d'image spécifiés. Ce nœud se connecte à l'API de Runway pour traiter la génération à distance. Runway recommande de consulter son guide des bonnes pratiques avant de générer : https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo. Ce nœud est marqué comme étant obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération (défaut : "") | STRING | Oui | N/A |
| `image_début` | Image de départ à utiliser pour la vidéo | IMAGE | Oui | N/A |
| `durée` | Durée de la vidéo en secondes (défaut : "5") | COMBO | Oui | `"5"`<br>`"10"` |
| `ratio` | Format d'image de la vidéo générée (défaut : "768:1280") | COMBO | Oui | `"768:1280"`<br>`"1280:768"` |
| `graine` | Graine aléatoire pour la génération (défaut : 0) | INT | Oui | 0 à 4294967295 |

**Contraintes des paramètres :**

- Le `start_frame` ne doit pas dépasser les dimensions de 7999x7999 pixels.
- Le `start_frame` doit avoir un format d'image compris entre 0.5 et 2.0.
- Le `start_frame` accepte une seule image (maximum de 1).
- Le `prompt` doit contenir au moins un caractère (ne peut pas être vide).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La séquence vidéo générée | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/fr.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
