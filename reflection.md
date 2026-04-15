# Reflection: Comparing User Profile Outputs

---

## High-Energy Pop vs Sad Hype Beast

Both profiles want pop music with high energy, but Sad Hype Beast adds mood: "sad."
The weird thing is they get almost the exact same results. That's because no song in
the catalog has the mood "sad," so the mood preference just gets ignored. The system
can't tell the difference between a user who's happy and a user who's sad — it treats
them the same. This feels wrong. A sad user probably doesn't want the same upbeat pop
as a happy one, but the system has no way to know that.

---

## Chill Lofi vs Perfectly Average

Chill Lofi (energy: 0.3) gets strong results — Library Rain and Midnight Coding both
match on genre, mood, and acoustic, and their energy levels are close to 0.3.
Perfectly Average (energy: 0.5) also wants lofi and chill, but its top results score
noticeably lower. That's because no song in the catalog has energy near 0.5 — songs
jump from 0.42 straight to 0.75. So even though the preferences are almost the same,
Perfectly Average gets penalized just for wanting something in the middle.

---

## Deep Intense Rock vs Obscure Taste

Deep Intense Rock gets great results because rock + intense + high energy all exist in
the catalog. Storm Runner matches on every single dimension and ranks first easily.
Obscure Taste wants metal and "aggressive" mood — neither of which exist in the catalog
at all. So it can never earn genre or mood points and ends up just getting ranked by
energy and acoustics. The top result is probably Storm Runner anyway since it has the
closest energy, but for completely different reasons. One profile is being served well,
the other is just getting leftovers.

---

## High-Energy Pop vs Deep Intense Rock

These two feel similar on the surface — both want high energy and non-acoustic songs.
The difference is genre and mood. High-Energy Pop gets Sunrise City first (pop, happy)
while Deep Intense Rock gets Storm Runner first (rock, intense). But here's something
worth noticing: Gym Hero (a pop workout song tagged as "intense") keeps showing up near
the top for the pop user even though its mood doesn't match "happy" at all. That happens
because genre is worth enough points that any pop song gets a head start over
non-pop songs, even ones with a better mood match. It's like the system thinks "same
genre = close enough," when really a gym anthem and a happy pop song feel nothing alike.

---

## Ghost User vs any normal profile

Ghost User has no preferences at all. Every single song scores 0.0 and the order is
basically random (whatever order they appear in the CSV). A normal profile at least gets
some songs bubbling to the top. This shows that the recommender has no fallback for
unknown users — it just gives up. Real systems handle this with things like "most
popular songs" as a default, but this one doesn't.

---

## Dead Silent vs Deep Intense Rock

Both want rock and intense, but Dead Silent has energy: 0.0 — basically asking for
silent rock, which doesn't exist. Deep Intense Rock gets Storm Runner at the top
because everything lines up. Dead Silent gets genre and mood points for Storm Runner
too, but then loses a huge chunk of energy points because Storm Runner has energy 0.91
which is as far from 0.0 as you can get. So a low-energy ambient song might actually
outscore a rock song for this user, even though the user explicitly asked for rock.
The energy score is so dominant now (worth 5 points) that it can override genre and
mood entirely when the gap is large enough.
