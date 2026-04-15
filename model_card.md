# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

It suggests songs based on your mood, genre, energy level, and whether you like acoustic music. This is a classroom project — not a real app. It's not meant to be used for actual music recommendations.

---

## 3. How the Model Works

Each song gets a score based on how well it matches what the user wants. Genre and mood get bonus points if they match exactly. Energy is scored by how close the song is to the user's target — closer means more points. Acoustic is a yes or no match. The top 5 highest-scoring songs are returned.

---

## 4. Data

The catalog has 10 songs. Each song has a genre, mood, energy level, and acousticness. Genres include pop, lofi, rock, jazz, and a few others. There are no sad, angry, or metal songs in the dataset at all.

---

## 5. Strengths

It works well when the user's taste matches what's in the catalog. A chill lofi fan gets quiet acoustic songs. A rock fan gets loud intense ones. The scores are easy to understand — you can always see exactly why a song ranked where it did.

---

## 6. Limitations and Bias

The catalog is too small and uneven. Most songs are either very low or very high energy, so middle-energy users never get a great match. Moods like "sad" and genres like "metal" don't exist in the data, so those users always get weaker results.

---

## 7. Evaluation

I tested nine profiles — three normal ones and six edge cases designed to stress-test the system. The normal profiles worked as expected. The most surprising result was that a "sad pop" user got the exact same recommendations as a "happy pop" user, because no sad songs exist in the catalog. An out-of-range energy value (2.0) also caused the formula to silently give negative scores.

---

## 8. Future Work

- Add more songs, especially ones with moods like "sad" or genres like "metal" so more users get useful results
- Score acousticness on a scale instead of yes or no, so a slightly acoustic song still gets some credit
- Let users say what they don't like, so the system can actively avoid recommending those songs

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
