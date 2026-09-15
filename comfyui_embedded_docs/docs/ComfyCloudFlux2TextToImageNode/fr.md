# Comfy Cloud Flux 2 Texte vers image [BETA]

Exécute le modèle texte-vers-image Flux 2 dev sur un GPU Comfy Cloud et renvoie l'image générée. L'option `turbo` applique le LoRA Turbo avec un programme raccourci pour une exécution bien plus rapide, au prix d'une légère perte de fidélité ; désactivée, elle effectue la passe complète de la version dev sans le LoRA. Il s'agit d'un ensemble de nœuds en version bêta, facturé en crédits selon la durée d'exécution.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Le prompt texte décrivant l'image à générer. Les espaces en début et en fin de chaîne sont supprimés avant la soumission. | STRING | Oui | 1 à 4096 caractères |
| `seed` | Graine aléatoire qui contrôle le résultat généré à des fins de reproductibilité (par défaut : 42). | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Rapport d'aspect de l'image de sortie (par défaut : « 1:1 »). | COMBO | Oui | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Budget total en pixels. 1.0 correspond à environ 1024x1024 avec un rapport carré (par défaut : 1.0). | FLOAT | Oui | 0.1 à 16.0 (pas de 0.1) |
| `turbo` | Exécute le LoRA Turbo selon un programme raccourci, en échangeant un peu de fidélité contre une exécution bien plus rapide. Désactivé, effectue la passe complète de la version dev sans le LoRA (par défaut : True). | BOOLEAN | Oui | True / False |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée à partir du prompt texte, renvoyée sous forme de tenseur d'image ComfyUI pouvant être transmis à d'autres nœuds. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
