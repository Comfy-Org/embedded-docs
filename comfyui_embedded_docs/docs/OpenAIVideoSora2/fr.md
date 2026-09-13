# OpenAI Sora - Vidéo

Le nœud OpenAIVideoSora2 génère des vidéos avec les modèles Sora d'OpenAI. Il prend une invite textuelle ainsi qu'une seule image de référence facultative, envoie la requête à OpenAI, attend la fin de la génération, puis renvoie la vidéo résultante. Les durées et résolutions prises en charge dépendent du modèle sélectionné.

**AVIS DE DÉPRÉCIATION :** OpenAI cessera de fournir l'API Sora v2 en septembre 2026. Ce nœud sera supprimé de ComfyUI à cette date.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle Sora d'OpenAI à utiliser pour la génération de vidéo (par défaut : "sora-2") | COMBO | Oui | "sora-2"<br>"sora-2-pro" |
| `prompt` | Texte de guidage ; peut être vide si une image d'entrée est présente (par défaut : chaîne vide) | STRING | Oui | - |
| `size` | Résolution de la vidéo générée (par défaut : "1280x720") | COMBO | Oui | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | Durée de la vidéo générée en secondes (par défaut : 8) | COMBO | Oui | 4<br>8<br>12 |
| `image` | Image de référence d'entrée facultative utilisée pour la génération de vidéo ; une seule image est prise en charge | IMAGE | Non | - |
| `seed` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Contraintes et limitations :**

- Le modèle "sora-2" ne prend en charge que les tailles "720x1280" et "1280x720" ; sélectionner "1024x1792" ou "1792x1024" avec "sora-2" provoque une erreur. Les tailles plus grandes ne sont disponibles qu'avec "sora-2-pro".
- Lorsqu'une image est connectée, une seule image doit être fournie ; en connecter plusieurs déclenche une erreur.
- Les résultats sont non déterministes quelle que soit la valeur de la graine.
- L'estimation de prix affichée dépend des paramètres `model`, `size` et `duration` sélectionnés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Vidéo générée par OpenAI Sora | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/fr.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
