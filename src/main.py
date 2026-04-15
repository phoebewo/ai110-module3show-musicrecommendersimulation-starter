"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


USERS = {
    # --- Original profiles ---
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.3,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "likes_acoustic": False,
    },

    # --- Adversarial / edge-case profiles ---
    "Sad Hype Beast": {
        # mood="sad" doesn't exist in catalog — 2.0 pts permanently unreachable
        "genre": "pop",
        "mood": "sad",
        "energy": 0.9,
        "likes_acoustic": False,
    },
    "Perfectly Average": {
        # energy=0.5 sits between catalog songs — tests tie-breaking
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.5,
        "likes_acoustic": True,
    },
    "Obscure Taste": {
        # genre and mood don't exist — winner decided by energy + acoustic only
        "genre": "metal",
        "mood": "aggressive",
        "energy": 0.91,
        "likes_acoustic": False,
    },
    "Dead Silent": {
        # energy=0.0 extreme low end — can genre match (3pts) beat energy gap?
        "genre": "rock",
        "mood": "intense",
        "energy": 0.0,
        "likes_acoustic": False,
    },
    "Ghost User": {},
    "Superhuman Energy": {
        # energy=2.0 out of range — energy_score goes negative, hidden bug
        "genre": "rock",
        "mood": "intense",
        "energy": 2.0,
        "likes_acoustic": False,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in USERS.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 40)
        print(f" {name}")
        print("=" * 40)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n#{i}  {song['title']} by {song['artist']}")
            print(f"    Score : {score:.2f} / 10.0")
            print(f"    Why   : {explanation}")
        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
