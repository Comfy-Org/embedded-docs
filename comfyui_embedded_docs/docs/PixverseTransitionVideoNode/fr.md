> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/fr.md)

Génère une vidéo de transition entre deux images d'entrée à l'aide de l'API PixVerse. Vous fournissez une image de départ et une image de fin, et le nœud crée une vidéo fluide qui passe de l'une à l'autre, guidée par votre invite textuelle et les paramètres choisis.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `first_frame` | IMAGE | Oui | - | Image de départ pour la transition vidéo |
| `last_frame` | IMAGE | Oui | - | Image de fin pour la transition vidéo |
| `prompt` | STRING | Oui | - | Invite pour la génération vidéo (par défaut : chaîne vide) |
| `quality` | COMBO | Oui | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` | Réglage de la qualité vidéo (par défaut : `"540p"`) |
| `duration_seconds` | COMBO | Oui | `5`<br>`8` | Durée de la vidéo en secondes |
| `motion_mode` | COMBO | Oui | `"normal"`<br>`"fast"` | Style de mouvement pour la transition (par défaut : `"normal"`) |
| `seed` | INT | Oui | 0 à 2147483647 | Graine pour la génération vidéo (par défaut : 0) |
| `negative_prompt` | STRING | Non | - | Description textuelle facultative des éléments indésirables sur une image (par défaut : chaîne vide) |

**Remarque sur les contraintes des paramètres :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur `"normal"` et la durée est limitée à 5 secondes. Pour toute durée autre que 5 secondes, le mode de mouvement est également automatiquement défini sur `"normal"`.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo de transition générée |

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`
