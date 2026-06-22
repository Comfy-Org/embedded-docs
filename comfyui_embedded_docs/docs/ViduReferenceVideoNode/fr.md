# Génération vidéo Vidu à partir de référence

Voici la traduction en français de la documentation du nœud ViduReferenceVideoNode :

Le nœud Vidu Reference Video génère des vidéos à partir de plusieurs images de référence et d'une invite textuelle. Il utilise des modèles d'IA pour créer un contenu vidéo cohérent basé sur les images fournies et la description. Le nœud prend en charge divers paramètres vidéo, notamment la durée, le rapport hauteur/largeur, la résolution et le contrôle du mouvement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Nom du modèle pour la génération vidéo (par défaut : "viduq1") | COMBO | Oui | `"viduq1"` |
| `images` | Images à utiliser comme références pour générer une vidéo avec des sujets cohérents (maximum 7 images) | IMAGE | Oui | - |
| `prompt` | Description textuelle pour la génération vidéo | STRING | Oui | - |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 5) | INT | Non | 5-5 |
| `graine` | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) | INT | Non | 0-2147483647 |
| `ratio_aspect` | Rapport hauteur/largeur de la vidéo de sortie (par défaut : "16:9") | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `résolution` | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : "1080p") | COMBO | Non | `"1080p"` |
| `amplitude_mouvement` | Amplitude de mouvement des objets dans le cadre (par défaut : "auto") | COMBO | Non | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Contraintes et limitations :**

- Le champ `prompt` est obligatoire et ne peut pas être vide
- Maximum de 7 images autorisées pour la référence
- Chaque image doit avoir un rapport hauteur/largeur compris entre 1:4 et 4:1
- Chaque image doit avoir des dimensions minimales de 128x128 pixels
- La durée est fixée à 5 secondes

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée à partir des images de référence et de l'invite | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `11a7de2f50658467f63d284ef6b95d91dcdd39b4e6e5cea3b8d2f2a5d63a3020`
