> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/fr.md)

Voici la traduction en français de la documentation du nœud ViduReferenceVideoNode :

Le nœud Vidu Reference Video génère des vidéos à partir de plusieurs images de référence et d'une invite textuelle. Il utilise des modèles d'IA pour créer un contenu vidéo cohérent basé sur les images fournies et la description. Le nœud prend en charge divers paramètres vidéo, notamment la durée, le rapport hauteur/largeur, la résolution et le contrôle du mouvement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"viduq1"` | Nom du modèle pour la génération vidéo (par défaut : "viduq1") |
| `images` | IMAGE | Oui | - | Images à utiliser comme références pour générer une vidéo avec des sujets cohérents (maximum 7 images) |
| `prompt` | STRING | Oui | - | Description textuelle pour la génération vidéo |
| `durée` | INT | Non | 5-5 | Durée de la vidéo de sortie en secondes (par défaut : 5) |
| `graine` | INT | Non | 0-2147483647 | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) |
| `ratio_aspect` | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Rapport hauteur/largeur de la vidéo de sortie (par défaut : "16:9") |
| `résolution` | COMBO | Non | `"1080p"` | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : "1080p") |
| `amplitude_mouvement` | COMBO | Non | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | Amplitude de mouvement des objets dans le cadre (par défaut : "auto") |

**Contraintes et limitations :**

- Le champ `prompt` est obligatoire et ne peut pas être vide
- Maximum de 7 images autorisées pour la référence
- Chaque image doit avoir un rapport hauteur/largeur compris entre 1:4 et 4:1
- Chaque image doit avoir des dimensions minimales de 128x128 pixels
- La durée est fixée à 5 secondes

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée à partir des images de référence et de l'invite |

---
**Source fingerprint (SHA-256):** `11a7de2f50658467f63d284ef6b95d91dcdd39b4e6e5cea3b8d2f2a5d63a3020`
