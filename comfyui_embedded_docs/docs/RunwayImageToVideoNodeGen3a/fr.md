> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI Runway Image to Video (Gen3a Turbo) :

Le nœud Runway Image to Video (Gen3a Turbo) génère une vidéo à partir d'une seule image de départ en utilisant le modèle Gen3a Turbo de Runway. Il prend une invite textuelle et une image initiale, puis crée une séquence vidéo basée sur la durée et le rapport hauteur/largeur spécifiés. Ce nœud se connecte à l'API de Runway pour traiter la génération à distance.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite textuelle pour la génération (par défaut : "") |
| `image_début` | IMAGE | Oui | N/A | Image de départ à utiliser pour la vidéo |
| `durée` | COMBO | Oui | `"5"`<br>`"10"` | Durée de la vidéo en secondes (par défaut : "5") |
| `ratio` | COMBO | Oui | `"1280x720"`<br>`"720x1280"`<br>`"1920x1080"`<br>`"1080x1920"`<br>`"1080x1080"` | Rapport hauteur/largeur de la vidéo générée (par défaut : "1280x720") |
| `graine` | INT | Non | 0 à 4294967295 | Graine aléatoire pour la génération (par défaut : 0) |

**Contraintes des paramètres :**

- L'`start_frame` doit avoir des dimensions ne dépassant pas 7999x7999 pixels.
- L'`start_frame` doit avoir un rapport hauteur/largeur compris entre 0,5 et 2,0.
- Le `prompt` doit contenir au moins un caractère (ne peut pas être vide).

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | La séquence vidéo générée |

---
**Source fingerprint (SHA-256):** `4f3270ce070ce50580699292e21c5f9e3b1a56dd8ac981f67a9026ef6fc8ed76`
