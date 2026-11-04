# Pika SFX

Ce nœud génère un effet sonore à partir d'une description textuelle avec Pika. Décrivez le son et sa durée, et le nœud renvoie un clip audio.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Description de l'effet sonore souhaité. Ne doit pas être vide. Par défaut : "" (chaîne vide). | STRING | Oui | 1 à 4000 caractères |
| `duration` | Durée de l'effet sonore en secondes. Par défaut : 5.0. | FLOAT | Oui | 1.0 à 20.0 (pas : 0.1) |
| `seed` | Graine pour l'échantillonnage. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | L'effet sonore généré. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSFXNode/fr.md)

---
**Source fingerprint (SHA-256):** `a1dcd374d158009aceae2aecd87ed08f8105bff7db75160a99e8624be9459dfa`
