# FishAudioTextToSpeech

Ce nœud convertit le texte écrit en audio parlé en utilisant les modèles de synthèse vocale Fish Audio. Il prend en charge les indices d'émotion intégrés dans le texte ([happy], [whispering] sur s2.1-pro ; (happy) sur s1) et le dialogue multi-locuteur à l'aide des balises @Voice1/@Voice2 lorsque plusieurs voix sont connectées. Deux modèles sont disponibles : s2.1-pro, qui prend en charge jusqu'à cinq voix et le dialogue multi-locuteur, et s1, qui utilise une seule voix facultative.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Le texte à convertir en parole. Avec deux voix ou plus connectées, marquez les changements de locuteur avec @Voice1, @Voice2, etc. Ne doit pas être vide. (défaut : vide) | STRING | Oui | Any non-empty text |
| `model` | Modèle à utiliser pour la synthèse vocale. | DYNAMIC_COMBO | Oui | "s2.1-pro"<br>"s1" |
| `seed` | La graine (seed) contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. (défaut : 42) | INT | Oui | 0 to 2147483647 |

### Entrées s2.1-pro

Ces entrées apparaissent lorsque le modèle s2.1-pro est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voices` | Emplacement extensible : connectez 1 à 5 éléments de voix (`voice_1`, `voice_2`, ...). Voix pour la synthèse. Laissez vide pour la voix par défaut. Avec deux voix ou plus, marquez les changements de locuteur dans le texte avec @Voice1, @Voice2, etc. | FISHAUDIO_VOICE | Non | 0 to 5 voices |
| `temperature` | Expressivité. Des valeurs plus élevées donnent des résultats plus variés, des valeurs plus faibles sont plus cohérentes. (défaut : 0.7) | FLOAT | Oui | 0.0 to 1.0 |
| `top_p` | Diversité via l'échantillonnage par noyau (nucleus sampling). (défaut : 0.7) | FLOAT | Oui | 0.01 to 1.0 |
| `speed` | Débit de parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide. (défaut : 1.0) | FLOAT | Oui | 0.5 to 2.0 |
| `volume` | Réglage du volume en décibels. 0 correspond à aucun changement. (défaut : 0.0) | FLOAT | Oui | -10.0 to 10.0 |
| `normalize` | Normalise les nombres et le texte pour l'anglais et le chinois, améliorant la stabilité des nombres et des dates. (défaut : true) | BOOLEAN | Oui | true / false |

### Entrées s1

Ces entrées apparaissent lorsque le modèle s1 est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voice` | Voix pour la synthèse. Laissez non connecté pour la voix par défaut. | FISHAUDIO_VOICE | Non | Optional single voice |
| `temperature` | Expressivité. Des valeurs plus élevées donnent des résultats plus variés, des valeurs plus faibles sont plus cohérentes. (défaut : 0.7) | FLOAT | Oui | 0.0 to 1.0 |
| `top_p` | Diversité via l'échantillonnage par noyau (nucleus sampling). (défaut : 0.7) | FLOAT | Oui | 0.01 to 1.0 |
| `speed` | Débit de parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide. (défaut : 1.0) | FLOAT | Oui | 0.5 to 2.0 |
| `volume` | Réglage du volume en décibels. 0 correspond à aucun changement. (défaut : 0.0) | FLOAT | Oui | -10.0 to 10.0 |
| `normalize` | Normalise les nombres et le texte pour l'anglais et le chinois, améliorant la stabilité des nombres et des dates. (défaut : true) | BOOLEAN | Oui | true / false |

**Remarque :** L'entrée `text` ne doit pas être vide. Les balises de locuteur (@Voice1, @Voice2, etc.) sont insensibles à la casse et doivent faire référence à une voix connectée ; marquer une voix qui n'est pas connectée génère une erreur. Lorsque deux voix ou plus sont connectées, le texte doit référencer chaque voix connectée au moins une fois, sinon le nœud signale les balises manquantes. Sur s2.1-pro, connecter 0 voix utilise la voix par défaut, 1 voix utilise cette voix seule, et 2 voix ou plus activent le dialogue multi-locuteur. Sur s1, une seule voix facultative est utilisée et la laisser non connectée utilise la voix par défaut. Les indices d'émotion peuvent être placés dans le texte : [happy] et [whispering] sur s2.1-pro, et (happy) sur s1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | La parole générée sous forme de fichier audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/fr.md)

---
**Source fingerprint (SHA-256):** `6cc005ae76fc7b60d9399b1b0a3c5de40a6eff47cd6f0f0b73b4212c0270ae29`
