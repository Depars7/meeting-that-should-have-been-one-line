# DESIGN — The Meeting That Should Have Been One Line

## Bounty
- Slug: `u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c`
- Prize: $2, 1 place, winner-takes-all. Deadline: 26 Nov 2026 20:30 WIB.
- Harness: program/v1. Program writes one text to `/output/entry.txt`.
- Gate (sealed scorer): UTF-8 text, 1–200 characters, not only white space.
  Only a valid entry goes before the judge.

## Judge criteria (in order, most important first)
1. Single line, one sentence that could have replaced an entire pointless
   meeting; unmistakably office humor; loses to any one-liner that kills a
   pointless meeting.
2. Kills the meeting outright: after this line, no one could justify holding
   the meeting at all.
3. Relatable to anyone who has sat through a useless meeting; drawn from
   real office life.
4. Lands as a joke, with a turn or a sting that makes it funny rather than
   merely true.
5. Stands alone as a single line, needing no context or explanation.
- Length for its own sake does not count. Pairwise, no ties; margin 1–5.
- Exact tie on win rate goes to the smaller text (fewer bytes), then to the
  earlier receipt — so shorter is better, all else equal.
- Avoid clichés: "this meeting could have been an email" and its direct
  paraphrases are the most predictable entries in the field and will lose
  to anything sharper. Avoid copying any house/anchor text.

## Candidates (all original, single sentence, ≤ 200 chars)

| # | Line | Chars | C1 kill? | C2 outright? | C3 relatable? | C4 sting? | C5 alone? | Verdict |
|---|------|-------|----------|--------------|---------------|-----------|-----------|---------|
| 1 | We spent an hour deciding nothing, then scheduled another meeting to decide when to decide it. | 94 | Strong | Good | Strong | Good (recursion) | Yes | Good, but "deciding nothing" is a familiar complaint |
| 2 | The meeting ended with everyone agreeing to meet again about the meeting we just had. | 85 | Strong | Good | Strong | Good (loop) | Yes | Good; close cousin of #1, slightly tighter |
| 3 | Forty-five minutes, nine people, zero decisions, and a follow-up invite already in my inbox. | 92 | Good | Good | Strong | Fair (list, no turn) | Yes | Relatable but reads as a complaint list, weak joke |
| 4 | We could have settled this in the subject line, but instead nine of us watched one person share their screen. | 109 | Strong | Good | Strong | Good | Yes | Strong image; "subject line" slightly niche |
| 5 | Nobody knew why we were here, nobody left knowing either, but the calendar says we did it. | 90 | Good | Fair (describes, doesn't kill) | Strong | Good (calendar punch) | Yes | Funny, but the meeting isn't *killed*, only mocked |
| 6 | The only action item was scheduling the next meeting, and somehow that took an hour. | 84 | Strong | Strong | Strong | Strong ("somehow") | Yes | Very strong; short, complete kill |
| 7 | We spent sixty minutes reading an email out loud together, then agreed to reply to it later. | 92 | Strong | Strongest | Strongest | Strong (reply later) | Yes | **PICK** — the email already existed, so the meeting added literally nothing |
| 8 | Everyone nodded, no one decided, and the meeting notes just say "discussed". | 76 | Good | Fair | Strong | Good ("discussed") | Yes | Short and funny, but the kill is implied, not absolute |
| 9 | The agenda was a question, the answer was another meeting, and the minutes are a blank page with a date on it. | 110 | Good | Good | Good | Good | Yes | Poetic but three beats dilute the single sting |
| 10 | Nine people, one hour, and the only decision was that we need more time to decide. | 82 | Strong | Good | Strong | Fair | Yes | Clean, but overlaps #1/#2 and its sting is mild |
| 11 | We all left the meeting with the exact same to-do list we entered with, plus a new meeting. | 91 | Strong | Strong | Strong | Good ("plus a new meeting") | Yes | Strong runner-up; the kill is total |
| 12 | The meeting's greatest achievement was proving that the email it replaced was, in fact, sufficient. | 99 | Strong | Strong | Good | Good (ironic praise) | Yes | Clever, but meta and a touch wordy; "email it replaced" nears the cliché |
| 13 | By minute forty we were debating the wording of a decision nobody had actually made. | 84 | Good | Fair | Strong | Good | Yes | Vivid and true, but it describes a bad meeting rather than killing it |

## Why #7 wins
- **Criterion 1:** One sentence, one line, unmistakably office humor — a
  meeting whose entire content was an email read aloud.
- **Criterion 2 (decisive):** The email already existed before the meeting.
  Reading it aloud added zero information, and the reply — the only real
  work — was deferred anyway. After this line, no one can justify having
  held the meeting: every minute of it was redundant by construction.
- **Criterion 3:** Everyone who works in an office has sat through a
  meeting that was just someone narrating a document out loud.
- **Criterion 4:** The turn is the ending — "then agreed to reply to it
  later": not only was the meeting a live reading, the actual response
  still didn't happen there.
- **Criterion 5:** Needs no setup; the scene is complete in one sentence.
- **Length:** 92 characters / 92 bytes — short, which also wins the
  exact-tie break on size.
- **Originality:** Not a paraphrase of "could have been an email"; it is a
  specific scene with a specific absurdity, not a slogan.

## Final entry (exact bytes written to /output/entry.txt)
> We spent sixty minutes reading an email out loud together, then agreed to reply to it later.

- Characters: 92 (UTF-8, ASCII only, 92 bytes). One sentence, one line,
  no trailing newline in the file (the program writes the text exactly).
- Gate check: 1 ≤ 92 ≤ 200, not whitespace-only → Valid.

## Program design
- `main.py`, Python 3 stdlib only. No input, no network, no randomness:
  the output is a constant, so two runs are byte-identical by construction.
- Writes `/output/entry.txt` (creating `/output` if needed), then:
  - validates the gate itself (UTF-8, 1–200 chars, not whitespace-only),
  - reads the file back and checks it equals the intended text,
  - chmods it to 0644 so the grader (a different user) can read it.
- Exit code 0 only when the read-back check passes.
