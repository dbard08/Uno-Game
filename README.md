# Uno (Python)

## Setup
- 108-card deck. 2-4 players, chosen at the start. Each player is dealt 7 cards.
- The starting card must be a number card. If an action or Wild card is flipped, reshuffle and flip again.
- Score tracking is an optional toggle at the start. There is no Uno call.

## Deck
- Four colors (red, yellow, green, blue). Per color: one 0, two each of 1-9, two Skips, two Reverses, two Draw 2s (25 cards).
- Plus 4 Wilds and 4 Wild Draw 4s (no color). Total: 108.

## Playing a card
- A card is legal if it matches the top card's color or value. Wilds can be played anytime.
- Wild Draw 4 is only legal if you hold no card matching the current color.
- On your own turn you can play any number of identical action types together (Draw 2s, Skips, Reverses, Wild Draw 4s), and color doesn't matter between them.
- You can't mix draw cards. Draw 2s and Wild Draw 4s can't be stacked together.
- You can't stack onto a draw card another player just played on you.

## Effects
- **Draw 2:** the next player draws 2 and loses their turn. Multiples add up (three Draw 2s = 6 cards).
- **Wild Draw 4:** the next player draws 4 and loses their turn. Multiples add up the same way.
- **Skip:** the next player loses their turn. Multiples skip that many players.
- **Reverse:** flips direction. An even number played cancels out, an odd number reverses. With 2 players still in the game, a Reverse acts like a Skip.
- **Wild:** you choose the new color.

## No play (or no desire to play)
- You draw exactly one card and your turn ends. You never draw until you find a playable card.
- You can choose to draw even if you have a legal play.
- The drawn card can't be played that turn.
- If the deck runs out, reshuffle the discard pile (except the top card).

## Going out
- You must go out on a regular number card. Wilds count as action cards.
- If you go out on action cards, you pick up 2 and the game continues. The card's effect still applies to the next player.

## Game modes
**Scoring off (Last Player Standing):** when a player goes out, they leave the game but play continues. Players finish 1st, 2nd, 3rd, and so on until one player is left. With 2 players, the first to go out wins.

**Scoring on:** a round ends the moment one player goes out. Every other player adds the value of the cards left in their hand to their running score. The player who went out adds 0. Lowest score is best. The game ends when a player reaches the score limit (chosen at the start, default 100), and the player with the lowest total wins.

## Point values
- Number cards: face value
- Skip, Reverse, Draw 2: 20 each
- Wild, Wild Draw 4: 50 each