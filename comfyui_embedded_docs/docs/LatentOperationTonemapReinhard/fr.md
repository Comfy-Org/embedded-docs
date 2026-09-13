# Opération de Mappage de Tons Reinhard Latent

Ce nœud crée une opération latente qui applique un tonemapping Reinhard aux vecteurs latents. Il normalise chaque vecteur latent, mesure la distribution globale de magnitude (moyenne et écart-type), puis compresse les magnitudes extrêmes à l’aide de la courbe de Reinhard, l’intensité globale étant contrôlée par un multiplicateur. Le nœud est marqué comme expérimental (également recherchable sous « hdr latent »).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `multiplier` | Contrôle l’intensité de l’effet de tonemapping (par défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 (pas de 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `operation` | Renvoie une opération de tonemapping pouvant être appliquée aux vecteurs latents | LATENT_OPERATION |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/fr.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
