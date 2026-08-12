# WanAnimate2Cache

Caches the pose-video's per-block activations once so they do not need to be recomputed on every sampling step, which roughly halves generation time. The tradeoff is extra memory usage: about 12.5 GB of system RAM at 480x832 resolution with 81 frames in bf16, scaling with resolution and video length.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Wan Animate2 auquel attacher le cache. | MODEL | Oui | |
| `device` | Où conserver le cache. `cpu` (RAM) est le choix sûr, le cache ne tiendra pas dans la VRAM en plus du modèle aux tailles typiques. `gpu` (VRAM) peut être plus rapide s'il y tient. (par défaut : "cpu") | STRING | Oui | "cpu"<br>"gpu" |
| `dtype` | Précision de stockage. `default` stocke les activations dans le dtype de calcul du modèle. `int8` réduit le cache de moitié, `int4` le divise par quatre, `convrot` est utilisé pour conserver la précision. (par défaut : "default") | STRING | Oui | "default"<br>"int8"<br>"int4" |

Remarque : Lorsque des fenêtres de contexte sont utilisées, chaque fenêtre est mise en cache séparément, donc l'utilisation de la mémoire évolue avec le nombre de fenêtres. Le programme `static_standard` doit être utilisé, car les programmes uniformes déplacent les fenêtres à chaque étape et le cache n'est jamais réutilisé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle cloné avec le cache d'activations pose-vidéo attaché. Le cache est automatiquement libéré à la fin de la génération. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/fr.md)

---
**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`
