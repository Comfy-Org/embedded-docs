> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/fr.md)

Le nœud ElevenLabs Voice Selector vous permet de choisir une voix spécifique parmi une liste prédéfinie de voix de synthèse vocale ElevenLabs. Il prend un nom de voix en entrée et renvoie l'identifiant correspondant nécessaire à la génération audio. Ce nœud simplifie le processus de sélection d'une voix compatible pour une utilisation avec d'autres nœuds audio ElevenLabs.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `voice` | STRING | Oui | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | Choisissez une voix parmi les voix prédéfinies d'ElevenLabs. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `voice` | STRING | L'identifiant unique de la voix ElevenLabs sélectionnée, qui peut être transmis à d'autres nœuds pour la génération de synthèse vocale. |