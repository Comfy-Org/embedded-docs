# Pruna P-Video-2 Texte en vidéo

Génère une vidéo à partir d'une invite textuelle avec le modèle P-Video-2 de Pruna. L'invite décrit la scène, son mouvement et son son, et le nœud génère soit sa propre bande sonore, soit prend un clip audio qui pilote le mouvement et devient la bande sonore.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Modèle vidéo Pruna à utiliser. La sélection d'un modèle révèle ses propres entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"p-video-2"` |

### Entrées P-Video-2

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Décrit la vidéo, son mouvement et son son. Doit contenir au moins un caractère autre qu'un espace blanc, jusqu'à 5000 caractères (par défaut : vide). | STRING | Oui | Jusqu'à 5000 caractères |
| `aspect_ratio` | Format d'image de la vidéo de sortie (par défaut : `"16:9"`). | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `durée` | Durée de la vidéo en secondes. `"auto"` laisse le modèle choisir la durée à partir de l'invite. Ignoré lorsque `model.audio` est connecté : la vidéo suit alors la durée de l'audio, arrondie à la seconde supérieure, jusqu'à 20 secondes (par défaut : `"5"`). | COMBO | Oui | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `résolution` | Résolution de sortie. 720p génère environ 0,9 mégapixel (1280x704 en 16:9), 1080p environ 2 mégapixels (1920x1088 en 16:9) (par défaut : `"720p"`). | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `ips` | Images par seconde. 48 fps n'est pas disponible avec le mode brouillon en 1080p (par défaut : `"24"`). | COMBO | Oui | `"24"`<br>`"48"` |
| `brouillon` | Rendu plus rapide et moins détaillé, facturé à un tarif inférieur à celui d'un rendu standard (par défaut : False). | BOOLEAN | Oui | True/False |
| `generate_audio` | Générer une bande sonore pour la vidéo. Ignoré lorsque `model.audio` est connecté, qui devient alors la bande sonore (par défaut : True). | BOOLEAN | Oui | True/False |
| `enhance_prompt` | Réécrire l'invite avec plus de détails avant la génération ; les invites courtes en ont besoin. Désactivez-le pour reproduire exactement un résultat avec la même graine (par défaut : True). Réglage avancé. | BOOLEAN | Oui | True/False |
| `model.audio` | Audio qui pilote le mouvement et devient la bande sonore. D'une durée d'au moins 1 seconde ; un audio de plus de 20 secondes est tronqué. Définit la durée de la vidéo au lieu de `model.duration`. | AUDIO | Non | - |
| `graine` | Graine pour la génération. La même graine ne reproduit exactement un résultat que lorsque `model.enhance_prompt` est désactivé (par défaut : 42). | INT | Oui | 0 à 2147483647 |

**Remarques :**

- `model.prompt` est requis et limité à 5000 caractères.
- Le mode brouillon en 1080p ne peut pas être combiné avec 48 fps : le nœud déclenche une erreur, donc désactivez le mode brouillon ou utilisez 24 fps.
- L'audio connecté doit durer au moins 1 seconde ; tout ce qui dépasse 20 secondes est ignoré.
- Lorsque `model.audio` est connecté, l'audio définit la durée de la vidéo, donc `model.duration` et `model.generate_audio` n'ont aucun effet.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo générée avec sa bande sonore. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `bb7bacf2591618220c72525c1e32382174abe3a55069720adbc84fc1d8081718`
