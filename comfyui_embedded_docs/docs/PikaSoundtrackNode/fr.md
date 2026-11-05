# Pika Soundtrack

Ce nœud génère une bande-son synchronisée pour une vidéo avec Pika. L'image et la durée sont conservées ; seul l'audio est remplacé. Décrivez le son souhaité, ou laissez l'instruction vide pour le déduire de l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Le clip pour lequel écrire une bande-son. Jusqu'à 10 minutes. | VIDEO | Oui | - |
| `instruction` | Le contenu audio souhaité : effets sonores, ambiance, musique ou style. Laissez vide pour le déduire de l'image. Par défaut : "" (chaîne vide). | STRING | Oui | 0 à 10000 caractères |
| `seed` | Graine pour l'échantillonnage. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes :**

* La vidéo d'entrée doit durer 10 minutes ou moins.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le clip d'entrée avec la bande-son générée à la place de l'audio d'origine. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSoundtrackNode/fr.md)

---
**Source fingerprint (SHA-256):** `9820efec607ba52dbabe5e4fb0862240fb0f0215ce7e72914451823b7e75120b`
