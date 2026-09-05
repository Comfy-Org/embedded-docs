# ComfyCloudFlux2TextToImageNode

Exécute le modèle texte-à-image Flux 2 dev sur un GPU Comfy Cloud et renvoie l'image générée. L'option `turbo` applique la LoRA Turbo avec un planning court pour une exécution beaucoup plus rapide au prix d'une légère perte de fidélité ; la désactiver effectue le passage dev complet sans la LoRA. Il s'agit d'un ensemble de nœuds bêta, facturé en crédits selon la durée d'exécution.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Le prompt textuel décrivant l'image à générer. Les espaces de début et de fin sont supprimés avant l'envoi. | STRING | Oui | 1 à 4096 caractères |
| `seed` | Graine aléatoire qui contrôle le résultat généré pour la reproductibilité (défaut : 42). | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Rapport d'aspect de l'image de sortie (défaut : « 1:1 »). | COMBO | Oui | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Budget total de pixels. 1.0 correspond environ à 1024x1024 à un ratio carré (défaut : 1.0). | FLOAT | Oui | 0.1 à 16.0 (pas de 0.1) |
| `turbo` | Exécute la LoRA Turbo sur un planning court, échangeant un peu de fidélité pour une exécution beaucoup plus rapide. Désactivée, exécute le passage dev complet sans LoRA (défaut : True). | BOOLEAN | Oui | True / False |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée à partir du prompt textuel, renvoyée sous forme de tenseur d'image ComfyUI pouvant être transmis à d'autres nœuds. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
