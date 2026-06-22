# Sélecteur de voix ElevenLabs

Voici la traduction en français de la documentation du nœud ElevenLabs Voice Selector :

Le nœud ElevenLabs Voice Selector vous permet de choisir une voix spécifique parmi une liste prédéfinie de voix de synthèse vocale ElevenLabs. Il prend un nom de voix en entrée et fournit en sortie l'identifiant vocal correspondant nécessaire à la génération audio. Ce nœud simplifie le processus de sélection d'une voix compatible pour une utilisation avec d'autres nœuds audio ElevenLabs.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voix` | Choisissez une voix parmi les voix prédéfinies ElevenLabs. | STRING | Oui | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voix` | L'identifiant unique de la voix ElevenLabs sélectionnée, qui peut être transmis à d'autres nœuds pour la génération de synthèse vocale. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/fr.md)

---
**Source fingerprint (SHA-256):** `b87f5b2b8accca87d0593ab1f4bcfccaa84b393ddb3fd9121758a87871592cee`
