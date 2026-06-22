# Wan Image vers Vidéo

Le nœud Wan Image to Video génère une vidéo à partir d'une seule image d'entrée et d'une invite textuelle. Il utilise l'image fournie comme première image et crée une séquence vidéo basée sur la description, avec des options pour la résolution, la durée, l'audio et d'autres paramètres avancés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Modèle à utiliser (par défaut : "wan2.6-i2v") | COMBO | Oui | "wan2.5-i2v-preview"<br>"wan2.6-i2v" |
| `image` | Image d'entrée servant de première image pour la génération vidéo. Une seule image est requise. | IMAGE | Oui | - |
| `invite` | Invite décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois (par défaut : vide). | STRING | Oui | - |
| `invite_négative` | Invite négative décrivant ce qu'il faut éviter (par défaut : vide). | STRING | Non | - |
| `résolution` | Qualité de résolution vidéo (par défaut : "720P"). Le modèle Wan 2.6 ne prend pas en charge la résolution 480P. | COMBO | Non | "480P"<br>"720P"<br>"1080P" |
| `durée` | Durée de la vidéo générée en secondes. Une durée de 15 secondes est uniquement prise en charge par le modèle Wan 2.6 (par défaut : 5). | INT | Non | 5-15 (pas : 5) |
| `audio` | L'audio doit contenir une voix claire et forte, sans bruit parasite ni musique de fond. Lorsqu'il est fourni, l'audio doit avoir une durée comprise entre 3,0 et 29,0 secondes. | AUDIO | Non | - |
| `graine` | Graine à utiliser pour la génération (par défaut : 0). | INT | Non | 0-2147483647 |
| `générer_audio` | Si aucune entrée audio n'est fournie, générer automatiquement l'audio (par défaut : False). | BOOLEAN | Non | - |
| `extension_invite` | Indique s'il faut améliorer l'invite avec l'assistance de l'IA (par défaut : True). | BOOLEAN | Non | - |
| `filigrane` | Indique s'il faut ajouter un filigrane généré par l'IA au résultat (par défaut : False). | BOOLEAN | Non | - |
| `type de plan` | Spécifie le type de plan pour la vidéo générée, c'est-à-dire si la vidéo est un plan continu unique ou plusieurs plans avec des coupures. Ce paramètre n'est effectif que lorsque prompt_extend est True (par défaut : "single"). | COMBO | Non | "single"<br>"multi" |

**Contraintes :**

- Une seule image d'entrée est requise pour la génération vidéo.
- Le modèle Wan 2.6 (`wan2.6-i2v`) ne prend pas en charge la résolution 480P.
- Une durée de 15 secondes est uniquement prise en charge par le modèle Wan 2.6 (`wan2.6-i2v`).
- Lorsqu'un audio est fourni, sa durée doit être comprise entre 3,0 et 29,0 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Vidéo générée à partir de l'image d'entrée et de l'invite. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `ad4947dbb9c12ebb97ace99cd447431ba6db88a3b74239099fcbea501cff71f0`
