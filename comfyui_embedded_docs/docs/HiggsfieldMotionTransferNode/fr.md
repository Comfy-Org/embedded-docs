# Higgsfield Genjutsu Motion Transfer

Le nœud **Higgsfield Genjutsu Motion Transfer** transforme une vidéo en y intégrant de nouveaux personnages, lieux ou styles issus d'images de référence, tout en conservant le mouvement, les mouvements de caméra, le minutage et l'audio du clip source. Connectez le clip à restyler et une ou plusieurs images de référence qui décrivent la nouvelle apparence, puis décrivez le résultat dans le prompt. La requête est envoyée à l'API Higgsfield et la vidéo générée est renvoyée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. La sélection d'un modèle révèle les paramètres qui lui sont propres : `video`, `reference_images`, `prompt`, `resolution` et `seed`. | DYNAMIC_COMBO | Oui | `"genjutsu-v1.0"` |
| `video` | Vidéo source dont le mouvement, les mouvements de caméra, le minutage et l'audio sont conservés. Au moins 4 secondes ; seules les 30 premières secondes sont utilisées. | VIDEO | Oui | 4 à 30 secondes |
| `reference_images` | Emplacement extensible : connectez 1 à 8 images (`image_1`, `image_2`, ...) des personnages, lieux ou styles à utiliser. Une entrée par lot compte une fois par image. | IMAGE | Oui | 1 à 8 images |
| `prompt` | Facultatif. Décrivez le résultat, par exemple quelle référence remplace quelle personne, ou un nouveau décor. (par défaut : vide) | STRING | Oui | Tout texte |
| `resolution` | Résolution de la vidéo de sortie. (par défaut : `"720p"`) | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Ce paramètre dispose de la fonctionnalité « contrôle après génération » (par défaut : 42). | INT | Oui | 0 à 2147483647 |

La vidéo source est validée avant l'envoi de la requête : un clip de moins de 4 secondes est rejeté, et un clip de plus de 30 secondes est tronqué à ses 30 premières secondes. Son audio est repris dans le résultat. Les images de référence sont d'abord téléversées, et le nombre total d'images sur tous les emplacements connectés ne peut pas dépasser 8, même si le nœud expose huit emplacements. La modération de contenu de Higgsfield peut rejeter l'entrée ou le résultat, ce qui déclenche une erreur au lieu de renvoyer une vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le fichier vidéo restylisé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/fr.md)

---
**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`
