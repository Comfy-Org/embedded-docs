# VEED Remove Video Background

Détourez le sujet d’une vidéo avec VEED et renvoyez les images ainsi qu’un masque alpha. Utilisez les deux sorties pour le compositing, ou envoyez-les via Join Image with Alpha et Save WEBM pour écrire une vidéo transparente. Choisissez `"standard"` pour les meilleurs contours sur n’importe quel arrière-plan, `"fast"` lorsque la vitesse prime, ou `"green screen"` pour des séquences filmées sur fond vert.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle de segmentation à utiliser : `"standard"` pour n’importe quel arrière-plan avec les meilleurs contours et une sortie jusqu’à 3840x2160, `"fast"` pour un résultat plus rapide jusqu’à 1920x1080, ou `"green screen"` pour détourer un fond vert jusqu’à 3840x2160. Les vidéos plus grandes sont réduites. La sélection d’une option révèle ses paramètres. | DYNAMIC_COMBO | Oui | `"standard"`<br>`"fast"`<br>`"green screen"` |
| `video` | La vidéo dont le sujet doit être détouré. Jusqu’à 60 secondes. | VIDEO | Oui | Jusqu’à 60 secondes |
| `refine_foreground_edges` | Des contours plus propres sur les cheveux, la fourrure et les détails fins. Le désactiver réduit le coût. Disponible pour `"standard"` et `"fast"` (par défaut : True). | BOOLEAN | Oui | false<br>true |
| `subject_is_person` | Désactivez lorsque le sujet est un objet ou un animal. Disponible pour `"standard"` et `"fast"` (par défaut : True). | BOOLEAN | Oui | false<br>true |
| `spill_suppression_strength` | Force avec laquelle la dominante verte est supprimée du sujet. Augmentez-la lorsque des taches vertes subsistent ; diminuez-la lorsque les couleurs du sujet se décalent. Disponible pour `"green screen"` (par défaut : 0.8). | FLOAT | Oui | 0.0 à 1.0 (pas: 0.01) |

Le clip est limité à 60 secondes ; les vidéos plus longues sont rejetées avec une erreur. Le masque vaut 1 là où l’arrière-plan a été supprimé ; utilisez donc Invert Mask avant Image Composite Masked lorsque vous souhaitez conserver le sujet à la place.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Les images de la vidéo avec l’arrière-plan supprimé. | IMAGE |
| `mask` | Vaut 1 là où l’arrière-plan a été supprimé, pour chaque image. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedRemoveVideoBackgroundNode/fr.md)

---
**Source fingerprint (SHA-256):** `1bf52a380ab09437a5a57f70215856d4ea0055f78ce8b42fe2a2b87d686e8d26`
