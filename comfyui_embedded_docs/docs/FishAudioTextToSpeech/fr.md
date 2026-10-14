# Synthèse vocale Fish Audio

Ce nœud convertit le texte écrit en audio parlé à l’aide des modèles de synthèse vocale Fish Audio. Il prend en charge les indications intégrées au texte : [happy] et [whispering] sur s2.1-pro, (happy) sur s1, ainsi que les [directions] en langage naturel et les balises de mot `<whisper>...</whisper>` sur drama-3. Le dialogue multi-locuteurs utilise les balises @Voice1/@Voice2 lorsque plusieurs voix sont connectées. Trois modèles sont disponibles : drama-3 et s2.1-pro, qui prennent tous deux en charge jusqu’à cinq voix et le dialogue multi-locuteurs, et s1, qui utilise une voix unique facultative.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Texte à convertir en parole. Lorsque deux voix ou plus sont connectées, indiquez les changements de locuteur avec @Voice1, @Voice2, etc. (par défaut : vide) | STRING | Oui | Tout texte non vide |
| `model` | Modèle à utiliser pour la synthèse vocale. | DYNAMIC_COMBO | Oui | "drama-3"<br>"s2.1-pro"<br>"s1" |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Entrées drama-3 et s2.1-pro

Ces entrées apparaissent lorsque le modèle `drama-3` ou `s2.1-pro` est sélectionné. Les jeux de paramètres sont identiques.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voices` | Emplacement extensible : connectez 0 à 5 éléments de voix (`voice_1`, `voice_2`, ...). Voix pour la synthèse. Laissez vide pour une voix aléatoire. Avec deux voix ou plus, indiquez les changements de locuteur dans le texte avec @Voice1, @Voice2, etc. | FISHAUDIO_VOICE | Non | 0 à 5 voix |
| `temperature` | Expressivité. Des valeurs élevées sont plus variées, des valeurs faibles sont plus cohérentes. (par défaut : 0.7) | FLOAT | Oui | 0.0 à 1.0 |
| `top_p` | Diversité via échantillonnage noyau. (par défaut : 0.7) | FLOAT | Oui | 0.01 à 1.0 |
| `speed` | Débit de parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide. (par défaut : 1.0) | FLOAT | Oui | 0.5 à 2.0 |
| `volume` | Ajustement du volume en décibels. 0 correspond à aucun changement. (par défaut : 0.0) | FLOAT | Oui | -10.0 à 10.0 |
| `normalize` | Normalise les nombres et le texte pour l’anglais et le chinois, ce qui améliore la stabilité des nombres et des dates. (par défaut : true) | BOOLEAN | Oui | true / false |

### Entrées s1

Ces entrées apparaissent lorsque le modèle s1 est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `voice` | Voix pour la synthèse. Laissez non connecté pour une voix aléatoire. | FISHAUDIO_VOICE | Non | Voix unique facultative |
| `temperature` | Expressivité. Des valeurs élevées sont plus variées, des valeurs faibles sont plus cohérentes. (par défaut : 0.7) | FLOAT | Oui | 0.0 à 1.0 |
| `top_p` | Diversité via échantillonnage noyau. (par défaut : 0.7) | FLOAT | Oui | 0.01 à 1.0 |
| `speed` | Débit de parole. 1.0 est normal, <1.0 plus lent, >1.0 plus rapide. (par défaut : 1.0) | FLOAT | Oui | 0.5 à 2.0 |
| `volume` | Ajustement du volume en décibels. 0 correspond à aucun changement. (par défaut : 0.0) | FLOAT | Oui | -10.0 à 10.0 |
| `normalize` | Normalise les nombres et le texte pour l’anglais et le chinois, ce qui améliore la stabilité des nombres et des dates. (par défaut : true) | BOOLEAN | Oui | true / false |

**Remarque :** L’entrée `text` ne doit pas être vide. Les balises de locuteur (@Voice1, @Voice2, etc.) sont insensibles à la casse et doivent faire référence à une voix connectée ; baliser une voix non connectée génère une erreur. Lorsque deux voix ou plus sont connectées, le texte doit référencer chaque voix connectée au moins une fois, sinon le nœud signale les balises manquantes. Sur drama-3 et s2.1-pro, connecter 0 voix utilise une voix aléatoire, 1 voix utilise cette voix seule, et 2 voix ou plus activent le dialogue multi-locuteurs. Sur s1, une voix unique facultative est utilisée et la laisser non connectée utilise une voix aléatoire. Des indications peuvent être placées dans le texte : [happy] et [whispering] sur s2.1-pro, (happy) sur s1, ainsi que les [directions] en langage naturel et les balises de mot `<whisper>...</whisper>` sur drama-3.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | La parole générée sous forme de fichier audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/fr.md)

---
**Source fingerprint (SHA-256):** `adcfe8f994b8fbe07efb3dd3f86c8955ea3cec62cc3f0321efd2b63c0470b7a3`
